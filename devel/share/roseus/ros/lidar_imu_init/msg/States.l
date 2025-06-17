;; Auto-generated. Do not edit!


(when (boundp 'lidar_imu_init::States)
  (if (not (find-package "LIDAR_IMU_INIT"))
    (make-package "LIDAR_IMU_INIT"))
  (shadow 'States (find-package "LIDAR_IMU_INIT")))
(unless (find-package "LIDAR_IMU_INIT::STATES")
  (make-package "LIDAR_IMU_INIT::STATES"))

(in-package "ROS")
;;//! \htmlinclude States.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass lidar_imu_init::States
  :super ros::object
  :slots (_header _rot_end _pos_end _vel_end _bias_gyr _bias_acc _gravity _cov ))

(defmethod lidar_imu_init::States
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:rot_end __rot_end) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:pos_end __pos_end) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:vel_end __vel_end) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:bias_gyr __bias_gyr) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:bias_acc __bias_acc) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:gravity __gravity) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:cov __cov) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _rot_end __rot_end)
   (setq _pos_end __pos_end)
   (setq _vel_end __vel_end)
   (setq _bias_gyr __bias_gyr)
   (setq _bias_acc __bias_acc)
   (setq _gravity __gravity)
   (setq _cov __cov)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:rot_end
   (&optional __rot_end)
   (if __rot_end (setq _rot_end __rot_end)) _rot_end)
  (:pos_end
   (&optional __pos_end)
   (if __pos_end (setq _pos_end __pos_end)) _pos_end)
  (:vel_end
   (&optional __vel_end)
   (if __vel_end (setq _vel_end __vel_end)) _vel_end)
  (:bias_gyr
   (&optional __bias_gyr)
   (if __bias_gyr (setq _bias_gyr __bias_gyr)) _bias_gyr)
  (:bias_acc
   (&optional __bias_acc)
   (if __bias_acc (setq _bias_acc __bias_acc)) _bias_acc)
  (:gravity
   (&optional __gravity)
   (if __gravity (setq _gravity __gravity)) _gravity)
  (:cov
   (&optional __cov)
   (if __cov (setq _cov __cov)) _cov)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64[] _rot_end
    (* 8    (length _rot_end)) 4
    ;; float64[] _pos_end
    (* 8    (length _pos_end)) 4
    ;; float64[] _vel_end
    (* 8    (length _vel_end)) 4
    ;; float64[] _bias_gyr
    (* 8    (length _bias_gyr)) 4
    ;; float64[] _bias_acc
    (* 8    (length _bias_acc)) 4
    ;; float64[] _gravity
    (* 8    (length _gravity)) 4
    ;; float64[] _cov
    (* 8    (length _cov)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64[] _rot_end
     (write-long (length _rot_end) s)
     (dotimes (i (length _rot_end))
       (sys::poke (elt _rot_end i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _pos_end
     (write-long (length _pos_end) s)
     (dotimes (i (length _pos_end))
       (sys::poke (elt _pos_end i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _vel_end
     (write-long (length _vel_end) s)
     (dotimes (i (length _vel_end))
       (sys::poke (elt _vel_end i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _bias_gyr
     (write-long (length _bias_gyr) s)
     (dotimes (i (length _bias_gyr))
       (sys::poke (elt _bias_gyr i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _bias_acc
     (write-long (length _bias_acc) s)
     (dotimes (i (length _bias_acc))
       (sys::poke (elt _bias_acc i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _gravity
     (write-long (length _gravity) s)
     (dotimes (i (length _gravity))
       (sys::poke (elt _gravity i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _cov
     (write-long (length _cov) s)
     (dotimes (i (length _cov))
       (sys::poke (elt _cov i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64[] _rot_end
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _rot_end (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _rot_end i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _pos_end
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pos_end (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _pos_end i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _vel_end
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _vel_end (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _vel_end i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _bias_gyr
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bias_gyr (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _bias_gyr i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _bias_acc
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bias_acc (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _bias_acc i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _gravity
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _gravity (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _gravity i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _cov
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _cov (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _cov i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get lidar_imu_init::States :md5sum-) "4a896a0d8c07506c836e98c3fa512a5e")
(setf (get lidar_imu_init::States :datatype-) "lidar_imu_init/States")
(setf (get lidar_imu_init::States :definition-)
      "Header header          # timestamp of the first lidar in a frame
float64[] rot_end      # the estimated attitude (rotation matrix) at the end lidar point
float64[] pos_end      # the estimated position at the end lidar point (world frame)
float64[] vel_end      # the estimated velocity at the end lidar point (world frame)
float64[] bias_gyr     # gyroscope bias
float64[] bias_acc     # accelerator bias
float64[] gravity      # the estimated gravity acceleration
float64[] cov          # states covariance
# Pose6D[] IMUpose        # 6D pose at each imu measurements
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :lidar_imu_init/States "4a896a0d8c07506c836e98c3fa512a5e")


