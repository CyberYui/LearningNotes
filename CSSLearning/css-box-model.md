# CSS 盒模型

> 盒模型是 CSS 布局的基础, 理解盒模型对掌握页面布局至关重要

## 基础概念

即 (box model), 在 CSS 中, 每个 HTML 元素都可以看作是一个矩形的盒子, 这个盒子由四个部分组成, 从内到外依次是: **内容 (content) → 内边距 (padding) → 边框 (border) → 外边距 (margin)**。

盒模型是 CSS 布局的核心概念, 理解它对于:
- 控制元素大小和间距
- 实现精确的页面布局
- 解决样式问题

都至关重要。

```
┌─────────────────────────────────┐
│           margin (外边距)         │
│  ┌─────────────────────────────┐ │
│  │       border (边框)          │ │
│  │  ┌─────────────────────────┐│ │
│  │  │   padding (内边距)       ││ │
│  │  │  ┌─────────────────────┐││ │
│  │  │  │   content (内容)     │││ │
│  │  │  │                     │││ │
│  │  │  └─────────────────────┘││ │
│  │  └─────────────────────────┘│ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

## 盒模型组成 (常用)

### 内容区域 (Content)

即 (content area), 是盒子的核心部分, 包含元素的实际内容, 如文本、图片等。

- `width`: 设置内容区域的宽度
- `height`: 设置内容区域的高度
- `min-width` / `max-width`: 设置宽度的最小值和最大值
- `min-height` / `max-height`: 设置高度的最小值和最大值

```css
.box {
  width: 300px;
  height: 200px;
  background-color: #f0f0f0;
}
```

### 内边距 (Padding)

即 (padding), 是内容区域与边框之间的空间, 用于在内容和边框之间创建空白。

```css
/* 四个方向的内边距 */
.box {
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 10px;
  padding-left: 20px;
}

/* 简写: 上 右 下 左 (顺时针) */
.box { padding: 10px 20px 10px 20px; }

/* 简写: 上下 左右 */
.box { padding: 10px 20px; }

/* 简写: 四个方向相同 */
.box { padding: 15px; }
```

### 边框 (Border)

即 (border), 是内边距和外边距之间的边界线。

```css
.box {
  border-width: 2px;
  border-style: solid;   /* solid | dashed | dotted | double | none */
  border-color: #333;
}

/* 简写 */
.box { border: 2px solid #333; }

/* 单独的边框 */
.box {
  border-top: 1px solid #ddd;
  border-bottom: 2px solid #333;
}

/* 圆角 */
.box {
  border-radius: 8px;        /* 四个角 */
  border-radius: 8px 4px;    /* 左上右下 右上左下 */
  border-radius: 50%;        /* 圆形 */
}
```

### 外边距 (Margin)

即 (margin), 是边框外部的空间, 用于在元素之间创建距离。

```css
/* 四个方向的外边距 */
.box {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 10px;
  margin-left: 20px;
}

/* 简写: 上 右 下 左 (顺时针) */
.box { margin: 10px 20px 10px 20px; }

/* 简写: 上下 左右 */
.box { margin: 10px 20px; }

/* 简写: 四个方向相同 */
.box { margin: 15px; }

/* 水平居中 (块级元素) */
.box {
  width: 800px;
  margin: 0 auto;    /* 上下 0, 左右自动 */
}

/* 外边距可以设为负值 */
.overlap {
  margin-top: -20px;  /* 向上重叠 */
}
```

## box-sizing 属性 (重要)

即 (box-sizing), 这个属性决定了 `width` 和 `height` 的计算方式, 是 CSS 盒模型中最重要的属性之一。

### content-box (默认值)

即 (content-box), `width` 和 `height` 仅包含内容区域, 不包含 padding 和 border。

```css
/* 默认值 */
.box {
  box-sizing: content-box;
  width: 300px;
  padding: 20px;
  border: 2px solid #333;
  /* 实际占用宽度: 300 + 20*2 + 2*2 = 344px */
}
```

### border-box (推荐)

即 (border-box), `width` 和 `height` 包含内容区域、padding 和 border, 设置宽度后不需要再计算 padding 和 border。

```css
/* 推荐值 */
.box {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 2px solid #333;
  /* 实际占用宽度: 300px (内容区域自动缩小为 300 - 20*2 - 2*2 = 256px) */
}
```

### 最佳实践

在实际开发中, 推荐全局设置 `box-sizing: border-box`, 这样可以更直观地控制元素大小:

```css
/* 全局设置 */
*, *::before, *::after {
  box-sizing: border-box;
}
```

### 示例对比示例

```html
<div class="container">
  <div class="box content-box">content-box</div>
  <div class="box border-box">border-box</div>
</div>
```

```css
.container {
  width: 300px;
}

.box {
  width: 100%;
  padding: 20px;
  border: 5px solid #007bff;
  margin-bottom: 20px;
  background-color: #e7f3ff;
}

.content-box {
  box-sizing: content-box;
  /* 实际宽度: 300 + 20*2 + 5*2 = 350px (会溢出容器) */
}

.border-box {
  box-sizing: border-box;
  /* 实际宽度: 300px (不会溢出容器) */
}
```

## 标准盒模型与 IE 盒模型 (了解)

即 (standard vs quirks mode), 在早期的 IE 浏览器中, 盒模型的计算方式与标准不同。

- **标准盒模型 (content-box):** width/height 仅包含内容区域, 这是 W3C 标准
- **IE 盒模型 (border-box):** width/height 包含内容、padding 和 border

现代浏览器默认使用标准盒模型, 但通过设置 `box-sizing: border-box` 可以切换到 IE 盒模型的行为。如今 `border-box` 已成为推荐的盒模型设置。

## 外边距合并 (重要)

即 (margin collapsing / margin collapse), 当两个垂直相邻的元素都设置了外边距时, 它们之间的外边距不会叠加, 而是取较大的那个值。

### 相邻元素的外边距合并

```html
<div class="box1">盒子1</div>
<div class="box2">盒子2</div>
```

```css
.box1 {
  margin-bottom: 30px;
}

.box2 {
  margin-top: 20px;
}

/* 两个盒子之间的实际距离: 30px (不是 30 + 20 = 50px) */
```

### 父元素与子元素的外边距合并

```html
<div class="parent">
  <div class="child">子元素</div>
</div>
```

```css
.parent {
  margin-top: 20px;
}

.child {
  margin-top: 30px;
}

/* 如果父元素没有 border 或 padding, 子元素的 margin-top 会"穿透"父元素 */
/* 实际效果: 父元素距离上方 30px (取较大值) */
```

### 防止外边距合并

```css
/* 方法1: 给父元素添加 border */
.parent {
  border-top: 1px solid transparent;
}

/* 方法2: 给父元素添加 padding */
.parent {
  padding-top: 1px;
}

/* 方法3: 给父元素设置 overflow (触发 BFC) */
.parent {
  overflow: hidden;
}
```

## 盒模型实际应用

### 按钮样式

```html
<button class="btn">点击按钮</button>
```

```css
.btn {
  box-sizing: border-box;
  display: inline-block;
  padding: 10px 24px;
  border: 2px solid #007bff;
  border-radius: 6px;
  background-color: #007bff;
  color: white;
  font-size: 16px;
  cursor: pointer;
}

.btn:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}
```

### 卡片样式

```html
<div class="card">
  <h3>卡片标题</h3>
  <p>卡片内容</p>
</div>
```

```css
.card {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 16px;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```
