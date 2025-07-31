# 💬 Multi-Client Chat Server

A lightweight Python-based chat server that supports real-time messaging between multiple clients using sockets and threading. Great for learning networking, concurrency, and building your own mini Slack!

## 🚀 Features
- 🧑‍🤝‍🧑 Real-time group chat
- 🧵 Handles multiple clients concurrently (via `threading`)
- 💻 Simple command-line interface
- 🔄 Basic error handling & easy to extend

## 🛠️ Tech Stack
- Python 3 🐍
- Sockets & TCP/IP 🔌
- Python `threading` module 🧵

## 🗂️ Project Structure
multi-client-chat-server/
├── server.py # Server script
├── client.py # Client script
└── README.md # You're here!

##System Architecture 
+--------+                    +--------+
| Client | <----------------> |        |
+--------+                    |        |
                              | Server |
+--------+                    |        |
| Client | <----------------> |        |
+--------+                    +--------+


##STEPS

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/multi-client-chat-server.git
   cd multi-client-chat-server
   
2. **Run the server**
   ```bash
   python server.py

3. **Run clients in new terminals**
   ```bash
   python client.py

##EXAMPLE 
Terminal 1 (Server):
$ python server.py
[LISTENING] Server is running on 127.0.0.1:12345

Terminal 2 (Client 1):
$ python client.py
Enter name: Alice
Hello everyone!

Terminal 3 (Client 2):
$ python client.py
Enter name: Bob
Hi Alice!





