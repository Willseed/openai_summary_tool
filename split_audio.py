from pydub import AudioSegment

class SplitAudio:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.segment_length = 600000
        self.output_file_amount = 0

    def set_segment_length(self, segment_length: int) -> None:
        self.segment_length = segment_length

    def split_mp3_file(self) -> None:
        # 載入 MP3 音檔
        sound = AudioSegment.from_file(self.filename, format='mp3')
        # 將音檔分割成多個檔案
        for i, chunk in enumerate(sound[::self.segment_length]):
            # 設定分割檔案的檔名
            chunk.export(f'output_{i + 1}.mp3', format='mp3')
            self.output_file_amount += 1

    def get_output_file_amount(self) -> int:
        return self.output_file_amount
