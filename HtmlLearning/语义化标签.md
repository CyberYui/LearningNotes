# 语义化标签

> 定义页面结构和内容区域

## 标签列表

### `<header>`

**作用:** 定义页面或区块的头部

**常用场景:**
- 网站头部
- 文章标题区域
- 包含导航和 Logo

**深度示例:** 见 [[Learning/semantic-tags.html]]

```html
<header>
  <h1>网站标题</h1>
  <nav>
    <a href="/">首页</a>
    <a href="/about">关于</a>
  </nav>
</header>
```

---

### `<footer>`

**作用:** 定义页面或区块的底部

**常用场景:**
- 网站页脚
- 版权信息
- 相关链接

```html
<footer>
  <p>© 2024 版权所有</p>
  <a href="/privacy">隐私政策</a>
</footer>
```

---

### `<main>`

**作用:** 定义页面的主要内容

**常用场景:**
- 每个页面只能有一个
- 包含页面核心内容

```html
<main>
  <article>
    <h2>文章标题</h2>
    <p>文章内容...</p>
  </article>
</main>
```

---

### `<article>`

**作用:** 定义独立的内容块

**常用场景:**
- 博客文章
- 新闻报道
- 评论区

```html
<article>
  <h2>文章标题</h2>
  <p>作者: 张三</p>
  <p>文章内容...</p>
</article>
```

---

### `<section>`

**作用:** 定义文档中的节

**常用场景:**
- 内容分组
- 通常包含标题
- 比 div 更有语义

```html
<section>
  <h2>章节标题</h2>
  <p>章节内容...</p>
</section>
```

---

### `<nav>`

**作用:** 定义导航链接

**常用场景:**
- 主导航菜单
- 侧边栏导航
- 面包屑导航

```html
<nav>
  <ul>
    <li><a href="/">首页</a></li>
    <li><a href="/about">关于</a></li>
    <li><a href="/contact">联系</a></li>
  </ul>
</nav>
```

---

### `<aside>`

**作用:** 定义侧边栏内容

**常用场景:**
- 侧边栏
- 广告
- 相关文章推荐

```html
<aside>
  <h3>相关文章</h3>
  <ul>
    <li><a href="#">文章一</a></li>
    <li><a href="#">文章二</a></li>
  </ul>
</aside>
```

---

### `<figure>` 和 `<figcaption>`

**作用:** 定义独立的流内容（如图片、图表）及其说明

**常用场景:**
- 图片和说明文字
- 代码块和标题
- 图表和注释

```html
<figure>
  <img src="chart.png" alt="数据图表">
  <figcaption>图1: 2024年销售数据统计</figcaption>
</figure>
```

---

### `<details>` 和 `<summary>`

**作用:** 定义可折叠的内容

**常用场景:**
- FAQ 问答
- 折叠面板
- 更多信息展开

```html
<details>
  <summary>点击查看详情</summary>
  <p>这是隐藏的内容，点击后展开显示。</p>
</details>
```
