# 基础标签

> 定义 HTML 文档的基本结构和元数据

## 标签列表

### `<!DOCTYPE html>`

**作用:** 声明文档类型，告诉浏览器使用 HTML5 标准解析页面

**常用场景:**
- 每个 HTML 文档的第一行
- 不区分大小写

```html
<!DOCTYPE html>
```

---

### `<html>`

**作用:** HTML 文档的根元素，包含页面所有内容

**常用场景:**
- 包裹整个 HTML 文档
- 可以指定语言属性

```html
<html lang="zh-CN">
  <!-- 页面内容 -->
</html>
```

---

### `<head>`

**作用:** 包含文档的元数据，不会显示在页面上

**常用场景:**
- 设置页面标题
- 链接 CSS 样式表
- 添加 meta 信息

```html
<head>
  <title>页面标题</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
</head>
```

---

### `<body>`

**作用:** 包含文档的所有可见内容

**常用场景:**
- 页面的所有可见元素都放在这里
- 包含文本、图片、链接等

```html
<body>
  <h1>欢迎来到我的网站</h1>
  <p>这是一个段落</p>
</body>
```

---

### `<title>`

**作用:** 定义文档的标题，显示在浏览器标签页上

**常用场景:**
- 每个页面必须有一个标题
- 对 SEO 很重要

```html
<title>我的网页标题</title>
```

---

### `<meta>`

**作用:** 定义文档的元数据，提供给浏览器解析

**常用场景:**
- 设置字符编码
- 设置视口（响应式设计）
- 添加页面描述（SEO）

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="页面描述内容">
```

---

### `<link>`

**作用:** 链接外部资源，如样式表、图标等

**常用场景:**
- 链接 CSS 文件
- 设置网站图标
- 链接字体资源

```html
<link rel="stylesheet" href="style.css">
<link rel="icon" href="favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
```

---

### `<style>`

**作用:** 定义内部 CSS 样式

**常用场景:**
- 小型项目直接写在 head 中
- 动态生成样式

```html
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
</style>
```

---

### `<script>`

**作用:** 定义或引用 JavaScript 代码

**常用场景:**
- 链接外部 JS 文件
- 内联 JavaScript 代码
- 延迟加载脚本

```html
<script src="app.js"></script>
<script>
  console.log('Hello, World!');
</script>
<script defer src="app.js"></script>
```

---

### `<noscript>`

**作用:** 当浏览器不支持 JavaScript 时显示的内容

**常用场景:**
- 提示用户启用 JavaScript
- 提供替代内容

```html
<noscript>
  <p>您的浏览器不支持 JavaScript，请启用 JavaScript 以获得最佳体验。</p>
</noscript>
```
