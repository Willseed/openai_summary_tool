import yt_dlp


class Download:
    def __init__(self, filename: str, url: str) -> None:
        self.filename = filename
        self.url = url
    
    def get_mp3_file_from_youtube(self) -> None:
        # 設定選項
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': self.filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': 'bestaudio',
            }],
            'audio-format': 'mp3',
            'audio-quality': 'bestaudio'
        }

        # 建立 yt_dlp 下載器物件
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])