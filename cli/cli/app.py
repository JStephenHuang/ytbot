

import torch
import typer
import logging
from .llama3 import Llama3
from .tts import TTSSingleton
from .stable_diffusion import StableDiffusionSingleton


app = typer.Typer()
logger = logging.getLogger(__name__)

def single_line(multi_line: str):
    _, remaining_str = multi_line.split("\n", 1)
    return remaining_str.replace("\n", " ")

@app.command("run")
def generate_media():
    story = typer.prompt("story", type=str)
    llama3 = Llama3()

    summary_result = llama3.get_summary(story)
    short_narration_result = llama3.get_short_narration(story)
    image_description_result = llama3.get_image_description(story)
    thumbnail_description_result = llama3.get_thumbnail_description(story)

    summary = single_line(summary_result["value"])
    short_narration = single_line(short_narration_result["value"])
    image_description = single_line(image_description_result["value"])
    thumbnail_description = single_line(thumbnail_description_result["value"]
)
    if summary_result["status"] == "rejected":
        logger.debug(f"Summary generation failed: {summary}")
        return
    
    if short_narration_result["status"] == "rejected":
        logger.debug(f"Thumbnail description generation failed: {short_narration}")
        return
    
    if image_description_result["status"] == "rejected":
        logger.debug(f"Thumbnail description generation failed: {image_description}")
        return

    if thumbnail_description_result["status"] == "rejected":
        logger.debug(f"Thumbnail description generation failed: {thumbnail_description}")
        return

    print(f"\nSummary: {summary}\nNarration: {short_narration}\nImage Description: {image_description}\nThumbnail: {thumbnail_description}")

    tts(short_narration)
    tti(image_description)


@app.command()
def llama3():
    while True:
        prompt = typer.prompt("prompt", type=str)
        llama3 = Llama3()

        result = llama3.get_thumbnail_description(prompt)
        print(result["value"].splitlines())

@app.command()
def tts(text: str):
    # text = typer.prompt("text", type=str)

    model = TTSSingleton(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

    model.tts_to_file(text=text, speaker_wav="assets/speakers/brian2.wav", language="en", file_path="outputs/output.wav")

@app.command()
def tti(text: str):
    # text = typer.prompt("text", type=str)

    model = StableDiffusionSingleton()

    image = model(text).images[0]
    image.save("outputs/output.png")


@app.callback()
def callback(verbose: bool = False):
    logging.basicConfig()

    if verbose:
        logger.setLevel(logging.DEBUG)

# app.add_typer(member.app, name="member")