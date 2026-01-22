import csv
import os
import re

# 读取 keywords.csv
with open('keywords.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# 创建目录
os.makedirs('src/content/tools', exist_ok=True)

for row in rows:
    # 将 keyword 转为 slug（如 "json to yaml converter" → "json-to-yaml-converter"）
    slug = re.sub(r'[^a-z0-9]+', '-', row['keyword'].lower()).strip('-')
    
    # 根据 intent 决定内容
    if row['intent'] == 'explain':
        body = f"""## What You'll Learn

This guide explains **{row['keyword']}** in simple terms, with practical examples and common pitfalls to avoid.
"""
    else:
        tool_name = row['keyword'].replace('online', '').replace('tool', '').strip()
        body = f"""## How It Works

This tool processes your {tool_name} instantly in the browser. No data is sent to any server — everything runs locally for maximum privacy and speed.
"""

    md_content = f"""---
keyword: "{row['keyword']}"
intent: "{row['intent']}"
template: "{row['template']}"
h1: "{row['h1']}"
meta_desc: "{row['meta_desc']}"
faq:
  - question: "Is this tool secure?"
    answer: "Yes. All processing happens in your browser. No data leaves your device."
  - question: "Do I need to sign up?"
    answer: "No. This is a free, no-registration tool."
---

{body}
"""

    with open(f'src/content/tools/{slug}.md', 'w', encoding='utf-8') as f:
        f.write(md_content)

print(f"✅ 成功生成 {len(rows)} 个页面！")
print("接下来：")
print("1. 运行 `npm run dev`")
print("2. 访问 http://localhost:4321/json-to-yaml-converter 等页面测试")