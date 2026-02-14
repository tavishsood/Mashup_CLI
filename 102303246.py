import os
import sys
import subprocess
from yt_dlp import YoutubeDL


def download_videos(search_query, n, out_dir):
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": f"{out_dir}/%(title)s.%(ext)s",
        "noplaylist": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"scsearch{n}:{search_query}"])


def trim_audio(input_path, output_path, seconds):
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-t",
        str(seconds),
        "-vn",
        "-acodec",
        "mp3",
        output_path,
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def convert_to_mp3(initial_path, output_path):
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        initial_path,
        "-vn",
        "-acodec",
        "mp3",
        output_path,
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    if len(sys.argv) < 5:
        print('Usage: python script.py "search query" N duration output_file_name')
        sys.exit(1)

    search_query = sys.argv[1]
    n = int(sys.argv[2])
    # if n < 1:
    if n < 11:
        print("N must be greater than 10.")
        sys.exit(1)
    duration = int(sys.argv[3])
    output_file_name = sys.argv[4]

    if duration < 21:
        print("Duration must be greater than 20 seconds.")
        sys.exit(1)

    base_dir = "output"
    video_dir = os.path.join(base_dir, "videos")
    audio_dir = os.path.join(base_dir, "audio")

    os.makedirs(video_dir, exist_ok=True)

    download_videos(search_query, n, video_dir)
    # video: opus3, .ogg files

    os.makedirs(audio_dir, exist_ok=True)
    for file in os.listdir(video_dir):
        if file.lower().endswith(
            (
                ".opus",
                ".ogg",
            )
        ):
            input_path = os.path.join(video_dir, file)
            output_path = os.path.join(audio_dir, f"{os.path.splitext(file)[0]}.mp3")
            convert_to_mp3(input_path, output_path)
            trim_audio(output_path, output_path, duration)
        elif file.lower().endswith(".mp3"):
            input_path = os.path.join(video_dir, file)
            output_path = os.path.join(audio_dir, file)
            trim_audio(input_path, output_path, duration)
    trimmed_files = [f for f in os.listdir(audio_dir) if f.lower().endswith(".mp3")]
    if not trimmed_files:
        print("No audio files were created.")
        sys.exit(1)
    # merge all mp3 files into one
    merged_path = os.path.join(audio_dir, output_file_name)
    print("Merging audio files...")
    with open(merged_path, "wb") as merged_file:
        for file in trimmed_files:
            with open(os.path.join(audio_dir, file), "rb") as f:
                merged_file.write(f.read())
    print(f"Final merged audio saved to: {merged_path}")


if __name__ == "__main__":
    main()
