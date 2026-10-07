# 文学酒铺 · 部署指南（Cloudflare Pages）

本仓库是一个 **Astro 5 纯静态站**，已通过 Schema 质检（构建即把关 front matter）。
下面给出从「本地仓库」到「Cloudflare Pages 公网」的完整步骤。

---

## 一、本地前置（已完成可跳过）

```bash
cd wenxuejiupu
node -v                 # 建议 20.x（见 .nvmrc）
npm install
npm run build           # 构建产物在 dist/，同时生成 sitemap-index.xml
npm run dev             # 本地预览 http://localhost:4321
```

> 构建若报 `InvalidContentEntryDataError`，说明某篇 md 的 front matter 不符合
> `src/content.config.ts` 的 zod Schema —— 按报错改完再构建即可（这是验收标准第 2 条）。

---

## 二、推送到 GitHub

本项目**尚未初始化 git**。按以下步骤建立本地提交并关联远程：

```bash
git init
git add .
git commit -m "feat: 文学酒铺 Astro 静态站（4 栏目 + 留言板 + Schema 质检）"

# 在你的 GitHub 新建空仓库后，关联并推送（把 <your-repo> 换成实际地址）
git remote add origin https://github.com/<你的用户名>/wenxuejiupu.git
git branch -M main
git push -u origin main
```

> `.gitignore` 已忽略 `node_modules/`、`dist/`、`.astro/`，不会把构建产物和依赖传上去。

---

## 三、Cloudflare Pages 连接（Dashboard 方式）

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**。
2. 授权并选择刚才推送的 `wenxuejiupu` 仓库。
3. 构建配置（**Framework preset 选 Astro** 后多数会自动填充，核对即可）：

   | 项 | 值 |
   |---|---|
   | Framework preset | **Astro** |
   | Build command | `npm run build` |
   | Build output directory | `dist` |
   | Node.js version | **20**（由仓库根目录 `.nvmrc` 自动读取；若面板未识别，在 **Settings → Build & deployments → Environment variables** 加 `NODE_VERSION=20`）|

4. 点击 **Save and Deploy**。首次部署约 1–2 分钟。
5. 部署完成后会得到一个 `*.pages.dev` 预览域名。

### 绑定正式域名（wenxuejiupu.com）
- **Custom domains** → 添加 `wenxuejiupu.com` 与 `www.wenxuejiupu.com`。
- 按提示到你的 DNS 服务商处添加 Cloudflare 给出的 CNAME 记录。
- 注意：`astro.config.mjs` 里的 `site` 已设为 `https://wenxuejiupu.com`，
  改域名时同步改这里（影响 canonical / sitemap 绝对路径）。

---

## 四、后续更新流程

每次新文章或改稿：

```bash
# 1) 在 src/content/<栏目>/ 下按《写作规范》写 md（front matter 必须合规）
# 2) 本地构建验证 Schema 质检通过
npm run build
# 3) 提交并推送，Cloudflare Pages 自动重新部署
git add . && git commit -m "docs: 新增/更新 xxx" && git push
```

Cloudflare Pages 监听 `main` 分支 push，自动触发构建发布。

---

## 五、验证清单

- [ ] `npm run build` 本地零错误，dist/ 生成 sitemap-index.xml
- [ ] GitHub 仓库已推送 main 分支
- [ ] Cloudflare Pages 构建成功（Framework=Astro, output=dist, NODE_VERSION=20）
- [ ] 访问 `https://wenxuejiupu.com/` 首页、各栏目、文章页、留言板均正常
- [ ] `https://wenxuejiupu.com/sitemap-index.xml` 可访问
