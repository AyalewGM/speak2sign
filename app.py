from flask import Flask, render_template, request, jsonify
import whisper
import os
import queue
import sounddevice as sd
import vosk
import json
from modules.asl_processor import convert_to_asl_grammar

app = Flask(__name__)

# Load Whisper model for file upload transcription
model = whisper.load_model("tiny")

# Vosk ASR Model (For Real-Time Transcription)
vosk_model = vosk.Model("vosk-model-small-en-us-0.15")
audio_queue = queue.Queue()

# Microphone Input Callback
def audio_callback(indata, frames, time, status):
    """Captures live audio and sends to queue"""
    if status:
        print(status, flush=True)
    audio_queue.put(bytes(indata))

@app.route("/")
def index():
    """Render the frontend page."""
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    """Handle file upload, transcribe, and return ASL words."""
    file = request.files["audio"]
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Transcribe using Whisper
    result = model.transcribe(file_path)
    text = result["text"]

    # Convert to ASL grammar
    asl_text = convert_to_asl_grammar(text)
    asl_words = asl_text.split()

    return jsonify({"text": text, "asl_words": asl_words})

@app.route("/real_time_transcription", methods=["GET"])
def real_time_transcription():
    """Real-time transcription using Vosk"""
    samplerate = 16000  # Required sample rate for Vosk
    recognizer = vosk.KaldiRecognizer(vosk_model, samplerate)

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None, dtype="int16",
                           channels=1, callback=audio_callback):
        print("🎤 Listening... Speak Now!")

        while True:
            if not audio_queue.empty():
                audio_data = audio_queue.get()
                if recognizer.AcceptWaveform(audio_data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "")

                    if text:
                        asl_text = convert_to_asl_grammar(text)
                        asl_words = asl_text.split()
                        return jsonify({"text": text, "asl_words": asl_words})

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
