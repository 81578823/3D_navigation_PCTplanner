import sys
import argparse
import numpy as np

import rospy
from nav_msgs.msg import Path

from utils import *
from planner_wrapper import TomogramPlanner

sys.path.append('../')
from config import Config
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

parser = argparse.ArgumentParser()
parser.add_argument('--scene', type=str, default='Spiral', help='Name of the scene. Available: [\'Spiral\', \'Building\', \'Plaza\', \'Room\']')
args = parser.parse_args()
def goal_callback(msg):
    """接收目标点的回调函数"""
    global end_pos  # 声明修改全局变量
    # 从消息中提取目标点坐标
    end_pos = np.array([msg.pose.position.x, msg.pose.position.y], dtype=np.float32)
    # 触发新的路径规划
    pct_plan()

def localization_callback(msg):
    """接收定位数据的回调函数"""
    global start_pos  # 声明修改全局变量
    # 从消息中提取当前位置坐标
    start_pos = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y], dtype=np.float32)
    

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
elif args.scene == 'Room':
    tomo_file = 'scans_room'
    start_pos = np.array([-3.22, -1.69], dtype=np.float32)
    end_pos = np.array([5.84, 0.462], dtype=np.float32)
    start_height=0
    end_height=0
elif args.scene == 'Stairs':
    tomo_file = 'scans_stairs'
    start_pos = np.array([-3.4, -0.708], dtype=np.float32)
    end_pos = np.array([0.182, 0.29], dtype=np.float32)
    start_height=16
    end_height=20
elif args.scene == 'Common':
    tomo_file = 'scans'
    start_pos = np.array([2.53, 6.74], dtype=np.float32)
    end_pos = np.array([-3.48, 8.67], dtype=np.float32)
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
        # 订阅目标点话题（RViz中默认的2D Nav Goal话题）
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, goal_callback)
    rospy.Subscriber("/localization",Odometry, localization_callback)
    
    # 初始规划（使用场景默认目标点）
    pct_plan()

    rospy.spin()
