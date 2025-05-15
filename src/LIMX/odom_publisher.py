import json
import uuid
import threading
import time
import websocket
from datetime import datetime
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Point, Vector3
import tf

# Replace this ACCID value with your robot's actual serial number (SN)
ACCID = "WF_TRON1A_131"

# WebSocket client instance
ws_client = None

# ROS publishers
odom_pub = None
imu_pub = None

# Generate dynamic GUID
def generate_guid():
    return str(uuid.uuid4())

# Send WebSocket request with title and data
def send_request(title, data=None):
    if data is None:
        data = {}
    
    # Create message structure with necessary fields
    message = {
        "accid": ACCID,
        "title": title,
        "timestamp": int(time.time() * 1000),  # Current timestamp in milliseconds
        "guid": generate_guid(),
        "data": data
    }

    message_str = json.dumps(message)
    
    # Send the message through WebSocket if client is connected
    if ws_client:
        ws_client.send(message_str)

# Handle user commands
def handle_commands():
    send_request("request_enable_imu", {"enable": True})
    time.sleep(1)
    send_request("request_enable_odom", {"enable": True})
    time.sleep(1)

# WebSocket on_open callback
def on_open(ws):
    print("Connected!")
    # Start handling commands in a separate thread
    threading.Thread(target=handle_commands, daemon=True).start()

# WebSocket on_message callback
def on_message(ws, message):
    try:
        data = json.loads(message)
        if data["title"] == "notify_odom":
            # Create Odometry message
            odom_msg = Odometry()
            odom_msg.header.stamp = rospy.Time.now()
            odom_msg.header.frame_id = "odom"
            odom_msg.child_frame_id = "base_link"
            
            # Set position
            odom_msg.pose.pose.position = Point(
                data["data"]["pose_position"][0],
                data["data"]["pose_position"][1],
                data["data"]["pose_position"][2]
            )
            
            # Set orientation
            odom_msg.pose.pose.orientation = Quaternion(
                data["data"]["pose_orientation"][0],
                data["data"]["pose_orientation"][1],
                data["data"]["pose_orientation"][2],
                data["data"]["pose_orientation"][3]
            )
            
            # Set velocity
            odom_msg.twist.twist.linear = Vector3(
                data["data"]["twist_linear"][0],
                data["data"]["twist_linear"][1],
                data["data"]["twist_linear"][2]
            )
            odom_msg.twist.twist.angular = Vector3(
                data["data"]["twist_angular"][0],
                data["data"]["twist_angular"][1],
                data["data"]["twist_angular"][2]
            )
            
            # Publish odometry message
            odom_pub.publish(odom_msg)
            
        elif data["title"] == "notify_imu":
            # Create IMU message
            imu_msg = Imu()
            imu_msg.header.stamp = rospy.Time.now()
            imu_msg.header.frame_id = "imu_link"
            
            # Set orientation
            imu_msg.orientation = Quaternion(
                data["data"]["quat"][0],
                data["data"]["quat"][1],
                data["data"]["quat"][2],
                data["data"]["quat"][3]
            )
            
            # Set angular velocity
            imu_msg.angular_velocity = Vector3(
                data["data"]["gyro"][0],
                data["data"]["gyro"][1],
                data["data"]["gyro"][2]
            )
            
            # Set linear acceleration
            imu_msg.linear_acceleration = Vector3(
                data["data"]["acc"][0],
                data["data"]["acc"][1],
                data["data"]["acc"][2]
            )
            
            # Publish IMU message
            imu_pub.publish(imu_msg)
            
    except Exception as e:
        rospy.logerr(f"Error processing message: {str(e)}")

# WebSocket on_close callback
def on_close(ws, close_status_code, close_msg):
    print("Connection closed.")

# Close WebSocket connection
def close_connection(ws):
    ws.close()

def main():
    global ws_client, odom_pub, imu_pub
    
    # Initialize ROS node
    rospy.init_node('limx_odom_publisher')
    
    # Create publishers
    odom_pub = rospy.Publisher('/limx/wheel_odom', Odometry, queue_size=10)
    imu_pub = rospy.Publisher('/limx/imu', Imu, queue_size=10)
    
    # Create WebSocket client instance
    ws_client = websocket.WebSocketApp(
        "ws://10.192.1.2:5000",  # WebSocket server URI
        on_open=on_open,
        on_message=on_message,
        on_close=on_close
    )
    
    # Run WebSocket client loop
    print("Press Ctrl+C to exit.")
    ws_client.run_forever()

if __name__ == "__main__":
    main()