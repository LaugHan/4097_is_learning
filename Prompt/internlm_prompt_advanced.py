# 没想好怎么做

from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv('api_key'),
    base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
)

chat_rsp = client.chat.completions.create(
    model="internlm2.5-latest",
    messages=[{"role": "user", "content": "hello"}],
    stream=True,
)

for chunk in chat_rsp:
    print(chunk.choices[0].delta.content)