# AI 技术情报雷达 · 完整交付仓库

> **AI 应用 Lab 管培生 / 实习生测试题** — 方案设计 + 项目规划 + 可运行 Demo + 在线文档站

为 5–8 人 Lab 设计可自动跟踪、评估 AI 社区动态的「技术情报雷达」，辅助 **周度「是否投入」** 决策；MVP 目标 1–2 人、4 周落地。

---

## 在线访问

| 资源 | 链接 |
|------|------|
| **GitHub 仓库** | https://github.com/FBB123571/AI-Tech-Intelligence-Radar |
| **在线文档站（GitHub Pages）** | https://fbb123571.github.io/AI-Tech-Intelligence-Radar/ |
| **方案报告（提交用 · v3 对照补全）** | [docs/report.md](docs/report.md) |
| **实现架构图** | [diagrams/architecture-impl.mmd](diagrams/architecture-impl.mmd) |
| **FastAPI / Streamlit PoC** | [src/examples/](src/examples/) |
| **项目规划书** | [docs/project-plan.md](docs/project-plan.md) |
| **LLM 使用说明** | [docs/llm-usage.md](docs/llm-usage.md) |
| **示例周报** | [reports/sample_weekly_report.md](reports/sample_weekly_report.md) |

---

## 交付物清单（对齐测试题）

| # | 要求 | 路径 | 状态 |
|---|------|------|------|
| 1 | 方案设计报告（3–5 页，四章） | [docs/report.md](docs/report.md) | ✅ |
| 2 | 架构图（Mermaid，可导出 PNG） | [diagrams/architecture.mmd](diagrams/architecture.mmd) | ✅ |
| 3 | LLM 使用说明 | [docs/llm-usage.md](docs/llm-usage.md) | ✅ |
| 4 | 项目规划书（额外） | [docs/project-plan.md](docs/project-plan.md) | ✅ |
| 5 | 可运行 Demo | [src/radar/](src/radar/) | ✅ |
| 6 | 静态网站 | [docs/index.html](docs/index.html) | ✅ |

---

## 快速运行 Demo

```bash
cd AI-Tech-Intelligence-Radar
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python src/radar/cli.py demo
```

输出：终端评分表 + `reports/sample_weekly_report.md`

**在线拉取 arXiv（需网络）：**

```bash
python src/radar/cli.py fetch --limit 5
```

**Docker：**

```bash
docker build -t ai-radar-demo .
docker run --rm ai-radar-demo
```

---

## 目录结构

```
AI-Tech-Intelligence-Radar/
├── README.md
├── docs/
│   ├── index.html          # GitHub Pages 首页
│   ├── report.md           # 主报告（提交用）
│   ├── project-plan.md     # 项目规划书
│   └── llm-usage.md
├── diagrams/
│   └── architecture.mmd
├── src/radar/              # Demo 流水线
│   ├── cli.py
│   ├── agents/             # Classifier / Scorer / Writer
│   └── collectors/         # arXiv 等
├── data/sample/items.json
├── reports/                # 生成的周报
└── .github/workflows/      # Pages 自动部署
```

---

## 推送到 GitHub

```bash
git init
git add .
git commit -m "feat: complete AI tech intelligence radar deliverables"
git branch -M main
git remote add origin https://github.com/FBB123571/AI-Tech-Intelligence-Radar.git
git push -u origin main
```

推送后在 **Settings → Pages → Build and deployment → Source: GitHub Actions** 启用，站点将自动发布 `docs/`。

---

## 架构图预览

```bash
npx -y @mermaid-js/mermaid-cli -i diagrams/architecture.mmd -o diagrams/architecture.png
```

---

## 路径

- 远程：`/mnt/sdb1/leijh/AI-Tech-Intelligence-Radar`
- Windows：`D:\mnt\sdb1\leijh\AI-Tech-Intelligence-Radar`

---

## License

MIT — 见 [LICENSE](LICENSE)
