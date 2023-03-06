from download import Download
from split_audio import SplitAudio
from speech_to_text import SpeechToText
from summary import Summary

with open('key.txt', 'r', encoding='utf-8') as f:
    TOKEN = f.read().strip()

url = 'https://youtu.be/fPBNGLghVLU'
prefix = 'audio'
suffix = '.mp3'
origin_audio_file = prefix + suffix

mp3 = Download(prefix, url)
mp3.get_mp3_file_from_youtube()

# 預設切割10分鐘
audio_file = SplitAudio(origin_audio_file)
audio_file.split_mp3_file()
file_amount = audio_file.get_output_file_amount()
print(f'file_amount : {file_amount}')

text_result_file = 'text_result.txt'
speech_to_text = SpeechToText(TOKEN, text_result_file, file_amount)
speech_to_text.output_text_result()

summary_result_file = 'summary_result.txt'
summary = Summary(TOKEN, text_result_file, summary_result_file)
summary.get_summary()