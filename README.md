**Speak2Sign** is an AI-powered system that translates **spoken English** into **American Sign Language (ASL)** grammar using a combination of **speech recognition** and **natural language processing**.

It supports:
- 🗣️ **Real-time transcription** using Whisper or Vosk
- 🎤 **Audio or video file uploads**
- 🧠 **ASL grammar conversion** via a fine-tuned Flan-T5 transformer model
- 🖼️ **Animated sign visualization** using pre-generated ASL GIFs

---

## 🚀 Features

- 🔊 Live or recorded audio input
- ✍️ Converts English into ASL gloss (grammar)
- 🤖 Fine-tuned Flan-T5 model for grammar transformation
- 🎞️ Visual sign animation (GIF-based, easily extendable)
- 🌐 Clean web UI (Bootstrap + Flask)
- ⚡ GPU-supported training & inference

---

## 🧠 How It Works

1. **Speech Transcription**: Converts live or uploaded audio into English using Whisper/Vosk.
2. **ASL Grammar Converter**: Translates English to ASL grammar using a fine-tuned Flan-T5 model.
3. **Animation Display**: Displays word-by-word ASL sign GIFs in the web interface.

---

## 📁 Project Structure

```
speak2sign/
├── training/                   # Fine-tuning script for Flan-T5
├── inference/                 # Inference pipeline and model comparison
├── data/                      # ASL dataset (from ASLG-PC12 or custom)
├── scripts/                   # Dataset scraping and formatting
├── bart_model/                # Your previous BART-based pipeline
├── models/asl_flan_t5/        # Saved fine-tuned model
├── static/asl_animations/     # ASL GIFs
├── templates/index.html       # Bootstrap frontend
├── app.py                     # Flask app for UI + API
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

### ✅ Prerequisites

- Python 3.8+
- pip
- Optional: CUDA-compatible GPU

---

### 📦 Set up environment

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/speak2sign.git
cd speak2sign

# 2. Create virtual environment (optional but recommended)
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

### 🔡 Download and Prepare the Dataset

```bash
python scripts/prepare_aslg_pc12.py
```
This script will:
- Download the ASLG-PC12 dataset
- Format it into `data/asl_data.csv`

---

### 🧠 Fine-tune the Flan-T5 Model

```bash
python training/train_flan_t5_asl.py
```
The model will be saved to `models/asl_flan_t5/`

---

### 🧪 Run Side-by-Side Comparison (BART vs Flan-T5)

```bash
python inference/compare_models.py
```

---

### 🌐 Run the Web App

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🖼️ ASL GIFs

- Save your ASL sign animations (e.g., `hello.gif`, `thank_you.gif`) in:
```
static/asl_animations/
```
- Filenames must match the ASL gloss words in your model output.

---

## 🧪 Example Inputs/Outputs

| English (Input)             | ASL Gloss Output         |
|-----------------------------|--------------------------|
| What is your name?          | YOUR NAME WHAT           |
| I am going to the store.    | I GO STORE               |
| Can you help me?            | YOU HELP ME CAN          |

---

## 🛠️ Tech Stack

- 🤖 Transformers: `google/flan-t5-base`
- 🔊 Whisper / Vosk for audio transcription
- 🧪 Hugging Face Datasets + Trainer
- 🖥️ Flask + Bootstrap frontend
- ⚙️ Torch, SentencePiece, Pandas

---

## 🙌 Acknowledgements

- [ASLG-PC12 Dataset](https://achrafothman.net)
- [Flan-T5 Model (Google)](https://huggingface.co/google/flan-t5-base)
- [Whisper Speech-to-Text (OpenAI)](https://github.com/openai/whisper)

---

## 📜 License

This project is MIT licensed. Please credit datasets and models used in your own deployments.

---

## 💬 Questions or Contributions?

Feel free to open an issue or PR. Contributions are welcome!
