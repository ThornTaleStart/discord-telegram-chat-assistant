#pragma once
#include <string>
#include <nlohmann/json.hpp>

class Config {
public:
    static Config& get_instance();
    std::string get_discord_token() const;
    std::string get_telegram_token() const;
    std::string get_openai_key() const;

private:
    Config();
    nlohmann::json config_data;
    void load_config();
};