cmake_minimum_required(VERSION 3.12)
project(RobotEmulator)

set(CMAKE_CXX_STANDARD 17)

add_executable(robot_emulator
    src/main.cpp
    src/MQTTClient.cpp
    src/EmuMotorController.cpp
)

target_include_directories(robot_emulator PRIVATE
    include
)

target_link_libraries(robot_emulator
    pthread
)
