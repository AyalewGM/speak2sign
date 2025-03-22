# Speak2Sign

**Speak2Sign** is an AI-powered application that translates live speech or uploaded audio/video into American Sign Language (ASL) in real time. It converts spoken English into grammatically correct ASL (in gloss format) and plays animated sign language visuals word-by-word, allowing deaf or hard-of-hearing users to follow conversations or media in real time.

---

## What the Program Does

- Transcribes live speech through a microphone or processes uploaded audio/video files.
- Uses advanced speech recognition models (Whisper or Vosk) to convert speech to English.
- Translates English into ASL grammar using a fine-tuned Flan-T5 transformer model.
- Displays ASL word-by-word as animations using a collection of GIFs.
- Provides an accessible visual communication tool for following spoken content.

This project is especially useful for:
- Real-time ASL interpretation during conversations or presentations.
- Assisting with accessibility in digital content.
- Building educational tools for ASL learners or interpreters.

---

## Example Use Case

Imagine a deaf student attending a live lecture. Speak2Sign listens to the instructor, transcribes their speech, converts it to ASL grammar, and plays sign animations in real time—helping the student follow the class without needing a live interpreter.

---

## Features

- Live or recorded audio input
- Converts English into ASL gloss (grammar)
- Fine-tuned Flan-T5 model for grammar transformation
- Visual sign animation (GIF-based, easily extendable)
- Clean web UI (Bootstrap + Flask)
- GPU-supported training and inference

---

## How It Works

1. Speech Transcription: Converts live or uploaded audio into English using Whisper or Vosk.
2. ASL Grammar Conversion: Translates English to ASL grammar using a fine-tuned Flan-T5 model.
3. Animation Display: Displays word-by-word ASL sign GIFs in the web interface.

---

## Installation

### Prerequisites

- Python 3.8+
- pip
- Optional: CUDA-compatible GPU

---

### Set Up Environment

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/speak2sign.git
cd speak2sign

# Create virtual environment (optional)
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### Download and Prepare the Dataset

```bash
python scripts/prepare_aslg_pc12.py
```

This script will:
- Download the ASLG-PC12 dataset
- Format it into `data/asl_data.csv`

---

### Fine-Tune the Flan-T5 Model

```bash
python training/train_flan_t5_asl.py
```

The model will be saved to `models/asl_flan_t5/`

---

### Compare with BART

```bash
python inference/compare_models.py
```

---

### Run the Web App

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ASL GIFs

- Save your ASL sign animations (e.g., `hello.gif`, `thank_you.gif`) in:
```
static/asl_animations/
```

Filenames must match the ASL gloss words in your model output.

---

## Acknowledgements

- ASLG-PC12 Dataset: https://achrafothman.net
- Flan-T5 Model (Google): https://huggingface.co/google/flan-t5-base
- Whisper (OpenAI): https://github.com/openai/whisper

---

## License

This project is MIT licensed. Please credit datasets and models used in your own deployments.

---

## Questions or Contributions?

Feel free to open an issue or pull request. Contributions are welcome!
