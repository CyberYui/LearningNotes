# HTML 学习笔记

> 一个文件包含所有的知识点
>
> 例子只挑一些必要的放在 Learning 文件夹中

## HTML 简介

- 即 **超文本标记语言 ( Hyper Text Markup Language )**, 它是一种标记语言而非编程语言, 即使用标记标签来描述网页
- HTML 标签和 HTML 元素一般描述的是同样的意思, 现使用的 HTML5 是2012年发布的
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

---

## 标签分类导航

### [[基础标签]]

**作用:** 定义 HTML 文档的基本结构和元数据
- 声明文档类型和编码格式
- 链接外部资源（CSS、图标等）
- 设置页面标题和描述

### [[文本标签]]

**作用:** 定义文本内容的结构和样式
- 创建标题层级（h1-h6）
- 定义段落和文本格式
- 强调重要文本内容

### [[链接与媒体标签]]

**作用:** 创建超链接和嵌入多媒体内容
- 链接到其他页面或资源
- 嵌入图片、视频和音频
- 创建图片热区链接

### [[列表标签]]

**作用:** 创建有序和无序列表
- 展示项目清单
- 定义术语和描述
- 创建导航菜单

### [[表格标签]]

**作用:** 展示结构化数据
- 创建数据表格
- 定义表头和表尾
- 合并单元格

### [[表单标签]]

**作用:** 创建用户交互界面
- 收集用户输入数据
- 创建各种输入控件
- 验证和提交表单

### [[语义化标签]]

**作用:** 定义页面结构和内容区域
- 明确页面头部、底部和导航
- 划分内容区块
- 提升可访问性和 SEO

### [[其他标签]]

**作用:** 提供特殊功能和增强内容
- 折叠展开内容
- 展示图片和说明
- 显示进度和度量

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
