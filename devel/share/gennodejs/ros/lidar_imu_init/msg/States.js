// Auto-generated. Do not edit!

// (in-package lidar_imu_init.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class States {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.rot_end = null;
      this.pos_end = null;
      this.vel_end = null;
      this.bias_gyr = null;
      this.bias_acc = null;
      this.gravity = null;
      this.cov = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('rot_end')) {
        this.rot_end = initObj.rot_end
      }
      else {
        this.rot_end = [];
      }
      if (initObj.hasOwnProperty('pos_end')) {
        this.pos_end = initObj.pos_end
      }
      else {
        this.pos_end = [];
      }
      if (initObj.hasOwnProperty('vel_end')) {
        this.vel_end = initObj.vel_end
      }
      else {
        this.vel_end = [];
      }
      if (initObj.hasOwnProperty('bias_gyr')) {
        this.bias_gyr = initObj.bias_gyr
      }
      else {
        this.bias_gyr = [];
      }
      if (initObj.hasOwnProperty('bias_acc')) {
        this.bias_acc = initObj.bias_acc
      }
      else {
        this.bias_acc = [];
      }
      if (initObj.hasOwnProperty('gravity')) {
        this.gravity = initObj.gravity
      }
      else {
        this.gravity = [];
      }
      if (initObj.hasOwnProperty('cov')) {
        this.cov = initObj.cov
      }
      else {
        this.cov = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type States
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [rot_end]
    bufferOffset = _arraySerializer.float64(obj.rot_end, buffer, bufferOffset, null);
    // Serialize message field [pos_end]
    bufferOffset = _arraySerializer.float64(obj.pos_end, buffer, bufferOffset, null);
    // Serialize message field [vel_end]
    bufferOffset = _arraySerializer.float64(obj.vel_end, buffer, bufferOffset, null);
    // Serialize message field [bias_gyr]
    bufferOffset = _arraySerializer.float64(obj.bias_gyr, buffer, bufferOffset, null);
    // Serialize message field [bias_acc]
    bufferOffset = _arraySerializer.float64(obj.bias_acc, buffer, bufferOffset, null);
    // Serialize message field [gravity]
    bufferOffset = _arraySerializer.float64(obj.gravity, buffer, bufferOffset, null);
    // Serialize message field [cov]
    bufferOffset = _arraySerializer.float64(obj.cov, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type States
    let len;
    let data = new States(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [rot_end]
    data.rot_end = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [pos_end]
    data.pos_end = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [vel_end]
    data.vel_end = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [bias_gyr]
    data.bias_gyr = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [bias_acc]
    data.bias_acc = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [gravity]
    data.gravity = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [cov]
    data.cov = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 8 * object.rot_end.length;
    length += 8 * object.pos_end.length;
    length += 8 * object.vel_end.length;
    length += 8 * object.bias_gyr.length;
    length += 8 * object.bias_acc.length;
    length += 8 * object.gravity.length;
    length += 8 * object.cov.length;
    return length + 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lidar_imu_init/States';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4a896a0d8c07506c836e98c3fa512a5e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header          # timestamp of the first lidar in a frame
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new States(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.rot_end !== undefined) {
      resolved.rot_end = msg.rot_end;
    }
    else {
      resolved.rot_end = []
    }

    if (msg.pos_end !== undefined) {
      resolved.pos_end = msg.pos_end;
    }
    else {
      resolved.pos_end = []
    }

    if (msg.vel_end !== undefined) {
      resolved.vel_end = msg.vel_end;
    }
    else {
      resolved.vel_end = []
    }

    if (msg.bias_gyr !== undefined) {
      resolved.bias_gyr = msg.bias_gyr;
    }
    else {
      resolved.bias_gyr = []
    }

    if (msg.bias_acc !== undefined) {
      resolved.bias_acc = msg.bias_acc;
    }
    else {
      resolved.bias_acc = []
    }

    if (msg.gravity !== undefined) {
      resolved.gravity = msg.gravity;
    }
    else {
      resolved.gravity = []
    }

    if (msg.cov !== undefined) {
      resolved.cov = msg.cov;
    }
    else {
      resolved.cov = []
    }

    return resolved;
    }
};

module.exports = States;
