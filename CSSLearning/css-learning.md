# CSS 学习笔记

> 一个文件包含所有的知识点
>
> 例子只挑一些必要的放在 Learning 文件夹中

## CSS 简介

- 即 **层叠样式表 (Cascading Style Sheets)**, 用于描述 HTML 文档的样式和布局, 实现网页内容与表现的分离
- CSS 由 **W3C (万维网联盟)** 制定和维护, 当前以模块化方式演进 (CSS3 泛指 CSS Level 3 及之后的模块)
- CSS 不能独立存在, 必须依附于 HTML 文件, 通过选择器与 HTML 元素建立关联
- 引入 CSS 的三种方式: **内联样式** (style 属性)、**内部样式表** (`<style>` 标签)、**外部样式表** (`<link>` 引用 .css 文件)

```html
<!-- 内联样式 -->
<p style="color: red; font-size: 16px;">红色文本</p>

<!-- 内部样式表 -->
<head>
  <style>
    p { color: red; font-size: 16px; }
  </style>
</head>

<!-- 外部样式表 -->
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

## 基础概念

### CSS 语法结构

即 (CSS syntax), CSS 规则由 **选择器 (selector)** 和 **声明块 (declaration block)** 组成, 声明块包含一个或多个 **属性-值对 (property: value)**。

```css
选择器 {
  属性1: 值1;
  属性2: 值2;
}

/* 示例 */
h1 {
  color: #333;
  font-size: 24px;
  margin-bottom: 16px;
}
```

- **选择器:** 指定要应用样式的 HTML 元素
- **声明块:** 用 `{}` 包裹, 包含一个或多个声明
- **声明:** 由属性名和属性值组成, 以 `:` 分隔, 以 `;` 结尾
- **注释:** 使用 `/* 注释内容 */` 包裹, 支持多行

### 层叠 (Cascade)

即 (cascade), 当多个规则作用于同一元素时, 浏览器按照优先级和顺序决定最终样式, 这就是"层叠"的含义。

- **样式来源优先级 (从低到高):**
  1. 浏览器默认样式 (user agent stylesheet)
  2. 用户自定义样式
  3. 外部样式表 / 内部样式表 (按引入顺序, 后引入的覆盖先引入的)
  4. 内联样式 (style 属性)
  5. `!important` 声明 (慎用, 会打破层叠规则)

```css
/* 外部样式表 */
p { color: blue; }

/* 内部样式表 (后引入, 覆盖外部) */
p { color: green; }

/* 内联样式 (优先级最高) */
/* <p style="color: red;">这段文本是红色</p> */
```

### 继承 (Inheritance)

即 (inheritance), 某些 CSS 属性会自动从父元素传递给子元素, 无需为每个子元素重复设置。

- **可继承的属性 (文本相关):** color、font-family、font-size、line-height、text-align、letter-spacing 等
- **不可继承的属性 (盒模型相关):** width、height、margin、padding、border、background 等
- 使用 `inherit` 关键字可以强制继承父元素的值

```css
/* 父元素设置字体颜色, 子元素自动继承 */
body {
  color: #333;
  font-family: "Microsoft YaHei", sans-serif;
}

/* 子元素会继承 body 的 color 和 font-family */

/* 强制继承 */
.child {
  border: inherit; /* 强制继承父元素的 border */
}
```

### 优先级 (Specificity)

即 (specificity), 当多个选择器作用于同一元素时, 优先级高的规则会覆盖优先级低的规则。

| 优先级 | 选择器类型 | 示例 |
|--------|-----------|------|
| 最高 | 内联样式 | `style="color: red;"` |
| 高 | ID 选择器 | `#header { }` |
| 中 | 类选择器、属性选择器、伪类 | `.nav { }`、`[type="text"] { }`、`:hover { }` |
| 低 | 元素选择器、伪元素 | `p { }`、`::before { }` |
| 最低 | 通用选择器 | `* { }` |

- 优先级相同时, 后定义的规则覆盖先定义的规则
- 使用 `!important` 可以强制提升优先级, 但应避免滥用

```css
/* 优先级计算示例 */
p { color: black; }           /* 低优先级 */
.text { color: blue; }        /* 中优先级 */
#main .text { color: green; } /* 高优先级 (ID + 类) */
p { color: red !important; }  /* 强制最高 (不推荐) */
```

### 引入方式

即 (import methods), CSS 可以通过多种方式引入到 HTML 文档中, 不同方式有不同的适用场景。

- **外部样式表 (最推荐):** 使用 `<link>` 标签引用, 实现样式与结构分离, 可被多个页面复用
- **内部样式表:** 使用 `<style>` 标签定义, 适用于单页样式或页面特有的样式
- **内联样式:** 使用 `style` 属性, 优先级最高但不推荐, 难以维护和复用
- **@import 导入:** 在 CSS 文件中引入其他 CSS 文件, 但性能较差, 不推荐

```html
<!-- 外部样式表 (推荐) -->
<link rel="stylesheet" href="styles.css">

<!-- 内部样式表 -->
<style>
  body { font-family: sans-serif; }
</style>

<!-- 内联样式 (不推荐) -->
<p style="color: red;">文本</p>
```

## CSS 分类导航

### CSS 选择器 (css-selectors) [[css-selectors]]

**作用:** 指定要应用样式的 HTML 元素
- 基础选择器: 通用、元素、类、ID
- 组合选择器: 后代、子、兄弟
- 伪类与伪元素: :hover、:nth-child()、::before 等
- 优先级计算规则

### CSS 盒模型 (css-box-model) [[css-box-model]]

**作用:** 定义元素在页面中所占空间的大小和排列方式
- 盒模型组成: content → padding → border → margin
- box-sizing: content-box vs border-box
- margin 合并 (外边距折叠)
- → 搭配 [[HtmlLearning#form-tags]]、[[HtmlLearning#table-tags]] 使用

### CSS 视觉表现 (css-visual) [[css-visual]]

**作用:** 控制元素的颜色、字体、背景、边框等视觉效果
- 颜色表示: hex、rgb、hsl
- 字体与文本属性
- 背景图片与渐变
- 边框圆角与阴影

### CSS 布局 (css-layout) [[css-layout]]

**作用:** 控制元素在页面中的位置和排列方式
- Flex 布局 (最常用): 一维布局
- Grid 布局 (常用): 二维布局
- 定位: relative、absolute、fixed、sticky
- 浮动: float 与清除浮动
- → 搭配 [[HtmlLearning#semantic-tags]] 构建页面结构

### CSS 响应式设计 (css-responsive) [[css-responsive]]

**作用:** 使网页在不同设备和屏幕尺寸下都能良好显示
- 媒体查询: @media 语法与断点设置
- 响应式单位: rem、vw、vh、%
- 移动优先设计策略
- → 搭配 [[HtmlLearning#other-tags]] 中的 `<meta>` 标签使用

### CSS 动画与交互 (css-animation) [[css-animation]]

**作用:** 为页面元素添加动态效果和交互反馈
- Transition: 过渡效果
- Transform: 位移、旋转、缩放
- Animation: 关键帧动画
- 性能优化建议

### CSS 工程化 (css-engineering) [[css-engineering]]

**作用:** 在大型项目中组织和管理 CSS 代码
- CSS 变量: 主题切换与全局配置
- BEM 命名法: 避免样式冲突
- 选择器性能优化
- CSS 新特性: 容器查询、层叠层

---

## 常见问题

### CSS 和 HTML 是什么关系?

HTML 负责页面结构 (内容是什么), CSS 负责页面表现 (内容长什么样), JS 负责页面行为 (内容做什么)。三者配合才能构建完整的网页。

### 外部样式表、内部样式表、内联样式哪个更好?

**外部样式表最佳**, 原因:
- 实现样式与结构分离
- 可被浏览器缓存, 加快页面加载
- 一个 CSS 文件可被多个 HTML 页面复用
- 便于维护和团队协作

内部样式表适用于单页样式或页面特有的样式, 内联样式应尽量避免使用 (除非用于动态样式或测试)。

### Flex 和 Grid 有什么区别?

| 特性 | Flex 布局 | Grid 布局 |
|------|----------|----------|
| 维度 | 一维 (行或列) | 二维 (行和列) |
| 适用场景 | 导航栏、列表、居中 | 页面整体布局、复杂网格 |
| 对齐方式 | 主轴 + 交叉轴 | 行 + 列 |
| 常用度 | 最常用 | 常用 |

建议: 一维排列用 Flex, 二维布局用 Grid。

### 为什么不推荐使用 `!important`?

- 打破层叠规则, 使样式优先级混乱
- 难以调试和维护
- 后续覆盖需要更多 `!important`, 形成恶性循环
- 应通过提高选择器优先级或调整代码顺序来解决

### 如何理解 "移动优先" 设计?

- 先为移动端 (小屏幕) 编写基础样式
- 然后使用 `min-width` 媒体查询为大屏幕添加增强样式
- 好处: 移动设备加载更快, 渐进增强

```css
/* 移动优先: 基础样式针对小屏幕 */
.container { padding: 10px; }

/* 大屏幕增强 */
@media (min-width: 768px) {
  .container { padding: 20px; max-width: 1200px; margin: 0 auto; }
}
```
