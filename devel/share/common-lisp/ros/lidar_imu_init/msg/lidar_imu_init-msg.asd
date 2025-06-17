
(cl:in-package :asdf)

(defsystem "lidar_imu_init-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Pose6D" :depends-on ("_package_Pose6D"))
    (:file "_package_Pose6D" :depends-on ("_package"))
    (:file "States" :depends-on ("_package_States"))
    (:file "_package_States" :depends-on ("_package"))
  ))