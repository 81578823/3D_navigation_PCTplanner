#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/point_cloud2_iterator.h>
#include <livox_ros_driver2/CustomMsg.h> 
 
ros::Publisher pointcloud_pub;
 
void livoxCallback(const livox_ros_driver2::CustomMsg::ConstPtr& msg) {
    // 初始化 PointCloud2 消息
    sensor_msgs::PointCloud2 cloud_msg;
    cloud_msg.header = msg->header;  // 保持时间戳和frame一致
    cloud_msg.height = 1;
    cloud_msg.width = msg->point_num;
    cloud_msg.is_dense = false;
 
 
    // 设置字段
    sensor_msgs::PointCloud2Modifier modifier(cloud_msg);
    modifier.setPointCloud2Fields(4,
                              "x", 1, sensor_msgs::PointField::FLOAT32,
                              "y", 1, sensor_msgs::PointField::FLOAT32,
                              "z", 1, sensor_msgs::PointField::FLOAT32,
                              "intensity", 1, sensor_msgs::PointField::FLOAT32);
    modifier.resize(msg->point_num);
 
    // 通过迭代器来填充 PointCloud2 的数据
    sensor_msgs::PointCloud2Iterator<float> iter_x(cloud_msg, "x");
    sensor_msgs::PointCloud2Iterator<float> iter_y(cloud_msg, "y");
    sensor_msgs::PointCloud2Iterator<float> iter_z(cloud_msg, "z");
    sensor_msgs::PointCloud2Iterator<float> iter_intensity(cloud_msg, "intensity");
 
    for (size_t i = 0; i < msg->point_num; ++i) {
        *iter_x = msg->points[i].x;
        *iter_y = msg->points[i].y;
        *iter_z = msg->points[i].z;
        *iter_intensity = static_cast<float>(msg->points[i].reflectivity);  // 转换 reflectivity
 
        ++iter_x; ++iter_y; ++iter_z; ++iter_intensity;
    }
 
    pointcloud_pub.publish(cloud_msg);
}
 
int main(int argc, char** argv) {
    ros::init(argc, argv, "livox_to_pcl_converter");
    ros::NodeHandle nh;
    ROS_INFO("livox to pcd ==> /livox/lidar to /livox/pointcloud");
    // 订阅 Livox 自定义消息
    ros::Subscriber livox_sub = nh.subscribe("/livox/lidar", 10, livoxCallback);
 
    // 发布 PointCloud2 消息
    pointcloud_pub = nh.advertise<sensor_msgs::PointCloud2>("/livox/pointcloud", 10);
 
    ros::spin();
    return 0;
}
