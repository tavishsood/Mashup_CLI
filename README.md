
# Mashup Generator: CLI Tool

A robust command-line utility designed to automate the creation of audio mashups. This tool scrapes YouTube for a specified artist, downloads their top tracks, extracts a precise audio segment from each, and merges them into a seamless continuous mix.

## Methodology
The application executes a linear data processing pipeline designed for efficiency and strict constraint adherence:

1.  **Input Validation & Parsing:**
    * The script first parses command-line arguments using `sys.argv`.
    * **Constraint Check:** It checks for the correct number of arguments (4) and validates that $N$ (No. of Videos) > 10 and $Y$ (Duration) > 20 seconds. If constraints are violated, the program terminates immediately with an error message.

2.  **YouTube Scraping & Extraction:**
    * Utilizing **`yt-dlp`**, the script performs a search query for the specified "Artist Name".
    * It extracts the metadata (URLs) for the top $N$ results, filtering out playlists or non-video entries to ensure quality.

3.  **Audio Down-sampling:**
    * To optimize bandwidth, the tool downloads **audio-only streams** (m4a/webm) rather than full video files.
    * These streams are immediately converted to a consistent format (`.mp3` or `.wav`) using **FFmpeg**, ensuring compatibility for the merging phase.

4.  **Temporal Trimming (Signal Processing):**
    * The system iterates through the downloaded tracks and applies a strict time-based cut.
    * **Logic:** `ffmpeg -ss 0 -t <Duration> -i input.mp3 output_trimmed.mp3`
    * This extracts exactly the first $Y$ seconds from the start of each track.

5.  **Concatenation & Normalization:**
    * The trimmed clips are merged into a single continuous audio stream.
    * The final output is saved locally with the user-defined filename.

## Prerequisites
* **Python 3.x**
* **FFmpeg** (Critical: Must be installed and added to System PATH)
* **Libraries:** `yt-dlp`, `pydub` (or `moviepy`)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/tavishsood/mashup_cli.git
    cd mashup_cli
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Execute the script using the strict argument structure defined in the assignment:

```bash
python 102303246.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

```

### Parameters

* **SingerName:** Name of the artist (e.g., "The Weeknd"). Use quotes for multi-word names.
* **NumberOfVideos:** Total songs to scrape. **Must be > 10**.
* **AudioDuration:** Seconds to cut from the start of each song. **Must be > 20**.
* **OutputFileName:** The destination filename (e.g., `mashup.mp3`).

### Example Run

```bash
python 102303246.py "Sharry Maan" 20 30 output.mp3
