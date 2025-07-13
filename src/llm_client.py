
def generate_mock_content(prompt: str) -> str:
    """
    一个模拟的 LLM 生成函数。
    接收一个 prompt，返回一个固定的、可预测的字符串，用于测试。
    """
    # 为了让模拟更有意义，我们可以返回一个与 prompt 相关的、结构化的字符串
    mock_response = f'这是针对以下提示的模拟回复：\n---\n{prompt[:80]}...\n---\n模拟内容已生成。'
    
    print(f"\n--- [模拟LLM调用] ---")
    print(f"接收到的 Prompt (前80字符): {prompt[:80]}...")
    print(f"返回的模拟内容: {mock_response}")
    print(f"-----------------------\n")
    
    return mock_response
