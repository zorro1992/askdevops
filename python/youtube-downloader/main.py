from pytube import YouTube
DOWNLOAD_FOLDER="~/Desktop/"
video_url="https://youtu.be/9dvsqwyHtBk"
video_obj=YouTube(video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)