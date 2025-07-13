
import json
from typing import Dict, Any

def write_output_json(data: Dict[str, Any], file_path: str):
    """将数据字典以格式化的 JSON 写入文件。"""
    print(f"\n--- 正在将结果写入 {file_path} ---")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"成功将数据写入 {file_path}")
    except Exception as e:
        print(f"写入 JSON 文件时发生错误 -> {file_path}: {e}")
        raise
