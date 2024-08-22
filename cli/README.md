# Installation

```
poetry install
```

# Usage

```
poetry run cli
```

# Gameplan

    # Scrape reddit for a thread
    # Prompt type of thread: duration (# words), topic ...
    # Return an object {date: Date, title: str, content: str, src: str}

    # Pass content it through a LLM
    # Return a piece of text {summary: str}

    # Pass summary through model that generates an image
    # Returns a blob or image url

    # Pass the text or content to a text-to-speech model
    # Returns an audio blob/file

    # Use FFmpeg to merge the audio and the image together
    # Returns a video file

    # Use Youtube Data API to upload the video

# AI Model Setup

Check your NVIDIA CUDA version by running `nvcc --version` in your terminal. 
If no verison is found, download the latest cuda version that pytorch offers, at the time I am writing this, pytorch latest CUDA Version is 12.4.

Follow:
https://pytorch.org/ 

AI Model Requirements:
TTS => https://github.com/coqui-ai/TTS/blob/dev/requirements.txt
Stable Diffusion => ?

Do not stress yourself over this.
