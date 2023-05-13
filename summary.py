from typing import Generator
from tqdm import tqdm
import openai
from enum import Enum

class Model(Enum):
    GPT4 = "gpt-4"
    GPT4_0314 = "gpt-4-0314"
    GPT4_32K = "gpt-4-32k"
    GPT4_32K_0314 = "gpt-4-32k-0314"
    GPT3_5 = "gpt-3.5-turbo"
    GPT3_5_0301 = "gpt-3.5-turbo-0301"


class Summary:

    def __init__(self, token: str, text_filename: str, summary_filename: str) -> None:
        openai.api_key = token
        self.text_filename = text_filename
        self.summary_filename = summary_filename

    def __read_file(self) -> Generator[str, None, None]:
        with open(self.text_filename, 'r', encoding='utf-8') as file:
            # 讀取檔案內容，並去除換行符號
            content = file.read().replace('\n', '')
            # 切割字串，每個元素字數不大於 1000
            for i in range(0, len(content), 1000):
                yield content[i:i+1000]

    def get_summary(self, model: 'Model' = Model.GPT3_5_0301) -> None:
        summary_list = []
        with open(self.text_filename, 'r', encoding='utf-8') as f:
            for paragraph in tqdm(self.__read_file()):
                completion = openai.ChatCompletion.create(
                model = model.value,
                messages = [
                        {"role": "system", "content": "請你成為文章摘要的小幫手，摘要以下文字，以繁體中文輸出"},
                        {"role": "user", "content": paragraph}
                    ]
                )
            summary_list.append(completion.choices[0].message.content)
        with open(self.summary_filename, 'w', encoding='utf-8') as f:
            for i in summary_list:
                f.write(i + '\n')