# 🎥 Universal Media Converter CLI

A fast, lightweight, and dead-simple Command Line Interface (CLI) for converting any media file to another format. Powered by **Python**, **Typer**, and **FFmpeg**.

## 🚀 Features

- **Universal Support:** Convert video, audio, and images (anything FFmpeg handles).
- **Batch Processing:** Convert entire directories with a single command.
- **Smart Defaults:** Optimized for high-quality H.264 video and AAC audio.
- **Dependency Check:** Automatically ensures FFmpeg is doing the heavy lifting.

---

## 📦 Installation

### 1. Prerequisite: Install FFmpeg

This tool requires FFmpeg to be installed on your system.

- **macOS:** `brew install ffmpeg`
- **Linux:** `sudo apt install ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### 2. Install the CLI

Once you have published this to PyPI, users can install it via:

```bash
pip install universal-converter-cli
```

````

---

## 🛠 Usage

The CLI provides two main commands: `file` (for single items) and `dir` (for batch processing).

### 1. Convert a Single File

By default, it converts to `.mp4` unless specified.

```bash
# Basic conversion (AVI to MP4)
convert file video.avi

# Convert to a specific format
convert file video.mov --to mkv

# Convert with a custom output name
convert file input.wav --out song.mp3

```

### 2. Batch Convert a Directory

Scan an entire folder for a specific extension and convert them all.

```bash
# Convert all .avi files in the current folder to .mp4
convert dir ./my_videos --from avi --to mp4

# Convert all .wav files to .mp3
convert dir ./music --from wav --to mp3

```

---

## ⌨️ Command Reference

| Command | Argument     | Option         | Description                     |
| ------- | ------------ | -------------- | ------------------------------- |
| `file`  | `INPUT_PATH` | `--to`, `-t`   | Target extension (default: mp4) |
| `file`  | `INPUT_PATH` | `--out`, `-o`  | Custom output filename          |
| `dir`   | `PATH`       | `--from`, `-f` | Source extension to look for    |
| `dir`   | `PATH`       | `--to`, `-t`   | Target extension to convert to  |

---

## 🛠 Development

To run the project locally for development:

1. **Clone the repo:**

```bash
git clone [https://github.com/your-username/universal-converter.git](https://github.com/your-username/universal-converter.git)
cd universal-converter

```

2. **Install in editable mode:**

```bash
pip install -e .

```

3. **Run the tool:**

```bash
convert --help

```

---

## 📜 License

Distributed under the MIT License.


````
