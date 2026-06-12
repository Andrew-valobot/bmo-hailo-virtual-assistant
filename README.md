# Be More Agent 🤖 (Hailo-8L Edition)
**A Customizable, Offline-First AI Agent for Raspberry Pi 5**

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%205-red) ![Hardware](https://img.shields.io/badge/Hardware-Hailo--8L-orange) ![License](https://img.shields.io/badge/License-MIT-green)

This project turns a Raspberry Pi 5 into a fully functional, multimodal conversational AI agent. Unlike cloud-based assistants, this agent runs **100% locally** on your device. 

**This is a heavy-duty fork** of the original [Be More Agent](https://github.com/brenpoly/be-more-agent). While the original used CPU-based vision, this repository has been completely refactored to utilize the **Hailo-8L PCIe AI Accelerator** for real-time computer vision, alongside local LLM processing via Ollama.

## ✨ Features & Upgrades

* **100% Local Intelligence**: Powered by **Ollama** running `gemma2:2b` and **Whisper.cpp** (Speech-to-Text). No API fees, completely private.
* **Hardware-Accelerated Vision**: Replaced CPU vision models with **Hailo-8L** GStreamer pipelines (`yolov8` and `yolov5_personface`) for 30 FPS real-time object and person detection without taxing the main CPU.
* **Open Source Wake Word**: Wakes up to custom models using **OpenWakeWord** (Offline & Free).
* **Smart Web Search**: Uses DuckDuckGo to find real-time news when the LLM needs internet context.
* **Reactive Faces**: GUI updates the character's face based on its state (Listening, Thinking, Speaking, Idle).
* **Fast Text-to-Speech**: Uses **Piper TTS** for low-latency voice generation.

## 🛠️ Hardware Requirements

* **Raspberry Pi 5** (4GB or 8GB RAM)
* **Raspberry Pi Active Cooler** (Critical for Ollama thermal management)
* **Hailo-8L AI Accelerator** (connected via PCIe M.2 HAT)
* Official Raspberry Pi Camera Module (CSI cable)
* USB Microphone & Speaker
* LCD Screen (DSI or HDMI)

---

## 🚀 Installation

### 1. Prerequisites & Hailo Setup
Ensure your Raspberry Pi OS (Debian Trixie/Bookworm) is up to date and the Hailo software suite is installed:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install hailo-all git -y


```
### 2. Install Miniforge (Conda)
To prevent Python environment conflicts on the Pi5

```bash
wget [https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh)
bash Miniforge3-Linux-aarch64.sh

```

### 3. Install Ollama & Models

```bash
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
ollama pull gemma2:2b

```

### 4. Clone & Setup Environment

```bash
git clone [https://github.com/YOUR_USERNAME/bmo-hailo-assistant.git](https://github.com/YOUR_USERNAME/bmo-hailo-assistant.git)
cd bmo-hailo-assistant

# Create and activate the conda environment
conda create -n bmo_env python=3.11 -y
conda activate bmo_env

# Install dependencies
pip install -r requirements.txt

```

### 5. Configure the Wake Word
  1- Download the default "Hey Jarvis" model (or train your own at OpenWakeWord).
  2- Place the .onnx file in the root folder and rename it to wakeword.onnx.

### 6. Run the Agent
```bash
conda activate bmo_env
python main.py

```
