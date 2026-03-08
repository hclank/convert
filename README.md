🎥 Universal Converter CLIA fast, lightweight, and dead-simple Command Line Interface (CLI) for converting any media file to another format. Powered by Python, Typer, and FFmpeg.🚀 FeaturesUniversal Support: Convert video, audio, and images (anything FFmpeg handles).Batch Processing: Convert entire directories with a single command.Smart Defaults: Optimized for high-quality H.264 video and AAC audio.Dependency Check: Automatically ensures FFmpeg is doing the heavy lifting.📦 Installation1. Prerequisite: Install FFmpegThis tool requires FFmpeg to be installed on your system.macOS: brew install ffmpegLinux: sudo apt install ffmpegWindows: Download from ffmpeg.org2. Install the CLIOnce you have published this to PyPI, users can install it via:pip install universal-converter-cli
🛠 UsageThe CLI provides two main commands: file (for single items) and dir (for batch processing).1. Convert a Single FileBy default, it converts to .mp4 unless specified.# Basic conversion (AVI to MP4)
convert file video.avi

# Convert to a specific format

convert file video.mov --to mkv

# Convert with a custom output name

convert file input.wav --out song.mp3 2. Batch Convert a DirectoryScan an entire folder for a specific extension and convert them all.# Convert all .avi files in the current folder to .mp4
convert dir ./my_videos --from avi --to mp4

# Convert all .wav files to .mp3

convert dir ./music --from wav --to mp3
⌨️ Command ReferenceCommandArgumentOptionDescriptionfileINPUT_PATH--to, -tTarget extension (default: mp4)fileINPUT_PATH--out, -oCustom output filenamedirPATH--from, -fSource extension to look fordirPATH--to, -tTarget extension to convert to🛠 DevelopmentTo run the project locally for development:Clone the repo:git clone https://github.com/your-username/universal-converter.git
cd universal-converter
Install in editable mode:pip install -e .
Run the tool:convert --help
