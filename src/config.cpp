#include "config.hpp"
#include <fstream>
#include <stdexcept>

Config::Config() {
    load_config();
}

Config& Config::get_instance() {
    static Config instance;
    return instance;
}

void Config::load_config() {
    std::ifstream config_file("config.json");
    if (!config_file.is_open()) {
        throw std::runtime_error("Could not open config.json");
    }
    config_file >> config_data;
}

std::string Config::get_discord_token() const {
    return config_data["discord_token"];
}

std::string Config::get_telegram_token() const {
    return config_data["telegram_token"];
}

std::string Config::get_openai_key() const {
    return config_data["openai_key"];
}