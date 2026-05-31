#include "bot.hpp"
#include "config.hpp"
#include <iostream>

std::string simple_ai_response(const std::string& input) {
    if (input.find("hello") != std::string::npos) {
        return "Hello there! How can I help you today?";
    }
    return "I'm not sure how to respond to that. Try asking me something else!";
}

int main() {
    try {
        Config& config = Config::get_instance();
        ChatBot bot(config.get_discord_token(), config.get_telegram_token());
        bot.set_message_handler(simple_ai_response);
        bot.start();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}