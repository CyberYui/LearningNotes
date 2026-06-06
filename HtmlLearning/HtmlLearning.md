# HTML 学习笔记

> 一个文件包含所有的知识点
>
> 例子只挑一些必要的放在 Learning 文件夹中

## HTML 简介

- 即 **超文本标记语言 ( Hyper Text Markup Language )**, 它是一种标记语言而非编程语言, 即使用标记标签来描述网页
- HTML 标签和 HTML 元素一般描述的是同样的意思, 现使用的 HTML5 于2014年成为 W3C 推荐标准
- HTML 文档的后缀名必须是 `.html` 或者 `.htm`, 浏览器的作用是读取 HTML 文档, 并以网页的形式显示出它们

## 基础概念

### 块级元素

即 (block-level content), 此类标签因会在创建时使用一个区块而得名, 总是开始在新的行/列上, 占据父容器的整个水平空间。

```html
<div>
  <p>This the first paragraph.</p>
  <p>This is the second paragraph.</p>
</div>
```

### 行内元素

即 (inline-level content), 此类标签会按照文本基线进行对齐显示, 默认情况下, 大多数文本、替换元素以及生成的内容都是行内的。

```html
<p>
  This span is an <span class="highlight">inline-level element</span>; its
  background has been colored to display both the beginning and end of the
  element's influence.
</p>
```

### 行内块元素

即 (inline-block content), 是行内元素和块级元素的结合体, 既可以设置宽高又可以和其他行内元素在同一行显示。

- 可以设置 `width`、`height`、`margin`、`padding` 等属性
- 与其他行内元素或行内块元素水平排列
- 常见的行内块元素: `<img>`、`<input>`、`<button>`、`<select>` 等

```html
<div style="background: #f0f0f0; padding: 10px;">
  <span style="display: inline-block; width: 100px; height: 50px; background: #4CAF50; color: white; text-align: center; line-height: 50px;">块1</span>
  <span style="display: inline-block; width: 100px; height: 50px; background: #2196F3; color: white; text-align: center; line-height: 50px;">块2</span>
  <span style="display: inline-block; width: 100px; height: 50px; background: #FF9800; color: white; text-align: center; line-height: 50px;">块3</span>
</div>
```

### 元素 (Element)

即 (element), 从开始标签到结束标签之间的所有内容都称为一个元素, 元素可以包含文本、其他元素或为空。

- **包含内容的元素:** 由开始标签、内容和结束标签组成
- **空元素:** 没有内容, 只有开始标签 (如 `<br>`、`<img>`、`<input>` 等)
- **HTML 元素** 这个词通常指的是开始标签到结束标签之间的所有代码

```html
<!-- 包含内容的元素 -->
<p>这是一个段落元素</p>
<div>这是一个包含其他内容的元素</div>

<!-- 空元素 -->
<br>
<img src="image.jpg" alt="图片">
<input type="text">
```

### 标签 (Tag)

即 (tag), 标签是 HTML 的基本组成单位, 标签通常成对出现, 但也有一些是自闭合标签。

- **开始标签:** 元素的起始标记, 如 `<p>`
- **结束标签:** 元素的结束标记, 如 `</p>`
- **自闭合标签:** 无需结束标签, 如 `<br>`、`<img>`、`<input>` 等
- **标签名不区分大小写**, 但建议使用小写

```html
<!-- 成对标签 -->
<p>段落内容</p>
<div>容器内容</div>

<!-- 自闭合标签 -->
<br>
<img src="image.jpg" alt="图片">
<input type="text">
<meta charset="UTF-8">
```

### 属性 (Attribute)

即 (attribute), 属性提供关于 HTML 元素的附加信息, 属性在开始标签中定义, 以名值对的形式出现。

- **属性名:** 定义属性的名称 (如 `href`、`src`、`class` 等)
- **属性值:** 定义属性的值, 建议使用引号包裹
- **布尔属性:** 只有属性名, 没有属性值 (如 `disabled`、`required`、`checked` 等)
- **自定义属性:** 以 `data-` 开头, 用于存储自定义数据

```html
<!-- 基本属性 -->
<a href="https://www.example.com">链接</a>
<img src="image.jpg" alt="图片描述">
<input type="text" placeholder="请输入内容">

<!-- 布尔属性 -->
<input type="text" disabled>
<input type="text" required>
<input type="checkbox" checked>

<!-- 自定义属性 -->
<div data-id="123" data-name="test">自定义数据</div>
```

### 嵌套 (Nesting)

即 (nesting), 元素可以包含其他元素, 形成嵌套关系, 嵌套时要注意标签的闭合顺序。

- **父元素:** 包含其他元素的元素
- **子元素:** 被其他元素包含的元素
- **兄弟元素:** 具有相同父元素的元素
- **嵌套顺序:** 内层标签应该先闭合, 再闭合外层标签

```html
<!-- 正确的嵌套 -->
<div>
  <p>段落内容</p>
  <ul>
    <li>列表项1</li>
    <li>列表项2</li>
  </ul>
</div>

<!-- 错误的嵌套 (交叉嵌套) -->
<!-- <div><p>错误嵌套</div></p> -->
```

### 语义化 (Semantics)

即 (semantics), 语义化是指使用具有明确含义的标签来构建网页结构, 而不是单纯使用 `<div>` 和 `<span>` 来布局。

- **好处:** 提升可访问性、有利于 SEO、代码更易读和维护
- **常用语义化标签:** `<header>`、`<footer>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>` 等
- **对比:** 使用 `<div class="header">` 不如使用 `<header>` 语义明确

```html
<!-- 非语义化 -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="content">...</div>
<div class="footer">...</div>

<!-- 语义化 -->
<header>
  <nav>...</nav>
</header>
<main>...</main>
<footer>...</footer>
```

### 文档流 (Document Flow)

即 (document flow), 元素在页面中的排列方式, 主要分为正常文档流和脱离文档流两种情况。

- **正常文档流:** 块级元素垂直排列, 行内元素水平排列
- **浮动 (float):** 元素脱离正常文档流, 向左或向右浮动
- **定位 (position):** 元素通过 `position` 属性脱离文档流或进行精确定位

```html
<!-- 正常文档流 -->
<div>块1</div>
<div>块2</div>
<div>块3</div>

<!-- 浮动 -->
<div style="float: left; width: 100px; height: 100px; background: #4CAF50;">浮动1</div>
<div style="float: left; width: 100px; height: 100px; background: #2196F3;">浮动2</div>

<!-- 定位 -->
<div style="position: absolute; top: 10px; left: 10px; background: #FF9800;">绝对定位</div>
```

---

## 标签分类导航

### 基础标签 (basic-tags) [[basic-tags]]

**作用:** 定义 HTML 文档的基本结构和元数据
- 声明文档类型和编码格式
- 链接外部资源（CSS、图标等）
- 设置页面标题和描述

### 文本标签 (text-tags) [[text-tags]]

**作用:** 定义文本内容的结构和样式
- 创建标题层级（h1-h6）
- 定义段落和文本格式
- 强调重要文本内容

### 链接与媒体标签 (link-and-media-tags) [[link-and-media-tags]]

**作用:** 创建超链接和嵌入多媒体内容
- 链接到其他页面或资源
- 嵌入图片、视频和音频
- 创建图片热区链接

### 列表标签 (list-tags) [[list-tags]]

**作用:** 创建有序和无序列表
- 展示项目清单
- 定义术语和描述
- 创建导航菜单

### 表格标签 (table-tags) [[table-tags]]

**作用:** 展示结构化数据
- 创建数据表格
- 定义表头和表尾
- 合并单元格

### 表单标签 (form-tags) [[form-tags]]

**作用:** 创建用户交互界面
- 收集用户输入数据
- 创建各种输入控件
- 验证和提交表单
- → 样式参考: [[css-box-model]]、[[css-visual]]

### 语义化标签 (semantic-tags) [[semantic-tags]]

**作用:** 定义页面结构和内容区域
- 明确页面头部、底部和导航
- 划分内容区块
- 提升可访问性和 SEO
- → 布局参考: [[css-layout]]、[[css-responsive]]

### 其他标签 (other-tags) [[other-tags]]

**作用:** 提供特殊功能和增强内容
- 折叠展开内容
- 展示图片和说明
- 显示进度和度量
- → 响应式参考: [[css-responsive]]

---

## CSS 学习

> HTML 负责结构, CSS 负责样式, JS 负责行为

### CSS 学习笔记 (css-learning) [[css-learning]]

**作用:** 层叠样式表, 控制网页的视觉表现和布局
- CSS 选择器、盒模型、视觉属性
- Flex / Grid 布局、响应式设计
- 动画效果、CSS 工程化
- → 综合示例: `css-learning/Learning/html-css-combo.html`

---

## 常见问题

### 常用的浏览器有哪些?

IE, Edge, Firefox, Chrome, Safari, Opera 六大浏览器

### 常用的浏览器对应的内核是?

- IE (Trident) -- 猎豹安全, 360, 百度浏览器等
- Firefox (Gecko)
- Safari (Webkit)
- Chrome / Opera (Blink) -- Blink 其实是 WebKit 内核的分支

### Web 标准的构成

> 最佳体验方案: 三种文件相分离 (即结构, 样式, 行为相分离)

| 标准 | 说明 |
| :--- | :--- |
| 结构 (Structure) | 结构用于对网页元素进行整理和分类, 现阶段主要学的是 HTML |
| 表现 (Presentation) | 表现用于设置网页元素的版式, 颜色, 大小等外观样式, 主要指的是 CSS |
| 行为 (Behavior) | 行为是指网页模型的定义以及交互的编写, 现阶段主要是 JS |

### 一个完整的 HTML 文档应有哪些内容?

- `<!DOCTYPE html>` 声明为 HTML5 文档
- `<html>` 元素是 HTML 页面的根元素
- `<head>` 元素包含了文档的元（meta）数据, 如 `<meta charset="utf-8">` 定义网页编码格式为 utf-8
- `<title>` 元素描述了文档的标题
- `<body>` 元素包含了可见的页面内容
- `<h1>` 元素定义一个大标题
- `<p>` 元素定义一个段落
