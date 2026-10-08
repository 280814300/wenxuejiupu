// rehype 插件：把文章正文中出现的裸域名 wenxuejiupu.com 自动转为指向本站的内链。
// 不处理 <code> / <pre> / <a> 内部，避免破坏代码示例与已有链接。
// 站点标准（见 发布流程.md）：所有文章正文提及 wenxuejiupu.com 自动内链，作者无需手加。

const DOMAIN = 'wenxuejiupu.com';
const HREF = 'https://wenxuejiupu.com/';
const SKIP_TAGS = new Set(['code', 'pre', 'a']);

export default function rehypeAutoLinkDomain() {
  return (tree) => {
    walk(tree);
  };
}

function walk(node) {
  if (!node || !Array.isArray(node.children)) return;
  const out = [];
  for (const child of node.children) {
    if (
      child.type === 'text' &&
      typeof child.value === 'string' &&
      child.value.includes(DOMAIN)
    ) {
      const parts = child.value.split(DOMAIN);
      for (let i = 0; i < parts.length; i++) {
        if (parts[i] !== '') out.push({ type: 'text', value: parts[i] });
        if (i < parts.length - 1) {
          out.push({
            type: 'element',
            tagName: 'a',
            properties: { href: HREF, className: ['auto-domain-link'] },
            children: [{ type: 'text', value: DOMAIN }],
          });
        }
      }
    } else if (child.type === 'element' && SKIP_TAGS.has(child.tagName)) {
      // 代码 / 代码块 / 已有链接内部：保留原样
      out.push(child);
    } else {
      walk(child);
      out.push(child);
    }
  }
  node.children = out;
}
