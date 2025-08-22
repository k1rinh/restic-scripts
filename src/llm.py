# TODO:
# - [ ] 通过自然语言生成 OnCalendar Expression。

# Reference:
# - https://openrouter.ai/docs/quickstart
# - https://github.com/cuu508/oncalendar/


from datetime import datetime

import requests
from oncalendar import BaseIterator

# from tabulate import tabulate
from .config import LLM_API_KEY, LLM_API_URL

SYSTEM_PROMPT = """你是一个专业的时间表达式生成器，专门为 systemd 的 .timer 单元生成 OnCalendar 时间规则。用户将以自然语言描述时间计划，你需要准确转换为标准的 OnCalendar 表达式，并确保语法正确。

输入：用户提供自然语言的时间描述（如“每周三下午3点”）。
输出：
标准的 OnCalendar 表达式（如 Wed *-*-* 15:00:00），不要包含任何额外的说明。
错误处理：
如果出现包括但不限于下面的错误，请在回复中带上 `WARN` 关键词。
如果时间描述含糊（如“工作日上午”），要求用户澄清。
如果规则无法用 OnCalendar 实现（如“每月最后一个周五”），说明原因并提供替代方案。
"""


def parse_llm_response(response: dict):
    pass


def generate_oncalendar_from_text(text):
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    }

    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    return response.json()


def verify_oncalendar(
    oncalendar,
):
    it = BaseIterator(oncalendar, datetime.now())
    for _ in range(0, 10):
        print(next(it))
