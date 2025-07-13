
import json
from typing import Dict, Any

def render_markdown(json_path: str, md_path: str):
    """读取 output.json 文件并渲染成 Markdown 专利草案。"""
    print(f"\n--- 正在从 {json_path} 渲染 Markdown 文件到 {md_path} ---")

    # 1. 读取 JSON 数据
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"错误：JSON 数据文件未找到 -> {json_path}")
        raise
    except Exception as e:
        print(f"读取 JSON 文件时发生错误 -> {json_path}: {e}")
        raise

    # 2. 定义 Markdown 模板
    # 使用 f-string 和 .get() 方法来安全地访问字典键
    md_template = f"""
# 专利申请文件（草案）

## 一、发明名称

（待定）

## 二、技术领域

{data.get('tech_field', '[技术领域未生成]')}

## 三、背景技术

{data.get('background_pain_points', '[背景技术分析未生成]')}

## 四、发明内容

{data.get('invention_content', '[发明内容未生成]')}

## 五、附图说明

（无）

## 六、具体实施方式

（待补充）

---
*该文件由 AI 辅助生成，请务必进行人工审核和修改。*
"""

    # 3. 写入 Markdown 文件
    try:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_template)
        print(f"成功将 Markdown 文件渲染到 {md_path}")
    except Exception as e:
        print(f"写入 Markdown 文件时发生错误 -> {md_path}: {e}")
        raise
