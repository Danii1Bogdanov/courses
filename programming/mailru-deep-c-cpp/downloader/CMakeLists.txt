cmake_minimum_required(VERSION 3.2)
project(downloader)

set(DOWNLOADER_LIBS downloader CACHE INTERNAL "")
set(DOWNLOADER_INC "${PROJECT_SOURCE_DIR}/include/")

include_directories(${DOWNLOADER_INC})

enable_testing()

add_subdirectory(src)
add_subdirectory(examples)

add_subdirectory(tests)
