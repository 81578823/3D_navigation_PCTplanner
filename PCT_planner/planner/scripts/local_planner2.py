#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist, Point
from nav_msgs.msg import Odometry, Path
from tf.transformations import euler_from_quaternion
import math
import json
import uuid
import threading
import time
import websocket
from datetime import datetime

# Replace this ACCID value with your robot's actual serial number (SN)
ACCID = "WF_TRON1A_131"

# Atomic flag for graceful exit
should_exit = False

# WebSocket client instance
ws_client = None

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

def on_open(ws):
    print("Connected!")
    # Start handling commands in a separate thread

# WebSocket on_message callback
def on_message(ws, message):
    print(f"Received message: {message}")  # Print the received message

# WebSocket on_close callback
def on_close(ws, close_status_code, close_msg):
    print("Connection closed.")

# Close WebSocket connection
def close_connection(ws):
    ws.close()

class LocalPlanner:
    def __init__(self):
        # 初始化ROS节点
        rospy.init_node("local_planner")

        # 参数设置
        self.lookahead_distance = 1.0    # 前瞻距离（单位：米）
        self.max_speed = 0.3             # 最大线速度（m/s）
        self.kp_angular = 0.2            # 转向角比例系数
        self.last_speed = 0.0
        self.MAX_ACCEL = 0.3  # m/s²
        
        # 订阅全局路径和机器人位姿
        self.current_path = None
        self.current_pose = None
        rospy.Subscriber("/pct_path", Path, self.path_callback)
        rospy.Subscriber("/localization", Odometry, self.odom_callback)
        self.target_pub = rospy.Publisher("/target_point", Point, queue_size=1)

        # 发布控制指令
        self.cmd_vel_pub = rospy.Publisher("/topic/limx/twist", Twist, queue_size=1)

    def path_callback(self, msg):
        """接收全局路径并转换为坐标点列表"""
        self.current_path = [
            (p.pose.position.x, p.pose.position.y) 
            for p in msg.poses
        ]
        rospy.loginfo("Received new path with {} points".format(len(self.current_path)))

    def odom_callback(self, msg):
        """获取当前机器人位姿"""
        self.current_pose = msg.pose.pose

    def get_closest_point(self):
        """找到路径中距离机器人最近的点的索引"""
        if not self.current_path or self.current_pose is None:
            return -1

        robot_pos = np.array([
            self.current_pose.position.x, 
            self.current_pose.position.y
        ])
        distances = [
            np.linalg.norm(robot_pos - np.array(p)) 
            for p in self.current_path
        ]
        return np.argmin(distances)

    def find_target_point(self, closest_idx):
        """根据前瞻距离选择目标点"""
        if closest_idx < 0 or closest_idx >= len(self.current_path)-1:
            return None

        # 从最近点开始向后搜索
        for i in range(closest_idx, len(self.current_path)):
            target = np.array(self.current_path[i])
            robot_pos = np.array([
                self.current_pose.position.x,
                self.current_pose.position.y
            ])
            distance = np.linalg.norm(target - robot_pos)
            if distance >= self.lookahead_distance:
                return target

        # 如果所有点都小于前瞻距离，选择终点
        return np.array(self.current_path[-1])

    def calculate_velocity(self, target):
        """Pure Pursuit转向计算"""
        # 获取机器人航向角
        (_, _, yaw) = euler_from_quaternion([self.current_pose.orientation.x, self.current_pose.orientation.y,
                                    self.current_pose.orientation.z, self.current_pose.orientation.w])

        # 计算目标点在机器人坐标系中的位置
        robot_pos = np.array([
            self.current_pose.position.x, 
            self.current_pose.position.y
        ])
        delta = target - robot_pos
        angle_diff=math.atan2(delta[1], delta[0]) - yaw
        # 归一化角度到[-pi, pi]
        if angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2 * math.pi
        angular_speed = 0.8 * angle_diff # 计算相对角度
        
        linear_speed = min(self.max_speed, (delta[0] - 0.2))

        return angular_speed,linear_speed

    def run(self):
        rate = rospy.Rate(10)  # 10Hz控制频率
        while not rospy.is_shutdown():
            if self.current_path is None or self.current_pose is None:
                rate.sleep()
                continue

            # 路径跟踪逻辑
            closest_idx = self.get_closest_point()
            target = self.find_target_point(closest_idx)
            
            if target is not None:
                point_msg = Point(x=target[0], y=target[1], z=0)
                self.target_pub.publish(point_msg)
                
            if target is None:
                # 发布停止指令
                # twist = Twist()
                # self.cmd_vel_pub.publish(twist)
                send_request("request_emgy_stop")
                rospy.loginfo("The mission has completed, no target found.")
                break
                

                # rate.sleep()
                # continue

            # 计算控制指令
            angular_speed, linear_speed= self.calculate_velocity(target)
                        
            # 接近终点时减速
            if closest_idx >= len(self.current_path)-3:
                linear_speed *= 0.3
                
            # 在发布速度前添加：
            delta_speed = linear_speed - self.last_speed
            if abs(delta_speed) > self.MAX_ACCEL * 0.1:  # 0.1s周期
                linear_speed = self.last_speed + np.sign(delta_speed) * self.MAX_ACCEL * 0.1
            self.last_speed = linear_speed
            
            # 发布指令
            # twist = Twist()
            # twist.linear.x = linear_speed
            # twist.angular.z = angular_speed
            # self.cmd_vel_pub.publish(twist)
            send_request("request_twist", {"x": linear_speed, "y": 0, "z": angular_speed})
            rate.sleep()

if __name__ == "__main__":    
    # Create WebSocket client instance
    ws_client = websocket.WebSocketApp(
        "ws://10.192.1.2:5000",  # WebSocket server URI
        on_open=on_open,
        on_message=on_message,
        on_close=on_close
    )
    planner = LocalPlanner()
    planner.run()