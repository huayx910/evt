# - Find F-Stack DPDK
# Find the F-Stack DPDK library and includes
#
# DPDK_LIBRARIES - List of libraries when using DPDK.
# DPDK_FOUND - True if DPDK found.

find_library(DPDK_LIBRARIES
  NAMES lib/libdpdk.a
  HINTS ENV FF_DPDK)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(DPDK DEFAULT_MSG DPDK_LIBRARIES)

mark_as_advanced(
  DPDK_LIBRARIES)
