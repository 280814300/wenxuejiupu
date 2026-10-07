// 全站常量集中管理，避免散落硬编码

export const SITE = {
  domain: 'wenxuejiupu.com',
  title: '文学酒铺',
  slogan: '记录科技与人文',
  description: '开源软件分享 · AI 软件落地教学 · 网盘资源工具内容',
  author: '文学酒铺',
} as const;

// 三个栏目（content collections）元数据
export const COLUMNS = {
  ai: {
    name: 'AI 应用',
    desc: 'AI 软件落地教学，讲清怎么在国内网络环境下真正用起来',
  },
  tools: {
    name: '软件分享',
    desc: '开源与免费软件的分享、评测与自托管指南，含效率工具清单',
  },
  resources: {
    name: '资源合集',
    desc: '高频网盘资源与下载工具的整理，省去你的寻找时间',
  },
  humanities: {
    name: '人文记录',
    desc: '在科技之外，记录阅读、思考与生活的人文随笔',
  },
} as const;

// 由 COLUMNS 派生导航数组（顺序即展示顺序）
export const NAV = (
  Object.keys(COLUMNS) as Array<keyof typeof COLUMNS>
).map((key) => ({
  slug: key,
  name: COLUMNS[key].name,
}));

// 栏目 key 联合类型
export type ColumnKey = keyof typeof COLUMNS;
