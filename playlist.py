from pytube import YouTube, Playlist
import sys
PLAYLIST_URL = sys.argv[1]
directory = sys.argv[2]
playlist = Playlist(PLAYLIST_URL)

n = 1
print("Iniciando...")
for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    name = video.streams[0].title
    count_name = "0" + str(n) if n < 10 else str(n)
    new_name = count_name + " - " + name
    print("baixando: " + new_name)
    stream.download(directory, new_name)
    n += 1
print("Finalizado!")
