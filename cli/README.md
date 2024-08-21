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
