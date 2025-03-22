import whisper
import os
import queue
import sounddevice as sd
import numpy as np
import argparse
import re

# Load a smaller Whisper model for faster processing
model = whisper.load_model("tiny")


# Function to convert English to ASL grammar

def convert_to_asl_grammar(text):
    """Convert English text into ASL-friendly grammar by removing auxiliary verbs, articles, and restructuring sentences."""
    words = text.split()
    asl_keywords = [word for word in words if
                    word.lower() not in {"is", "am", "are", "was", "were", "the", "a", "an", "to", "of", "and", "be",
                                         "that", "this", "for", "with", "on", "at", "by"}]

    # Handling common ASL sentence structures (Topic-Comment, Subject-Verb-Object)
    if len(asl_keywords) > 2:
        subject = asl_keywords[0]
        verb = asl_keywords[1]
        object_phrase = " ".join(asl_keywords[2:])
        asl_sentence = f"{subject} {object_phrase} {verb}"  # Moving the verb to the end (ASL structure)
    else:
        asl_sentence = " ".join(asl_keywords)

    return asl_sentence.capitalize()

q = queue.Queue()

def callback(indata, frames, time, status):
    """Callback function to process real-time audio."""
    if status:
        print(status, flush=True)
    q.put(indata.copy())


def real_time_transcription():
    """Captures live audio and transcribes in real-time with lower latency."""
    samplerate = 16000  # Whisper works best with 16kHz audio
    blocksize = 1024  # Reduce block size for lower latency

    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback, blocksize=blocksize):
        print("Listening... Speak now!")
        while True:
            audio_data = q.get()
            audio_data = np.squeeze(audio_data)  # Convert to 1D array
            audio_data = audio_data.astype(np.float32)

            # Faster transcription with smaller chunk size
            result = model.transcribe(audio_data, language="en", fp16=False)

            asl_transcription = convert_to_asl_grammar(result["text"])
            print("ASL Grammar Output:", asl_transcription, flush=True)


def main():
    """Main function to handle real-time transcription with reduced latency."""
    global q
    q = queue.Queue()
    real_time_transcription()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-time speech-to-text transcription with ASL grammar conversion.")
    args = parser.parse_args()
    main()