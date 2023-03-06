import openai

class Summary:

    def __init__(self, token: str, text_filename: str, summary_filename: str) -> None:
        openai.api_key = token
        self.text_filename = text_filename
        self.summary_filename = summary_filename
    
    def get_summary(self) -> None:
        summary_list = []
        with open(self.text_filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                paragraph_len = len(line) // 1000 + 1
                for j in range(paragraph_len):
                    paragraph = line[j * 1000 : (j + 1) * 1000]
                    completion = openai.ChatCompletion.create(
                        model = "gpt-3.5-turbo",
                        messages = [
                                {"role": "system", "content": "請你成為文章摘要的小幫手，摘要以下文字，以繁體中文輸出"},
                                {"role": "user", "content": paragraph}
                            ]
                    )
                    summary_list.append(completion.choices[0].message.content)
        with open(self.summary_filename, 'w', encoding='utf-8') as f:
            for i in summary_list:
                f.write(i + '\n')