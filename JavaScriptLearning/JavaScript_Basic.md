# JavaScript 基础

----------------

## 从简单的输出开始

* Js 中最基础的输出就是 `alert` 命令

  ```javascript
  // Java 中
  System.out.println("This is a warning");
  // JavaScript 中
  alert('This is an alert');
  ```

-----------------------

## JS 简介

* **JavaScript 是运行在客户端的脚本语言** , 也就是不需要编译 , **逐行解释** 并执行的 , 这标志着它不需要环境的配置即可运行 , JS 是一种高级编程语言

* JS 的应用场景 : 

  * 表单动态校验 ( 密码强度检测 )
  * 网页特效
  * 服务端开发 ( Node.js )
  * 桌面程序 ( Electron )
  * App ( Cordova )
  * 控制硬件 - 物联网 ( Ruff )
  * 游戏开发 ( cocos2d-js )

* HTML / CSS / JS 的关系

  * HTML / CSS 标记语言 -- 描述类语言
  
    [HTML] --- 决定网页结构和内容 (决定看到什么) , 相当于人的身体
  
    [CSS] --- 决定网页呈现给用户的模样 (决定好不好看) , 相当于给人穿衣服 , 化妆
  
  * JS 脚本语言 -- 编程类语言
  
    [JS] --- 实现业务逻辑和页面控制 (决定功能) , 相当于人的各种动作
### 浏览器是如何运行的以及JS的组成

* 浏览器分为 **渲染引擎** 和 **JS引擎** 
  * **渲染引擎** : 用来解析 HTML 与 CSS , 俗称 **内核** , 比如 chrome 浏览器的 blink , 老版本的 webkit
  * **JS 引擎** : 也称为JS 解释器 . 用来读取网页中的 JavaScript 代码 , 对其处理后运行 , 比如 chrome 浏览器的 V8
* JS 的组成
  1. ECMAScript --- JavaScript语法 ( 基础 )
  2. DOM --- 页面文档对象模型 ( API )
  3. BOM --- 浏览器对象模型 ( API )

### ECMAScript

* 是由 ECMA 国际标准化的一门编程语言 , 其主要实现和扩展有两种 , 分别是 : 

  - JavaScript -- 网景公司
  - Jscript -- 微软公司

  [PS] ECMAScript 规定了 JS 的编程语法和基础核心知识 , 是所有浏览器厂商共同遵守的一套 JS 语法工业标准

### DOM ( Document Object Model )

* 文档对象模型是 W3C 组织推荐的处理可扩展标记语言的 **标准编程接口** , 通过 DOM 提供的接口可以对页面上的各种元素进行操作 ( 大小 , 位置 , 颜色等 )

### BOM ( Browser Object Model )

* 浏览器对象模型提供了独立于内容的 , 可以与浏览器窗口进行互动的对象结构.通过 BOM 可以操作浏览器窗口 , 比如弹出框 , 控制浏览器跳转 , 获取分辨率等.

-----------

## 开始 JS

* JS 的书写位置有 **行内 , 内嵌 , 外部** 三种形式

  1. 行内式的 JS 直接写到元素内部即可

  ```html
  <!-- onclick 被写在了行内 -->
  <input type="button" value="CyberYui" onclick="alert('Here is an alert')">
  ```

  2. 内嵌式的 JS 写在 `<Script>` 标签内部
  ```html
  <script>
  	alert('Here is another alert');
  </script>
  ```

  3. 外部式的 JS 写在外部文件中
  假如有一个叫 <kbd>my.js</kbd> 的文件 , 其内容如下
  ```javascript
  alert('Here is outside JS alert');
  ```
  > 要想使用这个文件 , 需要在页面中引用它

  ```html
  <!-- 引入同级目录下的 my.js -->
  <script src="my.js"></script>
  ```
  
* [PS] 需要注意的是 : 

  1. 行内式

  * 可以将单行或少量 JS 代码写在 HTML 标签的事件属性中 ( 以 on 开头的属性 ) , 比如 onclick
  * 注意单双引号的使用 , HTML 中用双引号 , JS 中使用单引号
  * 可读性差 , 这种方式的 JS 代码如果在 HTML 中存在大量的话 , 不方便阅读
  * 引号易错 , 引号多层嵌套匹配的时候 , 非常容易被弄混
  * 特殊情况下才会使用此种方式
