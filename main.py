import ffmpeg
import typer
import os
from pathlib import Path
from typing import Optional

app = typer.Typer(
    help="A simple CLI tool to convert video files to any format using ffmpeg."
)


def run_ffmpeg_conversion(input_path: Path, output_path: Path):
    try:
        typer.echo(f"Converting {input_path} to {output_path}")
        stream = ffmpeg.input(str(input_path))
        stream = ffmpeg.output(
            stream,
            str(output_path),
            vcodec="libx264",
            acodec="aac",
            strict="experimental",
            loglevel="quiet",
        )
        ffmpeg.run(stream, overwrite_output=True)
        typer.secho(
            f"✅ Successfully converted to {output_path}", fg=typer.colors.GREEN
        )
    except ffmpeg.Error as e:
        typer.secho(f"❌ FFmpeg Error: {e.stderr.decode()}", fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"❌ Unexpected Error: {e}", fg=typer.colors.RED)
