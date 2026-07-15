# AI Agent Zero To Hundred

一个可逐步扩展的 Python Agent 项目骨架。

## 项目架构

```text
AI-Agent-Zero-To-Hundred/
├── README.md                 # 项目说明与开发指南
├── pyproject.toml            # Python 项目、工具与测试配置
├── .env.example              # 环境变量模板（不存放真实密钥）
├── requirements.txt          # Python 依赖清单
├── run.py                    # 项目启动入口
├── agent/
│   ├── __init__.py           # Agent 包标识
│   ├── core/                 # Agent 核心循环、状态与编排逻辑
│   ├── prompts/              # 系统提示词、任务模板与输出格式
│   ├── skills/               # 可复用能力模块，如检索、总结、代码生成
│   ├── memory/               # 会话级上下文记忆与历史轮次管理
│   ├── tools/                # 对外部服务、文件、命令等工具的封装
│   ├── agents/               # 专项子 Agent 与协作角色定义
│   ├── configs/              # 模型、运行参数与应用配置
│   ├── data/                 # 本地运行数据与示例数据
│   └── tests/                # 单元测试与集成测试
```

## 一句话到输出的执行流程

```text
用户输入 → 读取历史上下文 → 调用模型 → 保存本轮问答 → 输出回答
```

`run.py` 启动程序，`core/runner.py` 负责对话循环，`tools/llm.py` 负责调用模型。

## Memory 上下文记忆

当前为会话级短期记忆，由 `agent/memory/conversation.py` 管理。

```text
程序启动 → 创建空记忆
用户提问 → 将历史问答与当前问题一起发给模型
模型回答 → 保存本轮“问题 + 回答”
超过上限 → 自动删除最早的完整对话
```

默认保留最近 10 轮完整问答，可在 `.env` 中修改：

```env
MEMORY_MAX_TURNS=10
```

- 输入 `/clear` 清空记忆。
- 输入 `exit` 退出程序。
- 记忆仅保存在内存中，程序重启后清空。

## 快速开始

```bash
python -m venv .venv
pip install -r requirements.txt
copy .env.example .env
python run.py
```

将 `.env` 中的 `OPENAI_API_KEY` 替换为自己的密钥后，再接入模型调用逻辑。
