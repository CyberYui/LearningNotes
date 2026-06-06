# CSS 布局

> 控制元素在页面中的位置和排列方式, CSS 布局是前端开发的核心技能

## 基础概念

即 (layout), CSS 布局是指控制元素在页面中的位置、大小和排列方式。在深入各种布局技术之前, 需要先理解 `display` 属性和 **格式化上下文 (Formatting Context)**。

### display 属性

即 (display property), 决定了元素的显示类型和布局方式。

| 值 | 说明 |
|----|------|
| `block` | 块级元素: 独占一行, 可设置宽高 |
| `inline` | 行内元素: 不独占一行, 不可设置宽高 |
| `inline-block` | 行内块元素: 不独占一行, 可设置宽高 |
| `flex` | Flex 容器: 子元素使用 Flex 布局 |
| `grid` | Grid 容器: 子元素使用 Grid 布局 |
| `none` | 隐藏元素 (不占据空间) |

```css
.block {
  display: block;
  width: 100%;       /* 块级元素可以设置宽高 */
  margin: 10px 0;    /* 上下外边距有效 */
}

.inline {
  display: inline;
  /* width 和 height 无效 */
  /* 上下 margin 和 padding 不影响布局 */
}

.inline-block {
  display: inline-block;
  width: 200px;      /* 可以设置宽高 */
  vertical-align: top; /* 顶部对齐 */
}
```

## Flex 布局 (最常用)

即 (Flexible Box), Flex 布局是一维布局模型, 用于在容器内排列子元素, 特别适合处理 **单行或单列** 的布局场景。

### Flex 容器属性

即 (flex container properties), 设置在父元素 (容器) 上的属性。

```css
.container {
  display: flex;  /* 启用 Flex 布局 */
}
```

#### flex-direction

指定主轴方向 (子元素的排列方向)。

```css
.container {
  flex-direction: row;            /* 水平, 从左到右 (默认) */
  flex-direction: row-reverse;    /* 水平, 从右到左 */
  flex-direction: column;         /* 垂直, 从上到下 */
  flex-direction: column-reverse; /* 垂直, 从下到上 */
}
```

#### justify-content

指定子元素在主轴上的对齐方式。

```css
.container {
  justify-content: flex-start;    /* 靠主轴起点 (默认) */
  justify-content: flex-end;      /* 靠主轴终点 */
  justify-content: center;        /* 居中 */
  justify-content: space-between; /* 两端对齐, 中间间隔相等 */
  justify-content: space-around;  /* 每个元素两侧间隔相等 */
  justify-content: space-evenly;  /* 所有间隔相等 */
}
```

#### align-items

指定子元素在交叉轴上的对齐方式。

```css
.container {
  align-items: stretch;     /* 拉伸填满 (默认) */
  align-items: flex-start;  /* 靠交叉轴起点 */
  align-items: flex-end;    /* 靠交叉轴终点 */
  align-items: center;      /* 居中 */
  align-items: baseline;    /* 基线对齐 */
}
```

#### flex-wrap

指定子元素是否换行。

```css
.container {
  flex-wrap: nowrap;    /* 不换行 (默认), 可能压缩子元素 */
  flex-wrap: wrap;      /* 换行 */
  flex-wrap: wrap-reverse; /* 换行, 反向 */
}
```

#### gap

指定子元素之间的间距。

```css
.container {
  gap: 16px;           /* 行和列间距相同 */
  row-gap: 16px;       /* 行间距 */
  column-gap: 24px;    /* 列间距 */
}
```

### Flex 项目属性

即 (flex item properties), 设置在子元素 (项目) 上的属性。

#### flex-grow

指定项目的放大比例。

```css
.item {
  flex-grow: 0;   /* 不放大 (默认) */
  flex-grow: 1;   /* 等比例放大填满剩余空间 */
  flex-grow: 2;   /* 放大比例为 2 */
}
```

#### flex-shrink

指定项目的缩小比例。

```css
.item {
  flex-shrink: 1;   /* 等比例缩小 (默认) */
  flex-shrink: 0;   /* 不缩小 */
  flex-shrink: 2;   /* 缩小比例为 2 */
}
```

#### flex-basis

指定项目在分配多余空间之前的初始大小。

```css
.item {
  flex-basis: auto;    /* 默认, 由内容决定 */
  flex-basis: 200px;   /* 初始宽度 200px */
  flex-basis: 25%;     /* 初始宽度 25% */
}
```

#### flex 简写

```css
.item {
  flex: 0 1 auto;    /* 默认值: 不放大, 可缩小, 基础大小自动 */
  flex: 1;           /* 等价于 flex: 1 1 0% */
  flex: auto;        /* 等价于 flex: 1 1 auto */
  flex: none;        /* 等价于 flex: 0 0 auto */
}
```

#### align-self

允许单个项目覆盖容器的 align-items 设置。

```css
.item {
  align-self: auto;       /* 继承容器的 align-items (默认) */
  align-self: center;     /* 居中 */
  align-self: flex-end;   /* 靠交叉轴终点 */
}
```

#### order

指定项目的排列顺序。

```css
.item {
  order: 0;    /* 默认值 */
  order: -1;   /* 排在最前面 */
  order: 1;    /* 排在最后面 */
}
```

### Flex 布局示例

详细示例见 [[Learning/flex-layout.html]]

```html
<!-- 导航栏 -->
<nav class="navbar">
  <div class="logo">Logo</div>
  <ul class="nav-links">
    <li><a href="#">首页</a></li>
    <li><a href="#">产品</a></li>
    <li><a href="#">关于</a></li>
  </ul>
  <div class="actions">
    <button>登录</button>
  </div>
</nav>
```

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background-color: #333;
}

.nav-links {
  display: flex;
  gap: 24px;
  list-style: none;
}

.nav-links a {
  color: white;
  text-decoration: none;
}
```

## Grid 布局 (常用)

即 (Grid Layout), Grid 布局是二维布局模型, 可以同时处理行和列, 适合复杂的页面布局。

### Grid 容器属性

即 (grid container properties), 设置在父元素 (容器) 上的属性。

```css
.container {
  display: grid;  /* 启用 Grid 布局 */
}
```

#### grid-template-columns / grid-template-rows

定义网格的列和行。

```css
.container {
  /* 固定宽度 */
  grid-template-columns: 200px 200px 200px;

  /* 百分比 */
  grid-template-columns: 1fr 2fr 1fr;

  /* 使用 repeat() 函数 */
  grid-template-columns: repeat(3, 1fr);

  /* 自动填充, 最小 200px */
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

  /* 混合使用 */
  grid-template-columns: 200px 1fr auto;
  grid-template-rows: 60px 1fr 80px;
}
```

#### gap

指定网格项之间的间距。

```css
.container {
  gap: 16px;           /* 行和列间距相同 */
  row-gap: 16px;       /* 行间距 */
  column-gap: 24px;    /* 列间距 */
}
```

#### justify-items / align-items

指定网格项在单元格内的对齐方式。

```css
.container {
  justify-items: start;    /* 靠单元格起点 */
  justify-items: end;      /* 靠单元格终点 */
  justify-items: center;    /* 居中 */
  justify-items: stretch;  /* 拉伸填满 (默认) */

  align-items: start;
  align-items: end;
  align-items: center;
  align-items: stretch;
}

/* 同时设置水平和垂直对齐 */
.container {
  place-items: center;    /* 水平垂直都居中 */
}
```

#### grid-template-areas

通过命名区域来布局。

```css
.container {
  grid-template-columns: 200px 1fr;
  grid-template-rows: 60px 1fr 80px;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }
```

### Grid 项目属性

即 (grid item properties), 设置在子元素 (项目) 上的属性。

#### grid-column / grid-row

指定项目在网格中的位置。

```css
.item {
  grid-column: 1 / 3;      /* 从第 1 条线到第 3 条线 (占 2 列) */
  grid-column: span 2;    /* 占 2 列 */
  grid-row: 1 / 2;         /* 占第 1 行 */
  grid-row: span 3;        /* 占 3 行 */
}
```

#### grid-area

指定项目在命名区域中的位置, 或同时指定行列。

```css
.item {
  grid-area: 1 / 1 / 3 / 3;  /* 起始行 / 起始列 / 结束行 / 结束列 */
  grid-area: header;          /* 使用命名区域 */
}
```

#### justify-self / align-self

指定单个项目在单元格内的对齐方式。

```css
.item {
  justify-self: center;
  align-self: center;
  place-self: center;
}
```

### Grid 布局示例

详细示例见 [[Learning/grid-layout.html]]

```html
<!-- 页面整体布局 -->
<div class="page">
  <header class="header">头部</header>
  <nav class="sidebar">侧边栏</nav>
  <main class="main">主内容</main>
  <footer class="footer">页脚</footer>
</div>
```

```css
.page {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: 60px 1fr 80px;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  min-height: 100vh;
}

.header  { grid-area: header;  background: #333; color: white; }
.sidebar { grid-area: sidebar; background: #f5f5f5; }
.main    { grid-area: main;    padding: 20px; }
.footer  { grid-area: footer;  background: #333; color: white; }
```

## 定位 (常用)

即 (positioning), 通过 `position` 属性可以将元素放置在页面的特定位置。

### position 属性

| 值 | 说明 |
|----|------|
| `static` | 默认值, 正常文档流 |
| `relative` | 相对定位, 相对于自身原始位置 |
| `absolute` | 绝对定位, 相对于最近的已定位祖先元素 |
| `fixed` | 固定定位, 相对于视口 |
| `sticky` | 粘性定位, 在 relative 和 fixed 之间切换 |

### relative (相对定位)

即 (relative positioning), 元素相对于自身原始位置进行偏移, 不会脱离文档流。

```css
.box {
  position: relative;
  top: 10px;      /* 向下偏移 10px */
  left: 20px;     /* 向右偏移 20px */
  /* 原始位置仍然保留 */
}
```

### absolute (绝对定位)

即 (absolute positioning), 元素脱离文档流, 相对于最近的已定位祖先元素定位。

```css
.parent {
  position: relative;  /* 作为定位参考 */
}

.child {
  position: absolute;
  top: 10px;
  right: 10px;    /* 相对于 .parent 的右上角 */
}
```

### fixed (固定定位)

即 (fixed positioning), 元素脱离文档流, 相对于视口定位, 滚动时位置不变。

```css
.fixed-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;    /* 固定在视口右下角 */
  z-index: 1000;
}
```

### sticky (粘性定位)

即 (sticky positioning), 元素在滚动时会在 relative 和 fixed 之间切换。

```css
.sticky-header {
  position: sticky;
  top: 0;    /* 滚动到顶部时变为 fixed */
  z-index: 100;
}
```

### z-index

指定元素的堆叠顺序 (仅在定位元素上生效)。

```css
.box {
  position: absolute;
  z-index: 10;    /* 值越大, 越在上层 */
}
```

## 浮动 (了解)

即 (float), 浮动最初用于实现文字环绕图片的效果, 后来被用于布局, 现在已被 Flex 和 Grid 替代。

### float 属性

```css
img {
  float: left;     /* 向左浮动, 文字环绕其右侧 */
  float: right;    /* 向右浮动 */
  float: none;     /* 不浮动 (默认) */
}
```

### 清除浮动

即 (clear float), 浮动会导致父元素高度塌陷, 需要清除浮动。

```css
/* 方法1: 在浮动元素后添加空元素 */
.clear {
  clear: both;
}

/* 方法2: 使用伪元素 (推荐) */
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}

/* 方法3: 父元素设置 overflow */
.parent {
  overflow: hidden;  /* 或 auto */
}
```

## 多列布局 (少用)

即 (multi-column layout), 用于创建类似报纸的多列文本布局。

```css
.article {
  column-count: 3;              /* 分为 3 列 */
  column-gap: 40px;             /* 列间距 */
  column-rule: 1px solid #ddd;  /* 列分隔线 */
}
```
