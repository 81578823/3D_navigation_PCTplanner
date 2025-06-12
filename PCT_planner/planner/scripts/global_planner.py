import sys
import argparse
import numpy as np

import rospy
from nav_msgs.msg import Path

from utils import *
from planner_wrapper import TomogramPlanner

sys.path.append('../')
from config import Config
from geometry_msgs.msg import PoseStamped, PointStamped
from nav_msgs.msg import Odometry

parser = argparse.ArgumentParser()
parser.add_argument('--scene', type=str, default='Spiral', help='Name of the scene. Available: [\'Spiral\', \'Building\', \'Plaza\', \'Room\']')
args = parser.parse_args()
def goal_callback(msg):
    """接收目标点的回调函数"""
    global end_pos, end_height  # 声明修改全局变量
    # 从消息中提取目标点坐标
    end_pos = np.array([msg.point.x, msg.point.y], dtype=np.float32)
    end_height = msg.point.z
    # 触发新的路径规划
    pct_plan()

def localization_callback(msg):
    """接收定位数据的回调函数"""
    global start_pos,  start_height# 声明修改全局变量
    # 从消息中提取当前位置坐标
    start_pos = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y], dtype=np.float32)
    start_height = msg.pose.pose.position.z

cfg = Config()

if args.scene == 'Spiral':
    tomo_file = 'spiral0.3_2'
    start_pos = np.array([-16.0, -6.0], dtype=np.float32)
    end_pos = np.array([-26.0, -5.0], dtype=np.float32)
elif args.scene == 'Building':
    tomo_file = 'building2_9'
    start_pos = np.array([11.1, 1.38], dtype=np.float32)
    end_pos = np.array([-6.0, -1.0], dtype=np.float32)
elif args.scene == 'Plaza':
    tomo_file = 'plaza3_10'
    start_pos = np.array([0.0, 0.0], dtype=np.float32)
    end_pos = np.array([1.98, 24.7], dtype=np.float32)
    start_height=0
    end_height=0
elif args.scene == 'Room':
    tomo_file = 'scans_room'
    start_pos = np.array([-3.22, -1.69], dtype=np.float32)
    end_pos = np.array([5.84, 0.462], dtype=np.float32)
    start_height=0
    end_height=0
elif args.scene == 'Stairs':
    tomo_file = 'stairs_best'
    start_pos = np.array([5.06, -0.379], dtype=np.float32)
    end_pos = np.array([6.99, 8.29], dtype=np.float32)
    start_height=0
    end_height=1.91
elif args.scene == 'Floor':
    tomo_file = 'floor_best'
    # start_pos = np.array([2.53, 6.74], dtype=np.float32)
    end_pos = np.array([4.8, -0.526], dtype=np.float32)
    start_height=0
    end_height=0
elif args.scene == 'Common':
    tomo_file = 'scans'
    start_pos = np.array([2.53, 6.74], dtype=np.float32)
    end_pos = np.array([4.8, -0.526], dtype=np.float32)
    start_height=5
    end_height=5

path_pub = rospy.Publisher("/pct_path", Path, latch=True, queue_size=1)
planner = TomogramPlanner(cfg)

def pct_plan():
    traj_3d = planner.plan(start_pos, end_pos, start_height, end_height)
    if traj_3d is not None:
        path_pub.publish(traj2ros(traj_3d))
        print("Trajectory published")

if __name__ == '__main__':
    rospy.init_node("pct_planner", anonymous=True)
    planner.loadTomogram(tomo_file)
    rospy.Subscriber("/localization", Odometry, localization_callback)
    rospy.Subscriber("/clicked_point", PointStamped, goal_callback)

    # 初始化目标队列
    end_poses = [
        np.array([6.99, 8.29, 1.91]),
        np.array([4.9, 8.28, 1.91]), 
        np.array([4.89, 2.42, 3.88])
    ]
    current_target_idx = 0
    
    # 主循环控制
    rate = rospy.Rate(10)  # 10Hz检测频率
    while not rospy.is_shutdown() and current_target_idx < len(end_poses):
        try:
            # 更新当前目标
            target = end_poses[current_target_idx]
            end_pos = target[:2]
            end_height = target[2]

            try:
                rospy.wait_for_message("/localization", Odometry, timeout=10)
            except rospy.ROSException:
                rospy.logerr("Timeout waiting for localization data.")
                exit()

            pct_plan()

            # 持续检测位置更新
            while not (np.linalg.norm(end_pos - start_pos) < 0.1 and abs(end_height - start_height) < 1):
                try:
                    rospy.wait_for_message("/localization", Odometry, timeout=10)
                except rospy.ROSException:
                    rospy.logerr("Timeout waiting for localization data.")
                    exit()

            current_target_idx += 1
            rospy.loginfo(f"Reached target {current_target_idx-1}, planning next...")
            rate.sleep()
            
        except rospy.ROSInterruptException:
            rospy.logerr("ROS interrupted")
            break

    rospy.spin()

