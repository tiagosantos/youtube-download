import sys
from pytube import YouTube
youtube_link = sys.argv[1]
directory = sys.argv[2]
print("Iniciando...")
YouTube(youtube_link).streams.filter(only_audio=True)[0].download(directory)
name = YouTube(youtube_link).streams[0].title
print("baixando: " + name)
print("Finalizado!")
