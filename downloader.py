# downloader.py
import yt_dlp, os

def download_youtube(urls, download_folder):
    results = []
    for url in urls:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
            'ignoreerrors': True,
            'extract_flat': False,
            'yes_playlist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            results.append(url)
    return results
