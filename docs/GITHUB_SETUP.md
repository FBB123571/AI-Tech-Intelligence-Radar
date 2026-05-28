# GitHub 上传与 Pages 启用指南

## 1. 创建远程仓库

在 GitHub 新建仓库：`AI-Tech-Intelligence-Radar`（Public，不要勾选 README 以免冲突）

## 2. 本地推送

```powershell
cd D:\mnt\sdb1\leijh\AI-Tech-Intelligence-Radar
git init
git add .
git commit -m "feat: complete deliverables — report, plan, demo, website"
git branch -M main
git remote add origin https://github.com/<你的用户名>/AI-Tech-Intelligence-Radar.git
git push -u origin main
```

## 3. 启用 GitHub Pages

1. 仓库 **Settings → Pages**
2. **Build and deployment → Source** 选择 **GitHub Actions**
3. 推送 `main` 后，Actions 工作流 `Deploy GitHub Pages` 会自动运行
4. 部署完成后访问：`https://<你的用户名>.github.io/AI-Tech-Intelligence-Radar/`

## 4. 更新网站上的 GitHub 链接

编辑 `docs/index.html`，将 `id="github-link"` 的 `href` 改为你的仓库 URL。

## 5. 验证 Demo

```powershell
python src/radar/cli.py demo
```

应生成 `reports/sample_weekly_report.md`。
