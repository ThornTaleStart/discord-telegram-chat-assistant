from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import Config
from ai_handler import AIHandler

ai = AIHandler()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI assistant. Send me a message or use /ask.")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Please provide a question. Usage: /ask <your question>")
        return
    response = ai.get_response(question)
    await update.message.reply_text(response)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = ai.get_response(update.message.text)
    await update.message.reply_text(response)

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ai.history.clear()
    await update.message.reply_text("Chat history cleared.")

def run_telegram():
    Config.validate()
    app = Application.builder().token(Config.TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Telegram bot started...")
    app.run_polling()