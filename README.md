# 🔊 Text-to-Speech Converter

> A simple Python project that converts text from a `.txt` file into speech using Microsoft's **Edge TTS** engine, with a British English voice and MP3 output.

<div align="center">

### 🔊 Text-to-Speech

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Edge TTS](https://img.shields.io/badge/Edge--TTS-Text%20to%20Speech-0078D4?style=for-the-badge&logo=microsoftedge&logoColor=white)](https://github.com/rany2/edge-tts)

</div>

---

## ✨ Overview

**Text-to-Speech Converter** is a Python project that converts written text into spoken audio using Microsoft's **Edge TTS** engine.

The application reads text from a `.txt` file, processes it using a **British English voice**, and saves the generated speech as an MP3 file.

---

## 🚀 Features

- 📄 Reads text from a `.txt` file
- 🗣️ Converts text into speech
- 🇬🇧 Uses a British English voice
- 🔊 Generates high-quality speech
- 🎵 Saves the output as an MP3 file
- ▶️ Automatically plays the generated audio
- 💻 Simple Python implementation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Edge-TTS** | Text-to-speech conversion |
| **Asyncio** | Handles asynchronous operations |
| **OS Module** | Plays the generated audio file |

---

## 🧠 Python Concepts Practiced

This project helped me practice:

- File handling
- Reading `.txt` files
- UTF-8 encoding
- Functions
- Asynchronous programming
- `async` / `await`
- External Python libraries
- `asyncio.run()`
- Using the `os` module
- Saving generated files

---

## 🔄 How It Works

```text
📄 sample.txt
      ↓
📖 Read Text
      ↓
🗣️ Edge TTS
      ↓
🇬🇧 British English Voice
      ↓
🎵 sample.mp3
      ↓
▶️ Play Audio
