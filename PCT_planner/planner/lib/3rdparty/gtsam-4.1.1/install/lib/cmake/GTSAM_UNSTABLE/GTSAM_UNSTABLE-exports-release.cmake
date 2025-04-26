#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "gtsam_unstable" for configuration "Release"
set_property(TARGET gtsam_unstable APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(gtsam_unstable PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libgtsam_unstable.so.4.1.1"
  IMPORTED_SONAME_RELEASE "libgtsam_unstable.so.4"
  )

list(APPEND _IMPORT_CHECK_TARGETS gtsam_unstable )
list(APPEND _IMPORT_CHECK_FILES_FOR_gtsam_unstable "${_IMPORT_PREFIX}/lib/libgtsam_unstable.so.4.1.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
