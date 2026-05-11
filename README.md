# TradingAgents-CN 🤖📈

> 基于多智能体框架的中国股市AI交易分析系统

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-支持-blue.svg)](https://docker.com)

## 简介

TradingAgents-CN 是 [TradingAgents](https://github.com/TauricResearch/TradingAgents) 的中文增强版本，专为中国A股、港股市场优化，集成了多个AI大模型，支持多智能体协作进行股票分析与交易决策。

> **个人备注**：我主要用 DeepSeek 模型 + A股数据跑分析，港股部分还没怎么测试过。

## ✨ 主要特性

- 🤖 **多智能体协作** - 基于LangGraph的多Agent框架，包含分析师、研究员、交易员等角色
- 🇨🇳 **中国市场支持** - 专为A股、港股优化，支持东方财富、同花顺等数据源
- 🧠 **多模型支持** - 支持OpenAI、DeepSeek、阿里百炼、腾讯混元等主流大模型
- 📊 **实时数据** - 集成多个金融数据接口，提供实时行情与历史数据
- 🐳 **Docker部署** - 提供完整的容器化部署方案
- 💬 **中文界面** - 全中文交互界面，分析报告中文输出

## 🚀 快速开始

### 环境要求

- Python 3.10+
- pip 或 conda
- Docker（可选）

### 安装

```bash
# 克隆仓库
git clone https://github.com/your-username/TradingAgents-CN.git
cd TradingAgents-CN

# 安装依赖
pip install -r requirements.txt

# 复制环境变量配置
cp .env.example .env
# 编辑 .env 文件，填入你的 API Keys
```

### 配置

编辑 `.env` 文件，配置必要的 API Keys：

```env
# 选择一个 LLM 提供商
OPENAI_API_KEY=your_openai_key
# 或
DEEPSEEK_API_KEY=your_deepseek_key

# 金融数据 API
FINANCIAL_DATASETS_API_KEY=your_key
```

### 运行

```bash
# 命令行模式
python main.py --ticker 600036 --market A股

# Web界面模式
python app.py
```

### Docker 部署

```bash
# 复制 Docker 环境配置
cp .env.docker .env

# 启动服务
docker-compose up -d
```

## 📖 文档

- [快速入门指南](docs/quickstart.md)
- [配置说明](docs/configuration.md)
- [API 文档](docs/api.md)
- [常见问题](docs/faq.md)

## 🏗️ 项目结构

```
TradingAgents-CN/
├── tradingagents/          # 核心模块
│   ├── agents/             # 各类智能体
│   ├── dataflows/          # 数据流处理
│   ├── graph/              # LangGraph 工作流
│   └── utils/              # 工具函数
├── docs/                   # 文档
├── tests/                  # 测试
├── main.py                 # 主入口
├── app.py                  # Web应用
└── docker-compose.yml      # Docker配置
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！请先阅读 [贡献指南](CONTRIBUTING.md)。

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 原项目：[TradingAgents](https://github.com/TauricResearch/TradingAgents)
- 上游 fork：[hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
