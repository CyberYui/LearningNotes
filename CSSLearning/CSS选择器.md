# CSS 选择器

> 选择器用于指定要应用样式的 HTML 元素, 是 CSS 的核心概念

## 基础概念

即 (selector), 选择器是 CSS 规则的左侧部分, 用于匹配 HTML 元素。CSS 提供了多种选择器类型, 可以精确地选择需要样式化的元素。

选择器的 **常用度** 决定了内容的详细程度:
- **常用**: 完整示例 + 详细说明
- **中等**: 简要示例 + 概括说明
- **少用**: 仅语法说明

## 基础选择器 (常用)

### 通用选择器

即 (universal selector), 使用 `*` 匹配页面中的所有元素, 常用于重置样式。

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

### 元素选择器

即 (type selector), 使用元素名称匹配所有该类型的元素。

```html
<p>段落1</p>
<p>段落2</p>
```

```css
p {
  color: #333;
  line-height: 1.6;
}
```

### 类选择器

即 (class selector), 使用 `.classname` 匹配具有指定 class 属性的元素。**最常用** 的选择器之一。

- 一个元素可以有多个 class, 用空格分隔
- 同一个 class 可以被多个元素使用
- 类名应使用有意义的命名, 如 `.btn`、`.nav-item`

```html
<button class="btn">普通按钮</button>
<button class="btn btn-primary">主要按钮</button>
<p class="text-muted">次要文本</p>
```

```css
.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.text-muted {
  color: #6c757d;
}
```

### ID 选择器

即 (ID selector), 使用 `#idname` 匹配具有指定 id 属性的元素。

- 一个页面中 id 应该是唯一的
- ID 选择器优先级高于类选择器
- 不推荐过度使用 ID 选择器 (优先级难以管理)

```html
<header id="main-header">网站头部</header>
<section id="intro">介绍部分</section>
```

```css
#main-header {
  background-color: #333;
  color: white;
  padding: 20px;
}

#intro {
  padding: 40px;
  text-align: center;
}
```

## 组合选择器 (常用)

### 后代选择器

即 (descendant selector), 使用空格分隔, 匹配指定元素的所有后代元素 (包括子元素、孙元素等)。

```html
<nav class="main-nav">
  <ul>
    <li><a href="#">首页</a></li>
    <li><a href="#">关于</a></li>
  </ul>
</nav>
```

```css
/* 选择 .main-nav 内部的所有 <a> 元素 */
.main-nav a {
  color: #007bff;
  text-decoration: none;
}
```

### 子选择器

即 (child selector), 使用 `>` 分隔, 仅匹配指定元素的直接子元素。

```html
<ul class="menu">
  <li>菜单1
    <ul class="submenu">
      <li>子菜单1</li>
    </ul>
  </li>
  <li>菜单2</li>
</ul>
```

```css
/* 仅选择 .menu 的直接子元素 <li>, 不影响 .submenu 中的 <li> */
.menu > li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
```

### 相邻兄弟选择器

即 (adjacent sibling selector), 使用 `+` 分隔, 匹配紧接在指定元素之后的同级元素。

```html
<h2>标题</h2>
<p>这是紧接在标题后的段落</p>
<p>这是第二个段落</p>
```

```css
/* 仅选择紧接在 <h2> 后的第一个 <p> */
h2 + p {
  font-size: 1.2em;
  color: #666;
}
```

### 通用兄弟选择器

即 (general sibling selector), 使用 `~` 分隔, 匹配指定元素之后的所有同级元素。

```html
<h2>标题</h2>
<p>段落1</p>
<p>段落2</p>
<p>段落3</p>
```

```css
/* 选择 <h2> 之后的所有 <p> 兄弟元素 */
h2 ~ p {
  margin-left: 20px;
}
```

## 属性选择器 (中等)

即 (attribute selector), 根据元素的属性及其值来选择元素。

```html
<input type="text" placeholder="用户名">
<input type="password" placeholder="密码">
<input type="email" placeholder="邮箱">
<a href="https://example.com">外部链接</a>
<a href="/about">内部链接</a>
```

```css
/* 选择 type="text" 的元素 */
[type="text"] {
  border: 1px solid #ccc;
}

/* 选择 type 属性以 "pass" 开头的元素 */
[type^="pass"] {
  border-color: #ff9800;
}

/* 选择 href 属性以 ".pdf" 结尾的元素 */
[href$=".pdf"]::after {
  content: " (PDF)";
  font-size: 0.8em;
  color: #666;
}

/* 选择 href 属性包含 "https" 的元素 (外部链接) */
[href*="https"] {
  color: #d63384;
}
```

## 伪类选择器 (常用)

即 (pseudo-class selector), 用于选择元素的特定状态或位置。

### 状态伪类

```html
<a href="#">链接</a>
<input type="text" placeholder="输入内容">
<button>按钮</button>
```

```css
/* 未访问的链接 */
a:link { color: blue; }

/* 已访问的链接 */
a:visited { color: purple; }

/* 鼠标悬停 */
a:hover { color: red; text-decoration: underline; }

/* 点击瞬间 */
a:active { color: orange; }

/* 获得焦点时 */
input:focus {
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

/* 禁用状态 */
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* 选中状态 (checkbox/radio) */
input:checked + label {
  font-weight: bold;
}
```

### 结构伪类

```html
<ul>
  <li>第1项</li>
  <li>第2项</li>
  <li>第3项</li>
  <li>第4项</li>
  <li>第5项</li>
</ul>
```

```css
/* 第一个子元素 */
li:first-child {
  font-weight: bold;
}

/* 最后一个子元素 */
li:last-child {
  border-bottom: none;
}

/* 第 n 个子元素 */
li:nth-child(2) {
  color: red;
}

/* 偶数个子元素 */
li:nth-child(even) {
  background-color: #f8f9fa;
}

/* 奇数个子元素 */
li:nth-child(odd) {
  background-color: #fff;
}

/* 第 3 个及之后的元素 */
li:nth-child(n+3) {
  font-size: 0.9em;
}
```

### 否定伪类

```html
<ul class="list">
  <li class="item">项目1</li>
  <li class="item active">项目2</li>
  <li class="item">项目3</li>
  <li class="item">项目4</li>
</ul>
```

```css
/* 选择没有 .active 类的 <li> 元素 */
.list li:not(.active) {
  opacity: 0.7;
}
```

## 伪元素选择器 (中等)

即 (pseudo-element selector), 用于选择元素的特定部分, 而不是整个元素。使用 `::` 语法 (CSS3 规范)。

```html
<p class="article">这是一段很长的文章内容, 首字会下沉显示。</p>
<div class="box">盒子内容</div>
```

```css
/* 首字下沉 */
.article::first-letter {
  font-size: 3em;
  float: left;
  margin-right: 8px;
  color: #007bff;
}

/* 首行样式 */
.article::first-line {
  font-weight: bold;
}

/* 在元素内容之前插入内容 */
.box::before {
  content: "★ ";
  color: gold;
}

/* 在元素内容之后插入内容 */
.box::after {
  content: " ✓";
  color: green;
}

/* 自定义占位符样式 */
input::placeholder {
  color: #aaa;
  font-style: italic;
}

/* 选中文本的样式 */
::selection {
  background-color: #007bff;
  color: white;
}
```

## 选择器优先级 (重要)

即 (specificity), 当多个选择器作用于同一元素时, 优先级高的规则会覆盖优先级低的规则。

### 优先级计算规则

| 优先级 | 选择器类型 | 示例 |
|--------|-----------|------|
| 最高 | 内联样式 | `style="color: red;"` |
| 高 | ID 选择器 | `#header { }` |
| 中 | 类选择器、属性选择器、伪类 | `.nav { }`、`[type="text"] { }`、`:hover { }` |
| 低 | 元素选择器、伪元素 | `p { }`、`::before { }` |
| 最低 | 通用选择器 | `* { }` |

### 计算示例

```css
p                    /* 优先级: 0,0,0,1 */
.text                 /* 优先级: 0,0,1,0 */
#main .text           /* 优先级: 0,1,0,1 */
.container p.text     /* 优先级: 0,0,2,1 */
#sidebar .item.active /* 优先级: 0,1,2,0 */
```

- 优先级相同时, 后定义的规则覆盖先定义的规则
- 使用 `!important` 可以强制提升优先级, 但应避免滥用
