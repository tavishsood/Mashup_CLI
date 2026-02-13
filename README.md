# 🎵 Mashup CLI Tool

A dedicated command-line utility that automates the creation of audio mashups. It scrapes YouTube for a specific artist, downloads their top tracks, extracts a specific segment from each, and merges them into a single audio file.

## ⚙️ Prerequisites
Ensure you have the following installed on your system:
* **Python 3.x**
* **FFmpeg** (Must be added to your system PATH)

## 📥 Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/mashup-cli.git](https://github.com/your-username/mashup-cli.git)
    cd mashup-cli
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Execute the script from the terminal using the argument structure defined in the assignment

```bash
python <RollNumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

```

### Parameters

* **SingerName:** Name of the artist. Use quotes if the name has spaces (e.g., "Sharry Maan"). 


* **NumberOfVideos:** Total songs to include in the mashup. **Must be > 10**. 


* **AudioDuration:** Length of the clip to cut from the start of each song (in seconds). **Must be > 20**. 


* 
**OutputFileName:** The name of the final output file (e.g., `output.mp3`). 



### Example Run

```bash
python 102303246.py "Sharry Maan" 20 30 output.mp3

```

*This command downloads 20 songs by Sharry Maan, trims the first 30 seconds of each, and saves the result as `output.mp3`.*

```

```
