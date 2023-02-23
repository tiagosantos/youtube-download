from pytube import YouTube, Playlist

PLAYLIST_URL = 'https://youtube.com/playlist?list=PLb6VOGXAYVXm2BOG5Q-_DBuedrz9yyGlU'
playlist = Playlist(PLAYLIST_URL)

n = 1
for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    name = video.streams[0].title
    count_name = "0" + str(n) if n < 10 else str(n)
    new_name = count_name + " - " + name
    stream.download('./download/playlist', new_name)
    n += 1
