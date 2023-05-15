# HTML相关知识点

> 一个文件包含所有的知识点
>
> 例子只挑一些必要的放在 Learning 文件夹中

## HTML

- 即 **超文本标记语言 ( Hyper Text Markup Language ) ** , 它是一种标记语言而非编程语言 , 即使用标记标签来描述网页 , Html标签 和 Html元素 一般描述的是同样的意思 , 现使用的 HTML5 是2012年发布的
- HTML 文档的后缀名必须是 <kbd>.html</kbd> 或者 <kbd>.htm</kbd> , 浏览器的作用是读取 HTML 文档 , 并以网页的形式显示出它们 , HTML 文档也称为 web页面
- 行内格式化上下文时, 排列顺序根据书写模式的设定来决定 :
  - 对于水平书写模式，各个框从左边开始水平地排列
  - 对于垂直书写模式，各个框从顶部开始水平地排列
- 

### 基础常用标签

| **标签名**          | **定义**       | **说明**                                                     |
| ------------------- | -------------- | ------------------------------------------------------------ |
| <!DOCTYPE html>     | 声明           | doctype 声明是不区分大小写的, 示例是HTML5的通用声明          |
| <html></html>       | HTML标签       | 页面中最大的标签, 我们称为 `根标签`                          |
| <head></head>       | 头部           | head标签中需要设置的标签是 `title`                           |
| <title></title>     | 标题           | 网页的页面标题, 一般内容通过 <h1> - <h6> 标签定义标题        |
| <body></body>       | 主体           | 元素包含文档的所有内容, 页面内容基本都是放到 body 里面的     |
| <header></header>   | 网页介绍       | 通常包含一组介绍性的或是辅助导航的实用元素, 如 Logo          |
| <footer></footer>   | 页脚           | 通常包含该章节作者, 版权数据或者与文档相关的链接等信息       |
| <article></article> | 独立文本结构   | 表示文档, 页面, 应用或网站中的独立结构, 其意在成为可独立分配的或可复用的结构 |
| <section></section> | 通用独立章节   | 一般来说会包含一个标题, 然后紧跟一段文字, 只是用于分节       |
| <nav></nav>         | 导航           | 在当前文档或其他文档中提供导航链接菜单, 目录和索引           |
| <video></video>     | 嵌入媒体播放器 | 用于支持文档内的视频播放, 也可以将 `<video>` 标签用于音频内容, 但是更建议使用 `<audio>` 标签于音频内容 |
| <ul></ul>           | 无序列表       | 项目符号表示的列表                                           |
| <ol></ol>           | 有序列表       | 带编号的列表                                                 |
| <li></li>           | 列表条目       | 它必须包含在一个父元素里, 如有序表 `<ol>` , 无序表 `<ul>` , 菜单 `<menu>` , 菜单和无需表中一般用符号表示, 有序列表中用序号表示 |
| <p></p>             | 段落           | 表示文本的一个段落, 通常表现为一整块与相邻文本分离的文本, 或以垂直的空白隔离或以首行缩进 |
| <a></a>             | 链接/锚        | 可以通过其 href 属性创建通向其他网页, 文件, 电子邮件地址, 同一页面内的位置或任何其他 URL 的超链接 |
| <img />             | 图像           | 将一张图像嵌入文档                                           |

## VScode 相关快捷操作



--------------

## 一些问题

### 常用的浏览器有哪些?

- IE , Edge , Firefox , Chrome , Safari , Opera 六大浏览器

### 常用的浏览器对应的内核是?

- IE ( Trident ) -- 猎豹安全 , 360 , 百度浏览器等

- firefox ( Gecko )

- Safari ( Webkit )

- Chrome / Opera ( Blink )

  > Blink 其实是 WebKit 内核的分支

### Web标准的构成

> 最佳体验方案 : 三种文件相分离 ( 即结构 , 样式 , 行为相分离 )

| **标准**            | **说明**                                                     |
| :------------------ | :----------------------------------------------------------- |
| 结构 (Structure)    | 结构用于对 **网页元素** 进行整理和分类 , 现阶段主要学的是 HTML |
| 表现 (Presentation) | 表现用于设置网页元素的版式 , 颜色 , 大小等 **外观样式** , 主要指的是 CSS |
| 行为 (Behavior)     | 行为是指网页模型的定义以及 **交互** 的编写 , 现阶段主要是 JS |

### 一个完整的Html文档应有哪些内容?

![img](https://www.runoob.com/wp-content/uploads/2013/06/02A7DD95-22B4-4FB9-B994-DDB5393F7F03.jpg)

- `<!DOCTYPE html>` 声明为 HTML5 文档
- `<html>` 元素是 HTML 页面的根元素
- `<head>` 元素包含了文档的元（meta）数据，如 `<meta charset="utf-8">` 定义网页编码格式为 **utf-8** 
- `<title>` 元素描述了文档的标题
- `<body>` 元素包含了可见的页面内容
- `<h1>` 元素定义一个大标题
- `<p>` 元素定义一个段落

### 块级元素

> 即 (block-level content), 此类标签因会在创建时使用一个区块而得名, 即类似盒子一样, 总是一个接一个地垂直放置在页面中; **块级元素总是开始在新的行/列上**, 它占据父容器的整个水平空间和等于其内容高度的垂直空间
>
> 现在的HTML编辑中 , 这类属性会被 css 接管

在下面的示例中，两个段落 `<p>` 元素被放置在 `<div>` 中:

```html
<div>
  <p>
    This the first paragraph. The background color of these paragraphs have been
    colored to distinguish them from their parent element.
  </p>
  <p>This is the second paragraph.</p>
</div>
```

### 行级元素

> 即 (inline-level content), 此类标签会按照文本基线进行对齐显示, 默认情况下, 大多数文本, 替换元素以及生成的内容都是行级的

在下面的示例中, `<p>` 元素包含一些文本, 在该文本中有一个 `<span>` 元素和两个 `<input>` 元素, 它们都是行级元素, 如果, `<span>` 分布在不同的行上, 则会生成两个行盒; 因为这些元素是行内的, 该段落只会渲染为不间断文本流的单个段落

```html
<p>
  This span is an <span class="highlight">inline-level element</span>; its
  background has been colored to display both the beginning and end of the
  element's influence. Input elements, like <input type="radio" /> and
  <input type="checkbox" />, are also inline-level content.
</p>
```

