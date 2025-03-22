import whisper
import argparse
import os
from moviepy.editor import AudioFileClip


def extract_audio(video_path, audio_path):
    """Extracts audio from a video file."""
    video = AudioFileClip(video_path)
    video.write_audiofile(audio_path, codec='mp3')


def transcribe_audio(audio_path, model_type="base"):
    """Transcribes audio using OpenAI's Whisper model."""
    model = whisper.load_model(model_type)
    result = model.transcribe(audio_path)
    return result["text"]


def main(input_file):
    """Handles input files (audio or video) and transcribes them."""
    file_extension = os.path.splitext(input_file)[-1].lower()

    if file_extension in [".mp4", ".mov", ".avi", ".mkv"]:
        audio_path = "temp_audio.mp3"
        extract_audio(input_file, audio_path)
    else:
        audio_path = input_file

    transcribed_text = transcribe_audio(audio_path)
    print("Transcription:", transcribed_text)

    if os.path.exists("temp_audio.mp3"):
        os.remove("temp_audio.mp3")

    return transcribed_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe speech from audio or video files.")
    parser.add_argument("input_file", type=str, help="Path to the audio or video file.")
    args = parser.parse_args()

    main(args.input_file)
