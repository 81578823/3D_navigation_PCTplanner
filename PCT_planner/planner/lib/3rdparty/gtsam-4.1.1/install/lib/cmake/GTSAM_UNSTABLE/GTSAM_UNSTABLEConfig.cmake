# - Config file for GTSAM
# It defines the following variables
#  GTSAM_UNSTABLE_INCLUDE_DIR - include directories for GTSAM

# Compute paths
get_filename_component(OUR_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
if(EXISTS "${OUR_CMAKE_DIR}/CMakeCache.txt")
  # In build tree
  set(GTSAM_UNSTABLE_INCLUDE_DIR /home/wbb/catkin_ws_3d/PCT_planner/planner/lib/3rdparty/gtsam-4.1.1 CACHE PATH "GTSAM_UNSTABLE include directory")
else()
  # Find installed library
  set(GTSAM_UNSTABLE_INCLUDE_DIR "${OUR_CMAKE_DIR}/../../../include" CACHE PATH "GTSAM_UNSTABLE include directory")
endif()

# Find dependencies, required by cmake exported targets:
include(CMakeFindDependencyMacro)
# Allow using cmake < 3.8
if(${CMAKE_VERSION} VERSION_LESS "3.8.0")
find_package(Boost 1.65 COMPONENTS serialization;system;filesystem;thread;program_options;date_time;timer;chrono;regex)
else()
find_dependency(Boost 1.65 COMPONENTS serialization;system;filesystem;thread;program_options;date_time;timer;chrono;regex)
endif()

# Load exports
include(${OUR_CMAKE_DIR}/GTSAM_UNSTABLE-exports.cmake)

# Load project-specific flags, if present
if(EXISTS "${OUR_CMAKE_DIR}/gtsam_extra.cmake")
	include("${OUR_CMAKE_DIR}/gtsam_extra.cmake")
endif()

message(STATUS "GTSAM include directory:  ${GTSAM_INCLUDE_DIR}")
