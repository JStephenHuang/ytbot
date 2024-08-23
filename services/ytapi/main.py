import subprocess
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service


def convert_to_mp4(audio_file, image_file, output_file):
    # FFmpeg command to combine the image and audio into an MP4 video
    ffmpeg_command = [
        "ffmpeg",
        "-loop", "1",                   # Loop the image (required if the image is static)
        "-i", image_file,               # Input image file
        "-i", audio_file,               # Input audio file
        "-c:v", "libx264",              # Use H.264 video codec
        "-tune", "stillimage",          # Optimize for still image
        "-c:a", "aac",                  # Use AAC audio codec
        "-b:a", "192k",                 # Set audio bitrate
        "-pix_fmt", "yuv420p",          # Set pixel format
        "-shortest",                    # Stop encoding when the shortest input stream ends
        output_file
    ]

    # Run the FFmpeg command
    result = subprocess.run(ffmpeg_command, capture_output=True, text=True)

    # Print out the stdout and stderr for debugging
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

def create_yt_api_client():
    # Setting up the Youtube API
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    # SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    client_file = 'client-secret.json'
    return create_service(client_file, API_NAME, API_VERSION, SCOPES)

def upload_video(service, video_title, video_description, video_file):
    # Define the request body, which includes the video title, description, category, and tags, then uploading the video
    request_body = {
    'snippet': {
        'title': video_title,
        'description': video_description,
        'categoryId': '24', # 24 is the category id for entertainment
        'tags': ['insert', 'video', 'tags', 'here']
    },
    'status': {
        'privacyStatus': 'private',
        'selfDeclaredMadeForKids': False
    },
    'notifySubscribers': False
    }

    media_file = MediaFileUpload(video_file)
    # print(media_file.size() / pow(1024, 2), 'mb')
    # print(media_file.to_json())
    # print(media_file.mimetype())

    response_video_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()

    return response_video_upload.get('id')

def set_thumbnail(service, video_id, thumbnail_file):
   response_thumbnail_upload = service.thumbnails().set(
    videoId=uploaded_video_id,
    media_body=MediaFileUpload('thumbnail.png')
    ).execute()


if __name__ == "__main__":
    # Define the input files
    audio_file = "audio.mp3"
    image_file = "cat.jpg"
    output_file = "output_video.mp4"
    thumbnail_file = "thumbnail.jpg"

    # Convert the audio and image to a video
    convert_to_mp4(audio_file, image_file, output_file)
    print('Video created successfully')

    # Define the video title and description
    video_title = "my video title"
    video_description = "my video description"


    # Create a Youtube API client
    service = create_yt_api_client()

    # Upload video
    uploaded_video_id = upload_video(service, video_title, video_description, output_file)

    # Set thumbnail
    set_thumbnail(service, uploaded_video_id, thumbnail_file)

    

