from pytube import YouTube
import sys
import os
import logging
import subprocess

def download(link):
    yt = YouTube(link)

    print("V-streams list:")
    vstreams = yt.streams.filter(only_video=True, progressive=False)
    for i in vstreams:
        print(i)

    print("A-streams list:")
    astreams = yt.streams.filter(only_audio=True)
    for i in astreams:
        print(i)

    print(1)
    print("A total of " + str(vstreams[0].filesize) + " bytes of the video is going to be downloaded.")
    ys = yt.streams.get_by_itag(vstreams[0].itag)
    ys.download(filename="video")
    print(2)
    ys = yt.streams.get_by_itag(astreams[0].itag)
    ys.download(filename="audio")
    print(3)

    subprocess.call(['ffmpeg', '-i', 'video', '-i', 'audio', '-c:v', 'copy', '-c:a', 'aac', yt.title+".mp4"])
    ##ffmpeg.concat(input_video, input_audio, v=1, a=1).output(yt.title+".mp4").run()
    # https://www.youtube.com/watch?v=C6ZqJ-5v3o4

input = sys.argv[1]
if os.path.exists(input):
    with open(input, 'r') as file:
        for link in file:
            try:
                download(link)
            except Exception as e:
                logging.error(e)
else:
    try:
        download(input)
    except Exception as e:
        logging.error(e)