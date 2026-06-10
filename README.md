# B-mo: Multimodal AI Assistant

This repository is an adapted application of the original project [AsistRCoral](https://github.com/AleRubin/AsistRCoral) created by AleRubin. 

While the original framework was designed specifically for the Google Coral Edge TPU, this version has been completely refactored and optimized to run natively on a **Raspberry Pi 5**. 

### Key Differences & Upgrades in this Fork:
* **Vision Acceleration:** Migrated from Google Coral (`pycoral`/`tflite`) to the **Hailo-8L AI Accelerator** using the official `hailo-all` toolchain and GStreamer pipelines.
* **Language Engine:** Integrated with **Ollama** running locally on the Raspberry Pi's CPU, utilizing models like Gemma 4 for fast and private natural language processing.
* **Audio & Wake Word:** Custom audio pipeline implementing `openwakeword` and `sounddevice` for hands-free interactions without relying on cloud services.

## Acknowledgment
Special thanks to [AleRubin](https://github.com/AleRubin) for the original open-source logic and architecture, which served as the foundation for B-mo's development.
