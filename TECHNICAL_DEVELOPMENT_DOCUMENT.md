# 技术开发需求文档

**文档版本:** 1.0
**日期:** 2025-07-11

#### 2.1. 系统架构

本系统采用三层模块化架构：**输入与配置层**、**核心处理引擎** 和 **输出与渲染层**。

*   **输入与配置层**：负责加载所有初始数据和配置，包括技术交底书和 Prompt 链定义。
*   **核心处理引擎**：负责编排整个工作流，与 LLM API 交互，并管理生成过程中的数据状态。
*   **输出与渲染层**：负责将最终的结构化数据持久化，并根据需求渲染成特定格式的文档。

#### 2.2. 模块详细设计

1.  **输入模块 (`input_loader`)**
    *   **功能**：读取 `technical_disclosure.txt` 和 `prompts.json`。
    *   **输入**：文件路径。
    *   **输出**：字符串形式的技术交底书内容，以及解析为 Python 列表/字典的 Prompt 链配置。
    *   **错误处理**：需处理文件未找到、JSON 格式错误等异常。

2.  **核心处理引擎 (`workflow_engine`)**
    *   **功能**：整个工作流的指挥官。
    *   **逻辑**：
        a. 初始化一个空字典 `patent_data` 用于存储结果。
        b. 遍历 `prompts.json` 中的每一个步骤对象。
        c. 对每个步骤，使用 `str.format()` 或类似方法，将 `patent_data` 中已有的内容填充到当前步骤的 `prompt_template` 中。
        d. 调用 LLM API 封装器，发送格式化后的 Prompt。
        e. 将 LLM 返回的结果，以步骤名（`step_name`）为键，存入 `patent_data` 字典。
        f. 循环直至所有步骤完成。
    *   **依赖**：需要一个 LLM API 的封装模块 (`llm_client`)。

3.  **LLM API 封装器 (`llm_client`)**
    *   **功能**：封装对具体 LLM（如 OpenAI, Gemini 等）的 API 调用。
    *   **接口**：提供一个简单的函数，如 `generate(prompt: str) -> str`。
    *   **职责**：处理 API Key、网络请求、超时、重试逻辑和错误处理。

4.  **数据输出模块 (`data_writer`)**
    *   **功能**：将最终完成的 `patent_data` 字典写入 `output.json` 文件。
    *   **要求**：使用 `utf-8` 编码，并进行格式化（`indent=2`）以提高可读性。

5.  **Markdown 渲染模块 (`md_renderer`)**
    *   **功能**：读取 `output.json`，生成 `.md` 文件。
    *   **逻辑**：内置一个固定的 Markdown 模板字符串，使用 f-string 或其他模板引擎，将 JSON 中的数据填入模板，然后写入文件。

#### 2.3. 技术栈选型

*   **语言**: Python 3.9+
*   **标准库**: `json`, `os`
*   **第三方库**:
    *   LLM API SDK (例如 `openai`, `google-generativeai`)
*   **开发环境**: `venv` 或 `conda` 进行环境隔离。
