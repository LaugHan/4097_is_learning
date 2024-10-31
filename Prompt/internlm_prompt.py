#./4097_is_learning/Prompt/internlm_prompt.py
from openai import OpenAI
import os
def internlm_gen(prompt, query, client):
    '''
    LLM生成函数
    Param prompt: prompt string
    Param client: OpenAI client 
    '''
    response = client.chat.completions.create(
        model="internlm2.5-latest",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content":query},
      ],
        stream=False
    )
    return response.choices[0].message.content

api_key = os.getenv('api_key')
#api_key = "" #也可以明文写在代码内，不推荐
client = OpenAI(base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",api_key=api_key)
prompt = '''
- Role: 字母统计专家
- Profile: 你是一位对字母和单词结构有深入研究的专家，擅长快速准确地识别和统计特定字母在单词中的出现次数。
- Skills: 你具备出色的视觉辨识能力，能够迅速识别单词中的字母，并准确计算特定字母的出现频率。
- Rules: 必须提供准确无误的统计结果，确保用户能够信赖并应用于学习或工作中。
- Workflow:
  1. 观察指定的单词。
  2. 识别并计数特定字母的出现次数。具体，将特定字母与单词中的每一个字母比较，每次与特定字母相同时，计数加1
  3. 向用户报告特定字母的准确数量。
- Examples:
  - 例子1：单词 “blueberry” 中字母 “r” 的数量是 2。
  - 例子2：单词 “red” 中字母 “r” 的数量是 1。
  - 例子3：单词 “English” 中字母 “r” 的数量是 0。
  - 例子4：单词 “abcaaa” 中字母 “a” 的数量是 4。
- Initialization: 在第一次对话中，请直接输出以下：您好，我可以帮助您快速准确地统计任何单词中特定字母的数量。现在，请告诉我您想要统计的单词以及特定的字母。
'''
query = '''
“strawberry”中有几个字母“r”
'''
response = internlm_gen(prompt, query, client)
print(response)
