# 🛡️ CyberGuard - Cybersecurity Assistant

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![Ollama](https://img.shields.io/badge/ollama-llama3.2-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Privacy](https://img.shields.io/badge/privacy-100%20local-purple)

<div align="center">
  <h3>Your Personal Cybersecurity Assistant • Created by Abhilash</h3>
  <p><i>100% Private • Runs Locally • No Internet Required</i></p>
</div>

---

## 📋 Overview

**CyberGuard** is a privacy-focused cybersecurity assistant that runs entirely on your local machine. It answers questions about phishing, ransomware, passwords, and online safety using a knowledge base stored in simple text files. All processing happens locally - your questions never leave your computer.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔒 **100% Private** | Everything runs on your computer - no data leaves your machine |
| 📚 **Knowledge Base** | All information stored in easy-to-edit text files |
| 🎯 **Cybersecurity Focus** | Specializes in phishing, ransomware, passwords, and online safety |
| 💬 **Natural Conversation** | Handles greetings, questions, and casual chat |
| 🚀 **Fast & Lightweight** | Optimized for CPU with llama3.2:1b model |
| 🛠️ **Customizable** | Add your own knowledge by simply adding text files |
| 📝 **Conversation Logs** | All chats saved to `bot_logs.txt` for reference |
| 👨‍💻 **Created by Abhilash** | Developed by a cybersecurity enthusiast |

## 📁 Project Structure

cyberguard/
├── 📁 cybersecurity_docs/ # 📚 ALL KNOWLEDGE FILES
│ ├── greetings.txt # Greetings & casual responses
│ ├── creator_info.txt # Bot identity & creator info
│ ├── phishing.txt # Phishing information
│ ├── ransomware_complete.txt # Ransomware guide
│ ├── internet_attacks.txt # DDoS, MitM, etc.
│ ├── password_policy.txt # Password security
│ └── ... (more topic files)
├── 🤖 chatbot.py # 🧠 MAIN BOT CODE
├── 📝 bot_logs.txt # 📊 Conversation history
├── 📚 requirements.txt # Python dependencies
├── 📖 README.md # 📄 This file
├── 📄 LICENSE # ⚖️ MIT License
└── ⚙️ .gitignore # Git ignore rules