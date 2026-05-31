import sys
from discord_bot import run_discord
from telegram_bot import run_telegram

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py [discord|telegram]")
        sys.exit(1)

    platform = sys.argv[1].lower()
    if platform == "discord":
        run_discord()
    elif platform == "telegram":
        run_telegram()
    else:
        print("Invalid platform. Use 'discord' or 'telegram'.")
        sys.exit(1)

if __name__ == "__main__":
    main()