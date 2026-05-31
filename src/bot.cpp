#include "bot.hpp"
#include <cpr/cpr.h>
#include <iostream>

ChatBot::ChatBot(const std::string& token, const std::string& telegram_token)
    : discord_bot(token), telegram_token(telegram_token) {
    setup_discord_events();
}

void ChatBot::start() {
    discord_bot.start(dpp::st_wait);
}

void ChatBot::set_message_handler(std::function<std::string(const std::string&)> handler) {
    message_handler = handler;
}

void ChatBot::setup_discord_events() {
    discord_bot.on_message_create([this](const dpp::message_create_t& event) {
        if (event.msg.author.is_bot()) return;

        std::string response = message_handler(event.msg.content);
        event.reply(response);

        send_to_telegram("Discord: " + event.msg.content + "\nResponse: " + response);
    });
}

void ChatBot::send_to_telegram(const std::string& message) {
    cpr::Post(cpr::Url{"https://api.telegram.org/bot" + telegram_token + "/sendMessage"},
              cpr::Payload{{"chat_id", "YOUR_CHAT_ID"}, {"text", message}});
}