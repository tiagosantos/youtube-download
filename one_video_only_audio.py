from pytube import YouTube
youtube_link = 'https://youtu.be/Ufv7MNSBBVw'
YouTube(youtube_link).streams.filter(
    only_audio=True)[0].download('./download/audio')
