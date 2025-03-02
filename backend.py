"""from pytube import YouTube

def download_youtube_video(url, save_path="."):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Downloading '{yt.title}'...")
        video_stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    save_location = input("Enter the directory to save the video (or press Enter for current directory): ")
    download_youtube_video(youtube_url, save_path=save_location if save_location else ".")
    """



"""
from pytube import YouTube

url = input("Enter the YouTube video URL: ")
YouTube(url).streams.get_highest_resolution().download()
print("Video downloaded successfully!")
"""


"""
import yt_dlp

def download_highest_resolution(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Ensures highest resolution with audio
        'outtmpl': '%(title)s.%(ext)s'        # Save the file with the video title
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Video downloaded successfully!")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_highest_resolution(video_url)
"""


"""This tool often works better in cases where `pytube` faces issues like the 403 error."""

"""
from pytube import YouTube

def download_video(url):
       yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)  # Enable OAuth if needed
       stream = yt.streams.get_highest_resolution()
       stream.download()
       print("Video downloaded successfully!")

url = input("Enter the YouTube video URL: ")
download_video(url)"""


"""
import yt_dlp

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Highest resolution with audio
        'merge_output_format': 'mp4',         # Ensures output file is in MP4 format
        'outtmpl': '%(title)s.%(ext)s',       # Save the file with the video title as the filename
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
"""

"""
import yt_dlp

url = input("Enter the YouTube video URL: ")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Video downloaded successfully!")
"""


"""
import yt_dlp

url = input("Enter the YouTube video URL: ")
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Ensures highest resolution with audio
    'merge_output_format': 'mp4'          # Ensures the output file is in MP4 format
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Video downloaded successfully!")
"""
from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware  #for security purpose#
import os
import yt_dlp

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#allows all origins
    allow_credentials=True,
    allow_methods=["*"],#allows all methods(get,post,etc)
    allow_headers=["*"],#allows all headers
)

cur_dir = os.getcwd()
@app.post("/download")
def download_video(link: str = Form(...)):

    youtube_dl_options={
        "format": "best",
        "outtmpl": os.path.join(cur_dir,f"{link}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status":"Download started"}

# download_video("https://youtu.be/TlksvQrUrQ4?si=lH9JvqMe4SVOZ9wu","video_filename")

# uvicorn backend:app (to run this) backend 
        