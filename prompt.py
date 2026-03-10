import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client  = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def generate_response(prompt, model="qwen-plus"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

prompt = """
将文本分类成中性，负面，正面
文本：明天又要带娃
输出格式：当前情感：[情感类型]
"""
print(generate_response(prompt))