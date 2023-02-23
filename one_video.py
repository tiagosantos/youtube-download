from pytube import YouTube
youtube_link = 'https://youtu.be/Ufv7MNSBBVw'
YouTube(youtube_link).streams.get_highest_resolution().download('./download')
