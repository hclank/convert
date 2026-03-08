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


@app.command()
def file(
    input_file: Path = typer.Argument(..., help="Path to the source file"),
    to: str = typer.Option(
        "mp4", "--to", "-t", help="Target extension (e.g., mp4, mkv, avi, mov)"
    ),
    output: Optional[Path] = typer.Option(
        None, "--out", "-o", help="Custom output filename"
    ),
):
    """Convert a single file to a new format."""
    if not input_file.exists():
        typer.secho(f"File {input_file} not found.", fg=typer.colors.RED)
        raise typer.Exit()

    # Ensure extension starts with a dot
    ext = to if to.startswith(".") else f".{to}"

    if not output:
        output = input_file.with_suffix(ext)

    run_ffmpeg_conversion(input_file, output)


@app.command()
def dir(
    folder: Path = typer.Argument(..., help="Directory to scan"),
    source_ext: str = typer.Option("avi", "--from", "-f", help="Extension to look for"),
    target_ext: str = typer.Option("mp4", "--to", "-t", help="Extension to convert to"),
):
    """Batch convert all files of a specific type in a directory."""
    if not folder.is_dir():
        typer.secho(f"Not a directory: {folder}", fg=typer.colors.RED)
        raise typer.Exit()

    # Clean up dots
    s_ext = f".{source_ext.lstrip('.')}"
    t_ext = f".{target_ext.lstrip('.')}"

    files = list(folder.glob(f"*{s_ext}"))

    if not files:
        typer.echo(f"No files found with extension {s_ext}")
        return

    typer.echo(f"📂 Found {len(files)} files. Starting batch...")
    for f in files:
        target = f.with_suffix(t_ext)
        run_ffmpeg_conversion(f, target)


if __name__ == "__main__":
    app()
