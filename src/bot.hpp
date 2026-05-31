#pragma once
#include <dpp/dpp.h>
#include <string>
#include <functional>
#include <map>

class ChatBot {
public:
    ChatBot(const std::string& token, const std::string& telegram_token);
    void start();
    void set_message_handler(std::function<std::string(const std::string&)> handler);

private:
    dpp::cluster discord_bot;
    std::string telegram_token;
    std::function<std::string(const std::string&)> message_handler;

    void setup_discord_events();
    void send_to_telegram(const std::string& message);
};