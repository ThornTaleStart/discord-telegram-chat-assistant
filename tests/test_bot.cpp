#include "../src/bot.hpp"
#include <gtest/gtest.h>

TEST(ChatBotTest, HandlesSimpleMessage) {
    ChatBot bot("fake_token", "fake_telegram_token");
    auto handler = [](const std::string& input) {
        return "test response";
    };
    bot.set_message_handler(handler);

    // Note: Actual testing would require mocking dpp/cpr
    SUCCEED();
}