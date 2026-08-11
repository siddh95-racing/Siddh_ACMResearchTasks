import re
from datetime import datetime
def transform_logs(input_text: str) -> str:

    input_text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        '[HIDDEN]',
        input_text
    )
    pattern = r'\b(\d{2}/\d{2}/\d{4} \d{2}:\d{2})\b'

    def convert_timestamp(match):
        date = datetime.strptime(match.group(), "%d/%m/%Y %H:%M")
        return date.strftime("%d %B %Y, %#I:%M %p")

    input_text = re.sub(pattern, convert_timestamp, input_text)

    input_text = input_text.replace("ERROR", "🚨 ERROR")

    return input_text

text = "User john@mail.com logged in at 23/08/2025 14:05. ERROR: session timeout."
result = transform_logs(text)
print(result)