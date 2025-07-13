
import os
from src.input_loader import load_text_file, load_prompts
from src.workflow_engine import process_workflow
from src.data_writer import write_output_json
from src.md_renderer import render_markdown

# --- 配置文件路径 ---
DISCLOSURE_PATH = "data/technical_disclosure.txt"
PROMPTS_PATH = "data/prompts.json"
OUTPUT_JSON_PATH = "output.json"
OUTPUT_MD_PATH = "专利申请草案.md"

def main():
    """主函数，编排整个流程。"""
    print("--- [开始] AI 辅助专利申请文件生成 --- ")

    # 确保所有路径都是绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    disclosure_file = os.path.join(base_dir, DISCLOSURE_PATH)
    prompts_file = os.path.join(base_dir, PROMPTS_PATH)
    output_json_file = os.path.join(base_dir, OUTPUT_JSON_PATH)
    output_md_file = os.path.join(base_dir, OUTPUT_MD_PATH)

    try:
        # 1. 加载输入文件
        print("\n[步骤 1/4] 加载输入文件...")
        disclosure_content = load_text_file(disclosure_file)
        prompts = load_prompts(prompts_file)
        print("输入文件加载成功。")

        # 2. 执行工作流引擎
        print("\n[步骤 2/4] 执行工作流引擎...")
        patent_data = process_workflow(prompts, disclosure_content)
        print("工作流引擎执行完毕。")

        # 3. 写入 JSON 输出
        print("\n[步骤 3/4] 写入 JSON 输出...")
        write_output_json(patent_data, output_json_file)
        print("JSON 文件写入成功。")

        # 4. 渲染 Markdown 文件
        print("\n[步骤 4/4] 渲染 Markdown 文件...")
        render_markdown(output_json_file, output_md_file)
        print("Markdown 文件渲染成功。")

    except Exception as e:
        print(f"\n--- [错误] 程序执行失败 --- ")
        print(f"失败原因: {e}")
        return # 提前退出

    print("\n--- [完成] 所有任务已成功执行 --- ")
    print(f"最终输出文件位于: {output_md_file}")

if __name__ == "__main__":
    main()
