#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "metis-gtsam" for configuration "Release"
set_property(TARGET metis-gtsam APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(metis-gtsam PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libmetis-gtsam.so"
  IMPORTED_SONAME_RELEASE "libmetis-gtsam.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS metis-gtsam )
list(APPEND _IMPORT_CHECK_FILES_FOR_metis-gtsam "${_IMPORT_PREFIX}/lib/libmetis-gtsam.so" )

# Import target "CppUnitLite" for configuration "Release"
set_property(TARGET CppUnitLite APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(CppUnitLite PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libCppUnitLite.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS CppUnitLite )
list(APPEND _IMPORT_CHECK_FILES_FOR_CppUnitLite "${_IMPORT_PREFIX}/lib/libCppUnitLite.a" )

# Import target "gtsam" for configuration "Release"
set_property(TARGET gtsam APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(gtsam PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libgtsam.so.4.1.1"
  IMPORTED_SONAME_RELEASE "libgtsam.so.4"
  )

list(APPEND _IMPORT_CHECK_TARGETS gtsam )
list(APPEND _IMPORT_CHECK_FILES_FOR_gtsam "${_IMPORT_PREFIX}/lib/libgtsam.so.4.1.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
