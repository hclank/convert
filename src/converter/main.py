import ffmpeg
import typer
import os
from pathlib import Path
from typing import Optional

app = typer.Typer(
    help="A simple CLI tool to convert video files to any format using ffmpeg."
)


def run_ffmpeg_conversion(input_path: Path, output_path: Path, crf: int = 23):
    """Core logic with adjustable compression (CRF)."""
    try:
        typer.echo(f"⏳ Processing: {input_path.name} (CRF: {crf})...")

        (
            ffmpeg.input(str(input_path))
            .output(
                str(output_path),
                vcodec="libx264",
                acodec="aac",
                crf=crf,  # 0-51: 18 is high qual, 28 is high comp
                preset="medium",  # 'slower' = better compression, 'faster' = bigger file
                loglevel="error",
            )
            .run(overwrite_output=True)
        )
        typer.secho(f"✅ Finished: {output_path.name}", fg=typer.colors.GREEN)
    except ffmpeg.Error as e:
        typer.secho(f"❌ FFmpeg Error: {e}", fg=typer.colors.RED)


@app.command()
def file(
    input_file: Path = typer.Argument(..., help="Path to the source file"),
    to: str = typer.Option(
        "mp4", "--to", "-t", help="Target extension (e.g., mp4, mkv, avi, mov)"
    ),
    output: Optional[Path] = typer.Option(
        None, "--out", "-o", help="Custom output filename"
    ),
    compress: bool = typer.Option(
        False, "--compress", "-c", help="Enable high compression (CRF 28)"
    ),
    crf: Optional[int] = typer.Option(
        None, help="Manual CRF value (0-51). Override --compress"
    ),
):
    """Convert a single file to a new format."""
    if not input_file.exists():
        typer.secho(f"File {input_file} not found.", fg=typer.colors.RED)
        raise typer.Exit()

    # Ensure extension starts with a dot
    ext = to if to.startswith(".") else f".{to}"

    final_crf = 23  # Default
    if compress:
        final_crf = 28
    if crf is not None:
        final_crf = crf

    if not output:
        output = input_file.with_suffix(ext)

    run_ffmpeg_conversion(input_file, output, final_crf)


@app.command()
def dir(
    folder: Path = typer.Argument(..., help="Directory to scan"),
    from_ext: str = typer.Option("avi", "--from", "-f"),
    to_ext: str = typer.Option("mp4", "--to", "-t"),
    compress: bool = typer.Option(
        False, "--compress", "-c", help="Compress all files in batch"
    ),
):
    """Batch convert and compress an entire folder."""
    if not folder.is_dir():
        typer.secho(f"Not a directory: {folder}", fg=typer.colors.RED)
        raise typer.Exit()

    crf_val = 28 if compress else 23
    files = list(folder.glob(f"*.{from_ext.lstrip('.')}"))

    if not files:
        typer.echo("No matching files found.")
        return

    for f in files:
        target = f.with_suffix(f".{to_ext.lstrip('.')}")
        run_ffmpeg_conversion(f, target, crf=crf_val)


if __name__ == "__main__":
    app()
