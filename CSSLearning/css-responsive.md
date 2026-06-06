# CSS 响应式设计

> 使网页在不同设备和屏幕尺寸下都能良好显示

## 基础概念

即 (responsive design), 响应式设计是一种网页设计方法, 使网页能够自动适应不同设备和屏幕尺寸, 提供最佳的用户体验。

核心思想: **一次设计, 到处适用** — 同一份代码在手机、平板、桌面电脑上都能正常显示。

## 视口 Meta 标签 (重要)

即 (viewport meta tag), 与 [[HtmlLearning#basic-tags]] 中的 `<meta>` 标签配合使用, 控制视口的宽度和缩放。

```html
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

**属性说明:**
- `width=device-width`: 视口宽度等于设备宽度
- `initial-scale=1.0`: 初始缩放比例为 1
- `maximum-scale=1.0`: 最大缩放比例 (可省略)
- `user-scalable=no`: 禁止用户缩放 (不推荐, 影响可访问性)

这是响应式设计的第一步, 没有这个标签, 移动端会按桌面宽度渲染, 然后缩小显示, 导致文字很小。

## 媒体查询 (常用)

即 (media queries), 允许根据设备的特性 (如屏幕宽度) 应用不同的样式, 是响应式设计的核心技术。

### 基本语法

```css
@media 媒体类型 and (媒体特性) {
  /* 满足条件时应用的 CSS */
}

/* 示例 */
@media screen and (max-width: 768px) {
  .container {
    padding: 10px;
  }
}
```

### 常用媒体类型

| 类型 | 说明 |
|------|------|
| `all` | 所有设备 (默认) |
| `screen` | 屏幕设备 |
| `print` | 打印设备 |
| `speech` | 语音合成器 |

### 常用媒体特性

```css
/* 宽度相关 */
@media (max-width: 768px) { }      /* 最大宽度 768px */
@media (min-width: 768px) { }      /* 最小宽度 768px */
@media (min-width: 768px) and (max-width: 1024px) { }  /* 范围 */

/* 设备宽度 */
@media (max-device-width: 480px) { }

/* 屏幕方向 */
@media (orientation: portrait) { }   /* 竖屏 */
@media (orientation: landscape) { }  /* 横屏 */

/* 高分辨率 */
@media (-webkit-min-device-pixel-ratio: 2),
       (min-resolution: 192dpi) { }
```

### 断点设置

即 (breakpoints), 断点是响应式设计中的关键宽度值, 当屏幕宽度达到断点时, 布局会发生变化。

**常用断点 (移动优先):**

```css
/* 基础样式: 手机 (默认) */
.container { padding: 10px; }

/* 平板 (≥768px) */
@media (min-width: 768px) {
  .container { padding: 20px; }
}

/* 桌面 (≥1024px) */
@media (min-width: 1024px) {
  .container { padding: 30px; max-width: 1200px; }
}

/* 大桌面 (≥1440px) */
@media (min-width: 1440px) {
  .container { max-width: 1400px; }
}
```

### 移动优先 vs 桌面优先

**移动优先 (推荐):** 先编写手机样式, 再用 `min-width` 为大屏幕添加增强样式。

```css
/* 移动优先 */
.grid {
  display: grid;
  grid-template-columns: 1fr;    /* 手机: 单列 */
}

@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }  /* 平板: 双列 */
}

@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }  /* 桌面: 三列 */
}
```

**桌面优先:** 先编写桌面样式, 再用 `max-width` 为小屏幕覆盖样式。

```css
/* 桌面优先 */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 桌面: 三列 */
}

@media (max-width: 1023px) {
  .grid { grid-template-columns: repeat(2, 1fr); }  /* 平板: 双列 */
}

@media (max-width: 767px) {
  .grid { grid-template-columns: 1fr; }          /* 手机: 单列 */
}
```

## 响应式单位 (常用)

即 (responsive units), 使用相对单位可以让元素根据视口或父元素自动缩放。

### rem (Root EM)

相对于根元素 (`<html>`) 的字号, 最常用 的响应式单位。

```css
html {
  font-size: 16px;    /* 基准字号 */
}

h1 {
  font-size: 2rem;    /* 32px (2 × 16px) */
}

p {
  font-size: 1rem;    /* 16px */
  margin-bottom: 1rem; /* 16px */
}

/* 响应式基准字号 */
@media (max-width: 768px) {
  html { font-size: 14px; }  /* 所有 rem 值自动缩小 */
}
```

### em (Element EM)

相对于当前元素的字号, 常用于 `padding`、`margin` 等需要随字号变化的属性。

```css
.btn {
  font-size: 16px;
  padding: 0.5em 1em;    /* 8px 16px */
}

.btn-large {
  font-size: 24px;
  padding: 0.5em 1em;    /* 12px 24px (自动随字号缩放) */
}
```

### vw / vh (Viewport Width/Height)

相对于视口的宽度/高度, 1vw = 视口宽度的 1%。

```css
.hero {
  height: 100vh;       /* 占满整个视口高度 */
  width: 100vw;        /* 占满整个视口宽度 */
}

.sidebar {
  width: 25vw;         /* 视口宽度的 25% */
}

/* 注意: vw 包含滚动条宽度, 可能导致横向滚动 */
.full-width {
  width: 100vw;
  margin-left: calc(-50vw + 50%);  /* 居中处理 */
}
```

### % (百分比)

相对于父元素的对应属性。

```css
.container {
  width: 80%;          /* 父元素宽度的 80% */
  max-width: 1200px;   /* 最大宽度限制 */
  margin: 0 auto;      /* 水平居中 */
}

.column {
  width: 50%;          /* 父元素宽度的 50% */
}
```

## 响应式图片 (中等)

即 (responsive images), 与 [[HtmlLearning#link-and-media-tags]] 中的 `<img>` 和 `<picture>` 标签配合使用。

### 基本响应式图片

```css
img {
  max-width: 100%;     /* 不超过父元素宽度 */
  height: auto;        /* 保持宽高比 */
  display: block;      /* 消除底部间隙 */
}
```

### 使用 picture 元素

```html
<picture>
  <!-- 大屏幕 -->
  <source media="(min-width: 1024px)" srcset="large.jpg">
  <!-- 中等屏幕 -->
  <source media="(min-width: 768px)" srcset="medium.jpg">
  <!-- 默认 (小屏幕) -->
  <img src="small.jpg" alt="响应式图片">
</picture>
```

### 背景图片响应式

```css
.hero {
  background-image: url("hero-small.jpg");
  background-size: cover;
  background-position: center;
}

@media (min-width: 768px) {
  .hero { background-image: url("hero-medium.jpg"); }
}

@media (min-width: 1200px) {
  .hero { background-image: url("hero-large.jpg"); }
}
```

## 响应式表格 (了解)

即 (responsive tables), 在小屏幕上表格可能溢出容器, 需要特殊处理。

```css
/* 方法1: 水平滚动 */
.table-wrapper {
  overflow-x: auto;
}

/* 方法2: 隐藏部分列 */
@media (max-width: 768px) {
  .hide-mobile {
    display: none;
  }
}

/* 方法3: 转换为卡片布局 */
@media (max-width: 768px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }

  td {
    padding: 8px 8px 8px 50%;
    position: relative;
  }

  td::before {
    content: attr(data-label);
    position: absolute;
    left: 8px;
    font-weight: bold;
  }
}
```

## 响应式排版 (中等)

即 (responsive typography), 文字大小和行距应随屏幕尺寸调整。

```css
/* 使用 clamp() 实现流体排版 */
h1 {
  font-size: clamp(1.5rem, 4vw, 3rem);
  /* 最小 1.5rem, 理想 4vw, 最大 3rem */
}

p {
  font-size: clamp(1rem, 2vw, 1.25rem);
  line-height: 1.6;
}

/* 使用媒体查询 */
body {
  font-size: 14px;
  line-height: 1.5;
}

@media (min-width: 768px) {
  body {
    font-size: 16px;
    line-height: 1.6;
  }
}

@media (min-width: 1200px) {
  body {
    font-size: 18px;
    line-height: 1.7;
  }
}
```
