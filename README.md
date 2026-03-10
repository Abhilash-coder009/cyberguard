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

# 📋 Overview

**CyberGuard** is a privacy-focused cybersecurity assistant that runs entirely on your local machine. It answers questions about phishing, ransomware, passwords, and online safety using a knowledge base stored in simple text files.

All processing happens locally — **your questions never leave your computer**.

---

# ✨ Features

| Feature                       | Description                                                       |
| ----------------------------- | ----------------------------------------------------------------- |
| 🔒 **100% Private**           | Everything runs on your computer — no data leaves your machine    |
| 📚 **Knowledge Base**         | All information stored in easy-to-edit text files                 |
| 🎯 **Cybersecurity Focus**    | Specializes in phishing, ransomware, passwords, and online safety |
| 💬 **Natural Conversation**   | Handles greetings, questions, and casual chat                     |
| 🚀 **Fast & Lightweight**     | Optimized for CPU using `llama3.2:1b` model                       |
| 🛠️ **Customizable**          | Add your own knowledge by simply adding text files                |
| 📝 **Conversation Logs**      | All chats saved to `bot_logs.txt`                                 |
| 👨‍💻 **Created by Abhilash** | Developed by a cybersecurity enthusiast                           |

---

# 📁 Project Structure

```
cyberguard/

├── cybersecurity_docs/           # 📚 ALL KNOWLEDGE FILES
│   ├── greetings.txt             # Greetings & casual responses
│   ├── creator_info.txt          # Bot identity & creator info
│   ├── phishing.txt              # Phishing information
│   ├── ransomware_complete.txt   # Ransomware guide
│   ├── internet_attacks.txt      # DDoS, MITM etc
│   ├── password_policy.txt       # Password security
│   └── more_topic_files.txt

├── chatbot.py                    # 🧠 MAIN BOT CODE
├── bot_logs.txt                  # 📊 Conversation history
├── requirements.txt              # 📚 Python dependencies
├── README.md                     # 📄 Documentation
├── LICENSE                       # ⚖️ MIT License
└── .gitignore                    # ⚙️ Git ignore rules
```

---

# ⚙️ Installation

## Prerequisites

Install the following software before running CyberGuard.

• **Python 3.9 or higher**
https://www.python.org/downloads/

• **Ollama**
https://ollama.com/download/windows

• **Minimum 8GB RAM (16GB recommended)**

---

# 📦 Install Ollama Models

After installing Ollama run:

```
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

---

# 🧪 Set Up Python Environment

### Create Virtual Environment

```
python -m venv venv
```

### Activate Environment

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

---

# 📚 Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Run CyberGuard

Start the chatbot using:

```
python chatbot.py
```

---

# 💬 Usage Example

```
You: hi
CyberGuard: Hello! I'm CyberGuard, your cybersecurity assistant. How can I help you today?

You: what is phishing?
CyberGuard: Phishing is when attackers send fake emails to trick you into revealing information.

You: who created you?
CyberGuard: I was created by Abhilash!

You: good night
CyberGuard: Good night! Sleep well. Stay safe online!

You: exit
CyberGuard: Goodbye! Stay safe online! 👋
```

---

# 🛠️ Customizing Knowledge

CyberGuard uses simple **text files as its knowledge base**.

You can add more cybersecurity information by placing new files inside:

```
cybersecurity_docs/
```

Example:

```
malware.txt
network_security.txt
social_engineering.txt
web_security.txt
```

The chatbot will automatically use them to answer questions.

---

# 📝 Conversation Logs

Every chat is automatically stored in:

```
bot_logs.txt
```

This allows you to review conversation history later.

---

# ⚖️ License

This project is licensed under the **MIT License**.

See the full license here: [LICENSE](LICENSE)

You are free to use, modify, and distribute this project.


---

# 👨‍💻 Author

**Abhilash** — *Developer & Cybersecurity Enthusiast*

🔗 **GitHub:** [@Abhilash-coder009](https://github.com/Abhilash-coder009)

📦 **Project:** **CyberGuard**

---

🛡️ **Stay Safe Online!**
Created with ❤️ by **Abhilash**

# ⭐ Support

If you like this project, consider giving it a **⭐ star on GitHub**.

🛡️ **Stay Safe Online!**
Created with ❤️ by **Abhilash**