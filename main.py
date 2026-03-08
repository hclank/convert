import ffmpeg
import click


@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}")


@click.command()
@click.option("--convert", help="Convert a video file to any format")
def convert_video(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, vcodec="libx264", acodec="aac").run()


if __name__ == "__main__":
    hello()
    convert_video()
