cmake_minimum_required(VERSION 3.20)
project(advent_of_code LANGUAGES CXX)

# global C++ settings
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# find all day sources like src/2015/day01.cpp, src/2023/day07.cpp, ...
file(GLOB_RECURSE DAY_SOURCES CONFIGURE_DEPENDS "src/*/day*.cpp")

if(NOT DAY_SOURCES)
  message(STATUS "No day sources found under src/<YEAR>/day*.cpp")
endif()

foreach(src ${DAY_SOURCES})
  # derive target name: aoc_<year>_<dayXX>
  # src looks like /.../src/2015/day01.cpp
  get_filename_component(fn   "${src}" NAME_WE)      # day01
  get_filename_component(dir  "${src}" DIRECTORY)    # .../src/2015
  get_filename_component(year "${dir}"  NAME)        # 2015
  set(tgt "aoc_${year}_${fn}")

  add_executable(${tgt} "${src}")
  target_include_directories(${tgt} PRIVATE "${CMAKE_SOURCE_DIR}/src")
  target_compile_features(${tgt} PRIVATE cxx_std_23)
endforeach()

# copy compile_commands.json to repo root so clangd finds it automatically
if(CMAKE_EXPORT_COMPILE_COMMANDS)
  add_custom_target(copy_compile_commands ALL
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${CMAKE_BINARY_DIR}/compile_commands.json"
            "${CMAKE_SOURCE_DIR}/compile_commands.json"
    COMMENT "Copying compile_commands.json to project root for clangd")
endif()
