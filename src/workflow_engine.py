
from typing import List, Dict, Any
from src.llm_client import generate_mock_content

def process_workflow(prompts: List[Dict[str, Any]], disclosure_content: str) -> Dict[str, Any]:
    """
    处理整个专利生成工作流。

    Args:
        prompts: 从 prompts.json 加载的配置列表。
        disclosure_content: 技术交底书的原始内容。

    Returns:
        一个包含所有输入和生成内容的字典。
    """
    patent_data = {"disclosure": disclosure_content}

    print("=== 开始工作流处理 ===")

    for step in prompts:
        step_name = step["step_name"]
        prompt_template = step["prompt_template"]
        dependencies = step["dependencies"]

        print(f"\n--- 步骤: {step_name} ---")

        # 1. 检查依赖项是否都已满足
        if not all(dep in patent_data for dep in dependencies):
            print(f"错误：步骤 {step_name} 的依赖项 {dependencies} 未满足。跳过此步骤。")
            continue

        # 2. 格式化 prompt
        try:
            # 从 patent_data 中提取当前 prompt 需要的上下文
            context_for_prompt = {dep: patent_data[dep] for dep in dependencies}
            formatted_prompt = prompt_template.format(**context_for_prompt)
        except KeyError as e:
            print(f"错误：格式化 prompt 模板时缺少键: {e}。跳过此步骤。")
            continue
        
        print(f"已为步骤 '{step_name}' 准备好 Prompt。")

        # 3. 调用 (模拟) LLM 生成内容
        generated_content = generate_mock_content(formatted_prompt)

        # 4. 将生成的内容存入数据字典
        patent_data[step_name] = generated_content
        print(f"步骤 '{step_name}' 已完成，结果已存储。")

    print("\n=== 工作流处理完成 ===")
    return patent_data
