# LLM 使用说明

> 对应 `report.md` 第 4 节；满足题目对「AI 协作透明度」的评测要求。  
> **版本**：v2.0 · **日期**：2026-05-28（精加工交付轮）

---

## 使用的工具与模型

| 项目 | 内容 |
|------|------|
| **IDE / Agent** | Cursor Agent（Auto） |
| **模型** | Cursor 路由后端模型（对话、多文件生成、CLI 编排） |
| **日期** | 2026-05-28 |
| **任务** | 完整交付：精加工报告、项目规划书、Demo 代码、GitHub Pages 站点、仓库初始化 |

---

## 各交付物的 AI 参与程度

### `docs/report.md`（主报告 · 约 3–5 页）

| 部分 | AI 贡献 | 人工/提交者责任 |
|------|---------|-----------------|
| §1 质疑与假设 | 模糊点表格、假设 A1–A5、范围边界 | 按真实 Lab 方向收紧；答辩时能说清取舍 |
| §2 方案设计 | 架构分层、三 Agent、源列表、Rubric、里程碑 | 核对 4 周人力是否成立；删无法访问的源 |
| §3 设计决策 | 决策表、权衡、风险缓解 | 确认与 Lab 资源一致 |
| §4 LLM 说明 | 交叉引用本文件 | 签字认可 |

### `docs/project-plan.md`（项目规划书 · 额外）

| 部分 | AI 贡献 | 人工责任 |
|------|---------|----------|
| WBS / 甘特 / 预算 | 全文起草 | 调整日期与人名 |
| 风险与质量 | 标准模板 | 补充 Lab 特有风险 |

### `diagrams/architecture.mmd`

- **AI**：Mermaid 分层图，与报告模块一一对应。  
- **人工**：答辩前预览，术语与内部命名对齐。

### `src/radar/`（Demo 实现）

| 模块 | AI 贡献 | 说明 |
|------|---------|------|
| `agents/classifier.py` | 规则引擎草案 | 生产可换 LangGraph + LLM JSON Schema |
| `agents/scorer.py` | Rubric 加权逻辑 | 读取 `focus.yaml`，与报告 §2.5 一致 |
| `agents/writer.py` | 周报 Markdown 模板 | 与报告附录 A 结构一致 |
| `collectors/arxiv.py` | arXiv API 适配器 | `fetch` 命令需网络 |
| `cli.py` | 命令行入口 | `demo` 离线可跑 |

### `docs/index.html` + `docs/assets/style.css`（网站）

- **AI**：静态站布局、Mermaid 嵌入、周报预览逻辑。  
- **人工**：部署后检查 GitHub Pages URL。

### `README.md`

- **AI**：交付清单、运行说明、Git 推送步骤。  
- **人工**：填写 GitHub 用户名、作者姓名。

---

## 精加工轮次用户指令（摘要）

> 精加工满足测试题全部内容；生成完整 md、项目规划书、demo、同步 GitHub、建立网页。

约束仍来自题目：5–8 人 Lab、周度决策、Agent 架构、4 周 MVP、四章节报告 + 架构图 + LLM 说明。

---

## 提交前人工核对清单（必做 5 项）

1. **替换 Lab 方向**：编辑 `src/focus.yaml` 与报告中「RAG / Agent / 端侧」为真实课题。  
2. **核对信息源**：删除无法稳定访问的源（如 Twitter API）。  
3. **通读 Rubric 权重**：是否反映 Lab 价值观。  
4. **本地跑通 Demo**：`python src/radar/cli.py demo` 无报错。  
5. **GitHub**：创建远程仓库并 `git push`；在 Settings 启用 Pages（GitHub Actions）。

---

## 诚信声明

- 方案与代码由 AI 辅助生成，**架构取舍与答辩问答须由提交者理解并认可**。  
- Demo 使用**规则 Scorer** 以便离线演示；实习实现阶段应替换为 LangGraph + LLM，并在此更新「实现阶段」表格。

---

## 实现阶段记录（后续填写）

| 模块 | AI 用于 | 人工编写 |
|------|---------|----------|
| LangGraph 编排 | | |
| 真实 LLM Scorer | | |
| Streamlit 看板 | | |
| 飞书 Webhook | | |
