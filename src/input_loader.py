
import json
from typing import List, Dict, Any

def load_text_file(file_path: str) -> str:
    """读取指定的文本文件内容。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件未找到 -> {file_path}")
        raise
    except Exception as e:
        print(f"读取文件时发生未知错误 -> {file_path}: {e}")
        raise

def load_prompts(file_path: str) -> List[Dict[str, Any]]:
    """读取并解析 prompts.json 文件。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：Prompt 配置文件未找到 -> {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"错误：Prompt 配置文件格式不正确，无法解析 -> {file_path}")
        raise
    except Exception as e:
        print(f"读取 Prompt 配置文件时发生未知错误 -> {file_path}: {e}")
        raise
