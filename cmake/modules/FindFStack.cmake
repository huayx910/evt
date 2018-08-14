# - Find F-Stack
# Find the F-Stack library and includes
#
# FSTACK_INCLUDE_DIR - where to find ff_api.h, etc.
# FSTACK_LIBRARIES - List of libraries when using F-Stack.
# FSTACK_FOUND - True if F-Stack found.

find_path(FSTACK_INCLUDE_DIR
  NAMES lib/ff_api.h
  HINTS ENV FF_PATH)

find_library(FSTACK_LIBRARIES
  NAMES lib/libfstack.a
  HINTS ENV FF_PATH)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(FStack DEFAULT_MSG FSTACK_LIBRARIES FSTACK_INCLUDE_DIR)

mark_as_advanced(
  FSTACK_LIBRARIES
  FSTACK_INCLUDE_DIR)
