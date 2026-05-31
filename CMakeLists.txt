cmake_minimum_required(VERSION 3.10)
project(discord-telegram-chat-assistant)

set(CMAKE_CXX_STANDARD 17)

find_package(nlohmann_json REQUIRED)
find_package(cpr REQUIRED)
find_package(dpp REQUIRED)

add_executable(chat_assistant
    src/main.cpp
    src/bot.cpp
    src/bot.hpp
    src/config.cpp
    src/config.hpp
)

target_link_libraries(chat_assistant
    PRIVATE
    dpp::dpp
    cpr::cpr
    nlohmann_json::nlohmann_json
)