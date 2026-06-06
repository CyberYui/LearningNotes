# CSS 视觉表现

> 控制元素的颜色、字体、背景、边框等视觉效果

## 基础概念

即 (visual properties), CSS 视觉表现属性用于控制元素的外观, 包括颜色、字体、文本样式、背景、边框和阴影等。这些属性不涉及布局, 只影响元素的视觉效果。

视觉属性大多可以继承, 因此可以在父元素上设置, 子元素会自动继承, 减少重复代码。

## 颜色表示 (常用)

即 (color values), CSS 提供了多种表示颜色的方式。

### 十六进制 (HEX)

最常用 的颜色表示方式, 使用 `#RRGGBB` 格式。

```css
.text {
  color: #333333;    /* 深灰色 */
  color: #007bff;    /* 蓝色 */
  color: #ff0000;    /* 红色 */
  color: #f00;       /* 红色简写 (等同于 #ff0000) */
}
```

### RGB / RGBA

使用红 (Red)、绿 (Green)、蓝 (Blue) 三原色表示, RGBA 增加了透明度通道。

```css
.text {
  color: rgb(51, 51, 51);       /* 深灰色 */
  color: rgba(0, 123, 255, 1);  /* 不透明蓝色 */
  color: rgba(0, 123, 255, 0.5); /* 半透明蓝色 */
}
```

### HSL / HSLA

使用色相 (Hue)、饱和度 (Saturation)、亮度 (Lightness) 表示, 更符合人类对颜色的感知。

```css
.text {
  color: hsl(210, 100%, 50%);      /* 蓝色 */
  color: hsla(210, 100%, 50%, 0.5); /* 半透明蓝色 */
  color: hsl(0, 100%, 50%);         /* 红色 */
}
```

### 颜色关键字

CSS 定义了一些颜色关键字, 但精确度不如数值表示。

```css
.text {
  color: red;
  color: blue;
  color: transparent;  /* 完全透明 */
}
```

## 字体属性 (常用)

即 (font properties), 用于控制文字的字体、大小、粗细、样式等。

### font-family

指定字体名称, 可以设置多个字体作为备选 (字体栈)。

```css
body {
  font-family: "Microsoft YaHei", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
}

/* 等宽字体 (代码) */
code {
  font-family: "Fira Code", "Consolas", "Monaco", monospace;
}
```

**常用字体分类:**
- **衬线体 (Serif):** Times New Roman, Georgia, 宋体
- **无衬线体 (Sans-serif):** Arial, Helvetica, Microsoft YaHei, 黑体
- **等宽字体 (Monospace):** Consolas, Monaco, Fira Code
- **手写体 (Cursive):** Comic Sans MS, 楷体

### font-size

指定字体大小, 常用单位:

```css
.text {
  font-size: 16px;    /* 像素 (最常用) */
  font-size: 1rem;    /* 相对于根元素 (推荐) */
  font-size: 1.2em;   /* 相对于父元素 */
  font-size: 100%;    /* 相对于父元素 */
}

/* 推荐: 在根元素设置基准字号 */
html {
  font-size: 16px;
}

h1 { font-size: 2.5rem; }   /* 40px */
h2 { font-size: 2rem; }     /* 32px */
h3 { font-size: 1.75rem; }  /* 28px */
p { font-size: 1rem; }      /* 16px */
small { font-size: 0.875rem; } /* 14px */
```

### font-weight

指定字体粗细。

```css
.text {
  font-weight: normal;    /* 正常 (400) */
  font-weight: bold;      /* 粗体 (700) */
  font-weight: lighter;   /* 相对于父元素更细 */
  font-weight: bolder;    /* 相对于父元素更粗 */
  font-weight: 100;       /* 极细 */
  font-weight: 400;       /* 正常 */
  font-weight: 700;       /* 粗体 */
  font-weight: 900;       /* 极粗 */
}
```

### font-style 和 font-variant

```css
.text {
  font-style: normal;     /* 正常 */
  font-style: italic;     /* 斜体 */
  font-style: oblique;    /* 倾斜 */

  font-variant: normal;   /* 正常 */
  font-variant: small-caps; /* 小型大写字母 */
}
```

### line-height

指定行高 (一行文字的高度)。

```css
body {
  line-height: 1.5;     /* 无单位, 相对于当前字号 (推荐) */
  line-height: 24px;    /* 固定值 */
  line-height: 150%;    /* 百分比 */
}
```

### font 简写

```css
/* 顺序: style variant weight size/line-height family */
.text {
  font: italic bold 16px/1.5 "Microsoft YaHei", sans-serif;
}

/* 最少需要 size 和 family */
.text {
  font: 16px "Microsoft YaHei", sans-serif;
}
```

## 文本属性 (常用)

即 (text properties), 用于控制文本的对齐、装饰、缩进等。

### text-align

指定文本的水平对齐方式。

```css
.text {
  text-align: left;     /* 左对齐 (默认) */
  text-align: right;    /* 右对齐 */
  text-align: center;   /* 居中 */
  text-align: justify;  /* 两端对齐 */
}
```

### text-decoration

指定文本的装饰线。

```css
.text {
  text-decoration: none;           /* 无装饰 (常用于去除链接下划线) */
  text-decoration: underline;      /* 下划线 */
  text-decoration: overline;       /* 上划线 */
  text-decoration: line-through;   /* 删除线 */
}

/* 简写: 可以指定颜色和样式 */
.text {
  text-decoration: underline wavy red; /* 红色波浪下划线 */
}
```

### text-indent

指定文本首行的缩进。

```css
p {
  text-indent: 2em;    /* 缩进两个字符 (中文排版常用) */
  text-indent: 20px;   /* 缩进 20px */
}
```

### letter-spacing 和 word-spacing

```css
.text {
  letter-spacing: 2px;   /* 字符间距 */
  word-spacing: 4px;     /* 单词间距 */
}
```

### white-space

指定如何处理空白字符和换行。

```css
.text {
  white-space: normal;    /* 默认, 合并空白, 自动换行 */
  white-space: nowrap;    /* 合并空白, 不换行 */
  white-space: pre;       /* 保留空白和换行 (类似 <pre>) */
  white-space: pre-wrap;  /* 保留空白, 允许换行 */
  white-space: pre-line;  /* 合并空白, 保留换行 */
}

/* 文本溢出省略号 */
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

### text-shadow

为文本添加阴影。

```css
.text {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  /* 水平偏移 垂直偏移 模糊半径 颜色 */

  /* 多重阴影 */
  text-shadow: 1px 1px 2px #333, 2px 2px 4px #666;
}
```

## 背景属性 (常用)

即 (background properties), 用于设置元素的背景颜色、背景图片等。

### background-color

指定背景颜色。

```css
.box {
  background-color: #f5f5f5;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明 */
}
```

### background-image

指定背景图片。

```css
.box {
  background-image: url("image.jpg");
  background-image: linear-gradient(to right, #007bff, #00d084); /* 线性渐变 */
  background-image: radial-gradient(circle, #007bff, #00d084);   /* 径向渐变 */
}

/* 多重背景 (先定义的在上层) */
.box {
  background-image:
    url("overlay.png"),
    linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.5));
}
```

### background-size

指定背景图片的大小。

```css
.box {
  background-size: cover;      /* 覆盖整个区域, 可能裁剪 */
  background-size: contain;    /* 完整显示, 可能留空 */
  background-size: 100% 100%; /* 拉伸填充 */
  background-size: 200px 100px; /* 指定宽高 */
}
```

### background-position

指定背景图片的位置。

```css
.box {
  background-position: center;        /* 居中 */
  background-position: top right;     /* 右上角 */
  background-position: 50% 50%;       /* 居中 */
  background-position: 20px 10px;     /* 指定位置 */
}
```

### background-repeat

指定背景图片是否重复。

```css
.box {
  background-repeat: repeat;     /* 重复 (默认) */
  background-repeat: no-repeat;  /* 不重复 */
  background-repeat: repeat-x;    /* 水平重复 */
  background-repeat: repeat-y;    /* 垂直重复 */
}
```

### background 简写

```css
.box {
  background: #f5f5f5 url("image.jpg") no-repeat center/cover;
  /* 颜色 图片 重复 位置/大小 */
}
```

## 边框属性 (常用)

即 (border properties), 已在 [[css-box-model]] 中详细介绍了 border 的基本用法, 这里补充一些高级用法。

### border-radius (圆角)

```css
.box {
  border-radius: 8px;              /* 四个角统一圆角 */
  border-radius: 8px 4px;          /* 左上右下 右上左下 */
  border-radius: 8px 4px 2px 1px;  /* 四个角分别设置 */
  border-radius: 50%;              /* 圆形 */
  border-radius: 20px 10px;        /* 椭圆角 */
}

/* 单独设置每个角 */
.box {
  border-top-left-radius: 10px;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 20px;
}
```

### box-shadow (阴影)

为元素添加阴影效果。

```css
.box {
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
  /* 水平偏移 垂直偏移 模糊半径 颜色 */

  /* 内阴影 */
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);

  /* 多重阴影 */
  box-shadow:
    0 2px 4px rgba(0, 0, 0, 0.1),
    0 8px 16px rgba(0, 0, 0, 0.1);
}
```

## 其他视觉属性 (中等)

### opacity

指定元素的透明度。

```css
.text {
  opacity: 1;     /* 完全不透明 (默认) */
  opacity: 0.5;   /* 半透明 */
  opacity: 0;     /* 完全透明 (仍然占据空间) */
}
```

### cursor

指定鼠标悬停时的光标样式。

```css
.element {
  cursor: default;      /* 默认箭头 */
  cursor: pointer;      /* 手型 (链接) */
  cursor: text;         /* 文本输入 */
  cursor: move;         /* 可移动 */
  cursor: not-allowed;  /* 禁止 */
  cursor: help;         /* 帮助 */
}
```

### overflow

指定内容溢出时的处理方式。

```css
.box {
  overflow: visible;   /* 默认, 内容溢出显示 */
  overflow: hidden;    /* 裁剪溢出内容 */
  overflow: scroll;    /* 始终显示滚动条 */
  overflow: auto;      /* 需要时显示滚动条 */
}

/* 单独控制水平/垂直方向 */
.box {
  overflow-x: hidden;
  overflow-y: auto;
}
```

### outline

在元素外围绘制轮廓线 (不影响布局)。

```css
.input {
  outline: none;              /* 去除轮廓 (需确保有替代焦点样式) */
  outline: 2px solid #007bff;
  outline-offset: 2px;        /* 轮廓与边框的间距 */
}
```
