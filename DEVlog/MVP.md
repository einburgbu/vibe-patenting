## MVP（最小可行产品）定义

基于项目目标和现有代码，我建议的MVP最小实现如下：

### 一、MVP核心功能清单 🎯

```python
# MVP必须实现的功能（删除一个都不行）
1. ✅ 读取技术交底书（已完成）
2. ✅ 执行3步prompt链（已完成框架）
3. ⏳ 集成真实LLM API（待完成）
4. ✅ 生成markdown专利草案（已完成）

# MVP不包含的功能（后续迭代）
❌ MCP服务器
❌ 多LLM支持
❌ Web界面
❌ 批量处理
❌ 高级错误恢复
❌ 自定义模板
```

### 二、最小prompt链设计

```json
[
  {
    "step_name": "patent_title",
    "prompt_template": "基于以下技术交底书，生成一个准确的专利名称（15-30字）：\n\n{disclosure}\n\n专利名称："
  },
  {
    "step_name": "tech_field_and_background",
    "prompt_template": "基于技术交底书生成：\n1. 技术领域（1段）\n2. 背景技术及存在的问题（2-3段）\n\n技术交底书：\n{disclosure}\n\n输出："
  },
  {
    "step_name": "invention_content",
    "prompt_template": "基于技术交底书生成发明内容部分，包括：\n1. 发明目的\n2. 技术方案\n3. 有益效果\n\n技术交底书：\n{disclosure}\n\n输出："
  }
]
```

### 三、最简LLM客户端实现

```python
# src/llm_client.py - 最小实现
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(prompt: str) -> str:
    """最简单的LLM调用实现"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 成本最低
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"LLM调用失败: {e}")
        return f"[生成失败：{str(e)}]"
```

### 四、MVP交付物

```
patent-ai-mvp/
├── README.md              # 快速开始指南
├── requirements.txt       # 仅包含openai
├── .env.example          # API密钥模板
├── main.py               # 一键运行脚本
├── data/
│   ├── prompts.json      # 3步prompt链
│   └── technical_disclosure.txt  # 示例输入
├── src/
│   ├── llm_client.py     # 真实LLM调用
│   └── [其他已有模块]
└── output/
    ├── output.json       # 中间结果
    └── 专利申请草案.md   # 最终输出
```

### 五、MVP验收标准

#### 1. 功能验收 ✓
- [ ] 能读取技术交底书
- [ ] 能调用OpenAI API
- [ ] 能生成包含3个部分的专利草案
- [ ] 能输出可读的markdown文件

#### 2. 质量验收 ✓
- [ ] 生成的专利名称合理
- [ ] 技术领域描述准确
- [ ] 背景技术逻辑清晰
- [ ] 发明内容完整

#### 3. 可用性验收 ✓
- [ ] 一个命令即可运行
- [ ] 错误信息清晰
- [ ] 5分钟内完成生成
- [ ] 输出格式规范

### 六、MVP实施步骤（1天完成）

```bash
# 上午（2-3小时）
1. 配置OpenAI API环境
2. 替换mock客户端为真实调用
3. 简化prompts.json为3步
4. 首次运行测试

# 下午（2-3小时）  
5. 优化prompt质量
6. 处理常见错误
7. 编写README
8. 打包测试

# 晚上（1小时）
9. 邀请用户测试
10. 收集反馈
```

### 七、MVP成本估算

```python
# 单次运行成本
- 输入：~1000字技术交底书
- 3次API调用：~3000 tokens
- 成本：约 $0.01-0.02
- 时间：30-60秒

# 测试阶段成本
- 100次测试：$1-2
- 可接受范围内
```

### 八、MVP后的下一步

```
MVP完成后的优先级：
1. 优化prompt质量（1-2天）
2. 增加更多章节（2-3天）
3. 支持gpt-4（提升质量）
4. 添加简单CLI参数
5. 开发MCP服务器
```

### 九、关键简化决策

| 原计划 | MVP简化 | 理由 |
|--------|---------|------|
| 完整专利文档 | 仅3个核心章节 | 快速验证可行性 |
| 多LLM支持 | 仅OpenAI | 降低复杂度 |
| 复杂错误处理 | 基础try-catch | 快速实现 |
| 可配置模板 | 硬编码模板 | 减少开发时间 |
| 批量处理 | 单文件处理 | 专注核心功能 |

### 十、MVP成功标准

**技术成功：**
- ✅ 程序能稳定运行
- ✅ API调用成功率>90%
- ✅ 生成时间<1分钟

**业务成功：**
- ✅ 用户认为输出"有用"
- ✅ 相比手写节省>50%时间
- ✅ 用户愿意继续使用

这个MVP方案focused在最核心的价值验证上，1天即可完成，成本极低，但足以验证整个概念的可行性。