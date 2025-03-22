import os
import ffmpeg

# Ensure the output directory exists
os.makedirs("../static/asl_animations", exist_ok=True)

def convert_video_to_gif(video_path, output_gif):
    """Convert a video file to a GIF using ffmpeg."""
    output_path = os.path.join("../static/asl_animations", output_gif)

    (
        ffmpeg
        .input(video_path)
        .filter("fps", fps=15)
        .filter("scale", 200, -1)  # Adjust size
        .output(output_path, loop=0, pix_fmt="rgb8")
        .run(overwrite_output=True)
    )
    print(f"Converted {video_path} to {output_path}")

def process_asl_videos(video_folder):
    """Find all ASL videos in the folder and convert them to GIFs."""
    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4") or filename.endswith(".mov"):
            word = os.path.splitext(filename)[0]  # Use filename as word
            convert_video_to_gif(os.path.join(video_folder, filename), f"{word}.gif")

if __name__ == "__main__":
    process_asl_videos("C:\\Users\\ayalew.mersha\\Downloads\data1")
