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

* 换句话说 , JS 在运行时是解析一句然后执行一句 , 一旦遇到问题就会直接退出程序

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

------------------

### JS 的使用

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

  1. **行内式**

  * 可以将单行或少量 JS 代码写在 HTML 标签的事件属性中 ( 以 on 开头的属性 ) , 比如 onclick
  * 注意单双引号的使用 , HTML 中用双引号 , JS 中使用单引号
  * 可读性差 , 这种方式的 JS 代码如果在 HTML 中存在大量的话 , 不方便阅读
  * 引号易错 , 引号多层嵌套匹配的时候 , 非常容易被弄混
  * 特殊情况下才会使用此种方式

  2. **内嵌式** (最常用)

  * 可以将多行 JS 代码写到 `<script>` 标签中
  * 内嵌 JS 是学习时常用的方式

  3. **外部式** (完成用)

  * 利用 HTML 页面代码结构化 , 把大段 JS 代码独立到 HTML 页面之外 , 既美观 , 也方便文件级别的复用
  * 引用外部 JS 文件的 script 标签中间不可以写代码
  * 适合于 JS 代码量比较大的情况
  * 前端项目使用 webpack 打包之后也会生成这样的文件

--------------

### JS 注释

> 这里由于是学习 , 使用的编辑器进行代码编写 , 用的是 VScode 

* 单行注释 `//单行注释` , 快捷键一般是 <kbd>ctrl</kbd> + <kbd>/</kbd> 

* 多行注释 , 快捷键一般是 <kbd>shift</kbd> + <kbd>alt</kbd> + <kbd>a</kbd> 

  > 一般会把多行注释改成 <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>/</kbd> 

  ```javascript
  /** 注释
  * 这是多行注释
  */
  ```

----------------

## JS 基础

-----------------

### JS 输入输出语句

* 为了方便信息的输入和输出 , JS 中提供了一些输入和输出语句 , 其常用的语句如下

  |         方法         |              说明               |  归属  |
  | :------------------: | :-----------------------------: | :----: |
  |    **alert(msg)**    |        浏览器弹出警示框         | 浏览器 |
  | **console.log(msg)** |    浏览器控制台打印输出信息     | 浏览器 |
  |   **prompt(info)**   | 浏览器弹出输入框 , 用户可以输入 | 浏览器 |

* 实际使用

  ```html
  <script>
    	// 这是一个输入框  
  	prompt('This is a input box,please enter sth.');
      // 这是一个警示框
      alert('Warning !');
      // console 打印信息
      console.log('Here will be shown in your console.');
  </script>
  ```

### ★ JS 变量

> 变量是用于存放数据的 **容器** , 我们通过 **变量名** 获取数据 , 甚至数据可以修改
>
> [PS] 变量就是一个盒子 , 里面装着数据

* 本质 : 变量是在 **内存** 中申请的 , 一块用来存放数据的 **空间** 

* 一个变量的生命周期 : 声明 → 赋值 → 使用 → 删除

* 通过以下命令声明变量

  ```js
  // 声明变量
  var age; // 声明一个名称为 age 的变量
  // 赋值变量
  age = 10; // 给 age 变量赋值为 10
  // 使用:输出结果
  console.log(age); // 输出 age 的值,即 18
  // 此时就停止使用变量了,删除则是程序自行删除的
  ```

  * var 是一个 JS 关键字 , 用来声明变量 (即 variable 的意思)
  * 使用该关键字声明变量之后 , 系统自动为变量分配内存空间
  * age 是自定义的一个变量名 , 我们要通过变量名来访问内存中分配的空间

* 变量的初始化 ( 即将变量的声明和赋值写成一句 )

  > 声明一个变量并赋值 , 我们称之为 <font color=#f52443>**变量的初始化**</font> 

  ```javascript
  // 变量的初始化
  var age = 18;
  ```

#### 案例:变量的使用

* 目标:

  1. 弹出一个输入框 , 提示用户输入姓名
  2. 弹出一个对话框 , 输出用户刚才输入的姓名

* 思路:

  1. 用户输入姓名
  2. 将用户输入的姓名存储到变量中
  3. 输出变量值

* 解决代码:

  ```javascript
  // 获取输入内容,
  var myname = prompt('Please press your name:');
  // 输出名字
  alert(myname);
  ```

#### ★ 变量语法扩展

* 更新变量

  > 一个变量被重新赋值之后 , 它原有的值就会被覆盖 , 值以最后一次赋的值为准

* 同时声明多个变量

  > 同时声明多个变量 , 只需要写一个 var , 多个变量名之间使用英文逗号隔开

  ```js
  // 声明多个变量
  var age = 18,address = '火影',gz = 2000;
  ```

* 声明变量的特殊情况

  1. 只声明不赋值 , 输出结果为 `undefined` ( 未定义 )
  2. 没有声明也没有赋值 , 直接使用会报错
  3. 不声明 , 直接赋值使用 , 变量会被作为全局变量被使用 ← 这种方式不被推荐

#### ★ 变量的命名规范

* 由字母 (A-Z a-z) , 数字 (0-9) , **下划线 (_)** , **美元符号 ($)** 组成 , 如 : usrAge , num01 , _name
* **严格区分大小写** , `var app;` 和 `var App;` 以及 `var APp;` `var APP;` 是不同的变量
* 不能以数字开头, `18age` 是错误的变量名
* 不能是 **关键字** , **保留字** , 例如 : var , for , while ( 可以参照相关文档 )
* 变量名必须有意义 , MMD BBD nl → age , 尽量使用英文单词而不是拼音首字母
* 遵守驼峰命名法 , 首单词字母小写 , 后面单词的首字母需要大写 , 比如 myFirstName

> [PS] name 有时候也会是关键字或者保留字 , 尽量不要用它作为变量名
>
> 允许在变量名中存在的符号只有 **_** 和 **$** 这两种符号

#### 案例 : 课堂练习

* 目标 : 交换两个变量的值

* 思路 : 搞个临时变量

* 解决代码 : 赋值语句是把右边给左边

  ```javascript
  // JS 作为一种编程语言,有很强的逻辑性
  var apple1 = '青苹果';
  var apple2 = '红苹果';
  // 把青苹果放桌子上
  var temp = apple1;
  // 把红苹果给 apple1
  apple1 = apple2;
  // 把青苹果给 apple2
  apple2 = temp;
  // apple1→'红苹果' apple2→'青苹果'
  ```

-----------------

## 数据类型

-------------

### 数据类型简介

* 为了便于吧数据分成所需内存大小不同的数据 , 充分利用存储空间 , 于是定义了不同的数据类型 :

  **值类型(基本类型)**--[简单数据类型]：

  * 字符串 (String)  , 数字(Number) , 布尔(Boolean) , 对空 (Null)  , 未定义 (Undefined)  , Symbol

    | **简单数据类型** |                           **说明**                           | **默认值** |
    | :--------------: | :----------------------------------------------------------: | :--------: |
    |      Number      |            数字型,包含整型值和浮点型值,如21,0.21             |     0      |
    |     Boolean      |            布尔型,如 true , false , 等价于 1 和 0            |   false    |
    |      String      |       字符串型,如 '张三' [在JS中,所有的字符串都带引号]       |     ''     |
    |    Undefined     | `var a;` 声明了变量 a 但是没有赋值 , 此时 a 的类型为 undefined | undefined  |
    |       Null       |             `var a = null;` 声明了变量 a 为空值              |    null    |

  **引用数据类型**--[复杂数据类型]：

  ​	对象(Object) , 数组(Array) , 函数(Function)

### ★变量的数据类型

* **JavaScript 是一种弱类型, 或者说动态的语言** 

* 这意味着不用提前声明变量的类型 , 在程序运行过程中 , 类型会被自动确定

* 与 Java 不同的是 , 在 Java 中我们可以用 `int num=10;` 这样的语句创建一个整型变量

* 但是在 JavaScript 中 , 我们直接使用 `var num = 10;` 就可以创建一个数字型的数据

* 也就是说 , 直接使用 `var num` 是无法确定变量的数据类型的

  [PS] JS 变量的数据类型是由 JS 引擎根据赋值号右侧的数值确定的 , 代码运行完毕之后 , 变量就确定了数据类型

  由于 JavaScript 拥有动态类型 , 同时也意味着一个变量可以拥有不同的数据类型

------------------

### 1.数字型 (Number)

* `var num = 10;` 以及 `var PI = 3.14;` 都是数字型变量

#### 数字型进制

* 最常见的有二进制 (0,1) , 八进制 (0~7) , 十进制 (0~9) , 十六进制 (0~9,ABCDEF)

  ```javascript
  var num1 = 010;
  // 010 八进制,转换为十进制就是 8
  console.log(num1); 
  
  var num2 = 0xA;
  // 0xA 十六进制,转换为十进制就是 10
  console.log(num2); 
  ```

  > 我们只需要知道 , **在 JavaScript 中 , 八进制数前加 0 , 十六进制数前加 0x** 

#### 数字型范围

* JavaScript 中数字的最大和最小值

  ```javascript
  alert(Number.MAX_VALUE); // 1.7976931348623157e+308
  alert(Number.MIN_VALue); // 5e-324
  ```

#### △数字型的特殊值

* 数字型有三个特殊值

  > **Infinity** , 代表无穷大 , 大于任何数值
  >
  > **-Infinity** , 代表无穷小 , 小于任何数值
  >
  > **NaN** , 即 **Not a number** , 代表一个非数值

  ```js
  console.log(Number.MAX_VALUE * 2); // Infinity
  console.log(-Number.MAX_VALUE * 2); // -Infinity
  console.log('pink' - 100); // NaN
  ```

#### ★isNaN

* isNaN() 方法用来判断一个变量是否为非数字类型 , 并返回一个值 , 是数字返回 false , 否则返回 true

  ```js
  console.log(isNaN(12)); //结果返回false
  ```

----------------------

### 2.字符串型 (String)

- 字符串型可以是引号中的任意文本 , 引号可以是双引号也可以是单引号

- 由于 HTML 标签中的属性使用的是双引号 , 所以 JS 里推荐使用单引号

  > JS 中 , 可以使用单引号嵌套双引号 , 或者使用双引号嵌套单引号 (外双内单 , 外单内双)

#### △字符串转义符

* 类似于 HTML 中的特殊字符 , 字符串可以使用转义符

  |  **转义符**   |      **解释说明**       |
  | :-----------: | :---------------------: |
  | <kbd>\n</kbd> | 换行符 , n 意为 newline |
  | <kbd>\\</kbd> |         斜杠 \          |
  | <kbd>\'</kbd> |        ' 单引号         |
  | <kbd>\"</kbd> |        " 双引号         |
  | <kbd>\t</kbd> |        tab 缩进         |
  | <kbd>\b</kbd> |   空格 , b 意为 blank   |

#### 字符串长度及拼接

* 字符串是由若干字符组成的 , 这些字符的数量称为字符串长度

* 通过字符串的 length 属性可以获取整个字符串的长度

  ```js
  var str = 'my name is cyber';
  console.log(str.length); // 16
  ```

* 多个字符串之间可以使用 <kbd>+</kbd> 进行拼接 , 其拼接方式为 <font color="#f52443">字符串 + 任何类型 = 拼接之后的新字符串</font> 

* 拼接前会把字符串相加的任何类型转成字符串 , 再拼接成一个新的字符串

  > 只要有字符串拼接 , 最后的结果就是字符串 (<kbd>+</kbd>号口诀 : <font color="#eddd9e">数值相加 , 字符相连</font>)
  >
  > ```js
  > alert('11' + 12); //1112
  > ```

* 可以通过使用变量的形式输出会变化或者能控制的值

  > ```js
  > var age = 18;
  > console.log('I am '+ age +' years old.'); // I am 18 years old.
  > ```

  > 引号是就近匹配 , 四个引号直接会空出填写变量的地方

#### ★显示年龄案例

* 要求 : 弹出一个输入框 , 要求用户输入年龄 , 之后弹出警示框显示 "你今年xx岁啦" (xx表示刚刚输入的年龄)

  ```js
  var attitude = prompt('你喜欢我吗?');
  var str = '你的回答是:' + attitude;
  alert(str);
  ```

----------------------

### 3.布尔型 (Boolean)

* 布尔类型有 true 和 false 两个值 , 分别表示 真 / 假
* 布尔型可以和数字型相加 , 此时 true 的值为 1 , false 的值为 0

#### ❤ Undefined 未定义型 和 Null 空值

> 未定义型 也是一种数据类型

* 如果一个变量声明未赋值 , 那它就是 undefined , 即未定义数据类型

```javascript
var str;
console.log(str); // undefined
var variable = undefined;
console.log(variable + 'pink'); // undefinedpink -- 任何类型和 string 相连,最后都是 字符串型
console.log(variable + 1); //NaN --- undefined 和数字相加最后的结果为 NaN
var space = null; // 空值 --- undefined 和空值的区别
console.log(space + 'pink'); // nullpink
console.log(space + 1); // 1
```

* 一个声明后没有被赋值的变量会有一个默认值 undefined ( 注意它与其他数据类型的相连和相加结果 )
* 一个声明并赋予 null 值的变量 , 里面存储的值为空 ( 在对象中还会用到它 )

#### typeof 检测数据类型

* 一个变量的实际数据类型并不能想当然地判断 , 需要我们通过可靠的程序去检测

```javascript
var age = 18;
console.log(typeof var); // number
var str = 'cyber';
console.log(typeof(str)); // string --- 不论是空格还是括号包裹,都是可以的
var flag = true;
console.log(typeof flag); // boolean
var vari = undefined;
console.log(typeof vari); // undefined
var timer = null;
vonsole.log(typeof timer); // object
// 一个有趣的例子
var realage = prompt('Please press your age');
console.log(realage);
console.log(typeof(realage)); // string
```

* 事实上 , 我们不仅可以通过 typeof 的返回值判断变量的数据类型 , 还可以通过 chrome 浏览器的控制台输出判断

```javascript
console.log(18); // number -- 藏蓝色
console.log('18'); // string -- 黑色
console.log(true); // boolean -- 蓝色
console.log(undefined); // undefined -- 浅灰色
console.log(null); // null -- 浅灰色
```

### 字面量

* 字面量是在源代码中一个固定值的表示法 , 通俗来说 , 就是字面量表示如何表达这个值
  * 数字字面量 : 8 , 9 , 10
  * 字符串字面量 : '程序员' , '前端程序员'
  * 布尔字面量 : true , false

### ★ 数据类型转换

* 使用表单或者 prompt ( 即用户输入 ) 获取到的数据默认为**字符串类型** , 此时我们需要 :
* **把一种数据类型的变量转换成另外一种数据类型**

△ 通常会实现以下三种类型的转换 : 

* 转换为字符串类型
* 转换为数字型
* 转换为布尔型

--------------------------

#### 转换为字符串

|      **方式**      |           **说明**           |              **案例**              |
| :----------------: | :--------------------------: | :--------------------------------: |
|     toString()     |          转成字符串          | var num=1; alert(num.toString());  |
| String() 强制转换  |          转成字符串          |   var num=1; alert(String(num));   |
| **加号拼接字符串** | 和字符串拼接的结果都是字符串 | var num=1;alert(num+"我是字符串"); |

> 比较重要的是 **加号拼接字符串** 的方式

```javascript
// 类似的代码如下,我们可以实现类型转换
var num = 10;
var str = num.toString();
console.log(str);
console.log(typeof str);
// 直接将数字型的内容传参
console.log(String(num));
// 使用 + 拼接字符串进行转换
console.log(num + ' '); // 加个空格就行了
```

* toString() 和 String() 的使用方式不一样 , 一种是调用 , 另一种是传参
* 第三种 **加号拼接字符串** 的方式也称隐式转换

---------------------------

#### ★转换为数字型

|        **方式**         |            **说明**            |      **案例**       |
| :---------------------: | :----------------------------: | :-----------------: |
|  parseInt(string) 函数  |  将string类型转换为整数数字型  |   parseInt('78')    |
| parseFloat(string) 函数 | 将string类型转换为浮点数数字型 | parseFloat('78.21') |
|  Number() 强制转换函数  |    将string类型转换为数字型    |    Number('12')     |
|   js 隐式转换 (- * /)   |  利用算术运算隐式转换为数字型  |      '12' - 0       |

```javascript
var age = prompt('请输入您的年龄');
console.log(age); // 字符型
console.log(parseInt(age)); // 数字型,取整
console.log(parseInt('3.97')); // 3
console.log(parseInt('120px')); // 120
console.log(parseInt('res120px')); // NaN
```

* parseFloat(string) 类似于 parseInt 函数 , 只不过返回的是浮点型数字

```javascript
console.log(parseInt('3.97')); // 3.97
```

> 注意 I 和 F 是大写字母

* 隐式转换是我们在进行算术运算的时候 , JS 自动转换了数据类型

```javascript
// 使用 Number() 函数
console.log(Number(str));
```

* 使用算术运算 ( 减 , 乘 , 除 )

```javascript
// 这种运算有些特点,你再怎么弄也得是数字才能相加减
console.log('12' - 1); // 11
console.log('123' * 2); // 246
```

-----------------------------

#### 案例 : 计算年龄

* 目标 : 在页面中弹出一个输入框 , 输入出生年月日之后 , 能计算出年龄
* 思路 : 保存用户输入的年份 , 然后用今年年份减去它即可
* 解决代码 : 

```javascript
var year = prompt('please press your born year:');
// year 取过来的是字符串类型,刚刚好这里是减法,隐式转换了
var age = 2021 - year;
alert('Your age is '+age+' !');
```

> 只有 ( - * / ) 才有隐式转换 , 加法是没有隐式转换的哟

```JavaScript
// 加两个输入的数,加法没有隐式转换
var num1 = prompt('first num');
var num2 = prompt('second num');
var result = parseFloat(num1) + parseFloat(num2);
alert('The add result is ' + result);
```

--------------------------

#### 转换为布尔型

|   **方式**    |       **说明**       |    **案例**     |
| :-----------: | :------------------: | :-------------: |
| Boolean()函数 | 其他类型转换为布尔值 | Boolean('true') |

* 代表<font color=#f95245>空 否定</font>的值会被转换为 **false** , 比如 '' , 0 , NaN , null , undefined
* 其余值均为true

------------------------------

### 扩展阅读

* 能够知道解释型语言和编译型语言的特点
* 能够知道标识符是否为关键字或保留字
* 能够独立完成一些简单的程序

-----------------------

#### 解释型语言

* 计算机是无法理解除任何机器语言以外的语言的 , 所以必须要把高级程序语言翻译为机器语言才能执行程序 , 程序语言翻译成机器语言的工具 , 被称为翻译器
* 翻译器翻译的方式有两种 : 
  * 编译 -- 编译器在代码执行之前进行编译 , 生成中间代码文件
  * 解释 -- 解释器是在运行时进行及时编译 , 并立即执行 ( 当编译器以解释方式运行时 , 也称为解释器 )
* 两种方式之间的区别在于 <font color=#f95245>翻译的时间点不同</font> 
* JS 是典型的解释型语言 , Java 则是典型的编译型语言

![image-20210801110430028](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_basic_pic1.png) 

------------------------------------------

#### 标识符-关键字-保留字

* 标识符 : 即开发人员为变量 , 属性 , 函数 , 参数取的名字

  > 标识符不能是 **关键字** 或 **保留字** 

* 关键字 : 即 JS 本身已经使用了的字 , 不能再用它们充当变量名 , 方法名

* 保留字 : 实际上就是预留的 "关键字" , 即尽管现在不是关键字 , 但是将来可能会成为关键字 , 同样不能使用它们当变量名或者方法名

* ECMA-262 描述了一组具有特定用途的**关键字**,这些关键字可用于表示控制语句的开始或结束,或者用于执行特定操作等.按照规则,关键字也是语言保留的,不能用作标识符.以下为 ECMAScript 的全部关键字(带*号上标的是第5版新增的关键字):

* | Keywords 关键字 |          |            |        |
  | :-------------: | :------: | :--------: | :----: |
  |      break      |    do    | instanceof | typeof |
  |      case       |   else   |    new     |  var   |
  |      catch      | finally  |   return   |  void  |
  |    continue     |   for    |   switch   | while  |
  |    debugger*    | function |    this    |  with  |
  |     default     |    if    |   throw    |        |
  |     delete      |    in    |    try     |        |

* ECMA-262 还描述了另外一组不能用作标识符的**保留字**.尽管保留字在这门语言中还没有任何特定的用途,但它们有可能在将来被用作关键字.以下是 ECMA-262 定义的全部保留字:

* | Reserved words 保留字 |            |           |              |
  | :-------------------: | :--------: | :-------: | :----------: |
  |       abstract        |    enum    |    int    |    short     |
  |        boolean        |   export   | interface |    static    |
  |         byte          |  extends   |   long    |    super     |
  |         char          |   final    |  native   | synchronized |
  |         class         |   float    |  package  |    throws    |
  |         const         |    goto    |  private  |  transient   |
  |       debugger        | implements | protected |   volatile   |
  |        double         |   import   |  public   |              |

  > ECMAScript 5 把在非严格模式下运行的保留字缩减为下列这些:

  | ECMAScript 5 非严格模式保留字 |        |         |       |
  | :---------------------------: | :----: | :-----: | :---: |
  |             class             |  enum  | extends | super |
  |             const             | export | import  |       |

  > 在严格模式下,ECMAScript 5 还对以下保留字施加了严格的限制:

  | ECMAScript 5 严格模式保留字 |                 |                      |         |
  | :-------------------------: | :-------------: | :------------------: | :-----: |
  |         implements          |    interface    |         let          | package |
  |           private           |    protected    |        public        | static  |
  |            yield            | eval (非保留字) | arguments (非保留字) |         |

### JavaScript 预定义全局变量和函数

> JavaScript 预定义了很多全局变量和函数,我们也应该避免使用它们,下表列出的仅针对 Web 浏览器运行环境:

| JS预定义全局变量和函数 |                    |          |                |             |
| :--------------------: | :----------------: | :------: | :------------: | :---------: |
|       arguments        |     encodeURL      | Infinity |     Number     |   RegExp    |
|         Array          | encodeURLComponent | isFinite |     Object     |   String    |
|        Boolean         |       Error        |  isNaN   |   parseFloat   | SyntaxError |
|          Date          |        eval        |   JSON   |    parseInt    |  TypeError  |
|       decodeURL        |     EvalError      |   Math   |   RangeError   |  undefined  |
|   decodeURLComponent   |      Function      |   NaN    | ReferenceError |  URLError   |

> **[注意]** let 和 yield 是 ECMAScript 5 新增的保留字: 其他保留字都是 ECMAScript 3 定义的. 在实现 ECMAScript 3 的 JS 引擎中使用关键字作为标识符, 会导致 "Identifier Expected" 错误. 而使用宝录制作为标识符可能会也可能不会导致相同的错误, 具体取决于特定的引擎.
>
> 在上述中, eval 和 arguments 虽然并不是作为关键字或者保留字留存的, 但是在严格模式下, 这两个名字也不能作为标识符或属性名, 否则会抛出错误.

-------------------------------------

### 命名规范

* 在实际的代码编写中 , 为了使我们的代码简介易懂 , 需要在项目初期就进行代码的命名格式规范

-----------------------------

#### 标识符命名规范

* 变量 , 函数的命名必须要有意义
* 变量的名称一般用<font color="#c4332f">**名词**</font> 
* 函数的名称一般用<font color="#c4332f">**动词**</font> 

#### 操作符规范 ( 格式化 ) 

* 操作符的左右两侧各保留一个空格

  ```javascript
  let i = 1; // 而不是 let i=1;
  ```

* 单行注释尽量在开始留一个空格

  ```javascript
  // 这样注释
  //而不是这样
  ```

* 其他规范

  ```javascript
  // 多使用空格隔开符号和字符,以免字符符号冗杂
  if ( true ){
      // something
  } // 最后的大括号和开始的字符对齐
  ```

# JavaScript 基础 - 零碎知识

--------------

> 在一门语言的学习过程中 , 有很多模块化的知识 , 例如变量 , 函数等
>
> 但是有一些内容是零碎但重要的知识 , 这些知识在实际的代码编写过程中往往很容易被忽略
>
> 但是它们的的确确十分重要 , 在这里就对这些知识进行记录 , 方便自己查阅

--------------------------

### JavaScript 作用域

#### 作用域

* 通常 , 一段代码中使用到的变量或者函数的名称并不总是有效和可用的

* 限定这个名字 <font color="#f1b06f">可用性的代码范围</font> 就是这个名字的 <font color="#f1b06f">**作用域**</font> 

* 作用域提高了程序逻辑的局部性 , 增强了程序的可控性和可靠性 , 减少了大规模程序中的命名冲突等问题

* 简而言之 , 作用域就是 <font color="#ff9393">**变量或函数等名称在某个范围内起作用和效果**</font> 

* ES6 之前 , JS 的作用域分为 **全局作用域** 和 **局部作用域** , 只有到 ES6 的时候 , 才新增了 **块级作用域** 

* 全局作用域 : 整个 script 标签 或者是一个单独的 js 文件 , 都是一个全局作用域

* 局部作用域 : 在函数内部就是局部作用域 , 即这段 ( 或这行 ) 代码只在函数内部起效果和作用 

  ```javascript
  // Global Scope
  var num = 10;
  console.log(num);
  function newFn(){
      // Local Scope
      var num = 20;
      console.log(num);
  }
  newFn();
  ```

* 在同一个作用域中变量名会有命名冲突

* 块级作用域 : 使用 <kbd>{}</kbd> 包裹的区域 , 被称作块级作用域 , 现阶段各个浏览器均已拥抱 ES6 标准

#### 变量作用域

* 在 JS 中 , 根据作用域的不同 , 变量会分为两种 : **全局变量** 和 **局部变量** 

* 全局变量 : 在全局作用域下的变量 , 全局可用

* **★ [PS]** 如果在函数内部没有声明 , 直接使用或赋值的变量也是一个全局变量

* 局部变量 : 在局部作用域下的变量 , 仅局部可用

* **★ [PS]** 函数的形参也可以当做一个局部变量来使用

  ```javascript
  // Global Variable
  var num = 10;
  console.log(num);
  function newFn(aru){
      // aru is a Local Variable
      // Local Variable
      var num = 20;
      // Another Global Variable
      num2 = 100;
      console.log(num);
  }
  newFn();
  ```

* **★ 从执行效率来看** 

* 全局变量只有浏览器关闭的时候才会销毁 , 比较占内存资源

* 局部变量在程序执行完毕之后就会被销毁 , 比较节约内存资源

-------------------------

#### 作用域链

* 只要是代码 , 就至少有一个作用域 , 如果函数中还有函数 , 那么在这个作用域中就又可以诞生一个作用域

* 内部函数可以访问外部函数的变量 , 这种机制 , 是用链式查找来决定哪些数据能被内部函数访问的 , 这种结构就称作作用域链 ( **就近原则** )

  ```javascript
  // Global Variable
  var num = 10;
  function function1(){
      // Local Variable
      var num = 20;
      // Inner Function
      function function2(){
          // Inner function will use local variable
          console.log(num);
      }
      // transfer inner function
      function2();
  }
  // transfer outer function
  function1();
  ```

#### 作用域链案例

##### 案例-A

* 请观察以下代码 , 它的结果是什么 ?

  ```javascript
  function f1(){
      var num = 123;
      function f2(){
          console.log(num);
      }
      f2();
  }
  var num = 456;
  f1();
  ```

  > 这种代码的执行逻辑可以用链式图来展示 , 这和 CSS 的层叠性差不多 
  >
  > ![JS_Knowledges_pic1.png](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_Knowledges_pic1.png) 

* 请观察以下代码 , 它的结果是什么 ?

  ```javascript
  var a = 1;
  function fn1(){
      var a = 2;
      var b = '22';
      fn2();
      function fn2(){
          var a = 3;
          fn3();
          function fn3(){
              var a = 4;
              // a = 4
              console.log(a);
              // b = 22
              console.log(b);
          }
      }
  }
  fn1();
  ```

### ★JS 预解析

----------------

* 作为代码 , 其总会有一些处于边缘情况的编写问题 , 比如下面的情况

  ```javascript
  // ---------------------------------------------------------
  // 1st Question
  // 1st Answer:Uncaught ReferenceError: num1 is not defined
  console.log(num1);
  // ---------------------------------------------------------
  // 2nd Question
  // 2nd Answer:undefined
  console.log(num2);
  var num2 = 10;
  // ---------------------------------------------------------
  // 3rd Question
  // 3rd Answer:running well
  fn();
  function fn(){
      console.log(11);
  }
  // OR
  function fn(){
      console.log(11);
  }
  fn();
  // ---------------------------------------------------------
  // 4th Question
  // 4th Answer:Uncaught TypeError: fun is not a function
  fun();
  var fun = function(){
      console.log(22);
  }
  ```

* JavaScript 代码是由浏览器中的 JavaScript 解析器来执行的 , 或者叫 JS引擎

* JavaScript 解析器在运行 JavaScript 代码的时候分为两步 : 预解析和代码执行

* <1> 预解析 : JS引擎 会把JS里面所有的 var 变量声明以及 function 函数声明提升到当前作用域的最前面

* <2> 代码执行 : 按照代码书写的顺序从上往下执行代码

#### 预解析

> 预解析是面试的时候可能会问道的基本点

* 预解析分为 变量预解析 ( 变量提升 ) 和 函数预解析 ( 函数提升 )

* <1> 变量提升 : 就是把所有的变量声明提升到当前的作用域最前面 , 这仅仅提升变量的声明 , 而不提升赋值操作

  > 现在回看之前的 <kbd>2nd Question</kbd> , 我们可以这样解释它
  >
  > ```javascript
  > console.log(num2);
  > var num2 = 10;
  > // 上述代码相当于执行了以下代码
  > // 首先进行变量提升操作,即将变量声明提升
  > var num2;
  > console.log(num2);
  > num2 = 10;
  > ```
  >
  > 还有之前的 <kbd>4th Question</kbd> , 我们可以这样解释它 , fun 是一个
  >
  > ```javascript
  > fun();
  > var fun = function(){
  >  console.log(22);
  > }
  > // 上述代码相当于执行了以下代码
  > // 一样,首先进行变量声明
  > var fun;
  > fun(); // 此时执行出错,即声明的是变量,而不是函数
  > fun = function(){
  >  console.log(22);
  > }
  > ```

* <2> 函数提升 : 就是把所有的函数声明提升到当前作用域的最前面 , 这仅仅提升变量的声明 , 而不提升函数调用内容 , 也就是预解析并不调用函数

  > 现在就能解释之前的 <kbd>3rd Question</kbd> , 我们可以这样解释它
  >
  > ```javascript
  > fn();
  > function fn(){
  >  console.log(11);
  > }
  > // OR
  > function fn(){
  >  console.log(11);
  > }
  > fn();
  > // 上述代码相当于执行了以下代码
  > // 首先进行函数声明
  > function fn(){
  >  console.log(11);
  > }
  > // 调用函数的内容会被下放
  > fn();
  > ```
  >
  > <kbd>4th Question</kbd> 是用了函数表达式的情况 , 但是 <kbd>3rd Question</kbd> 是正常的函数声明和调用 , 这两者是有区别的

* 总结 : 

* 1. 我们 JS 引擎运行 JS 分为两步内容 : 即 预解析 + 代码执行

     <1> 预解析 : JS 引擎会把 JS 里面所有的 var 还有 function 提升到当前作用域的最前面

     <2> 代码执行 : 按照代码书写的顺序从上往下依序执行

  2. 预解析分为 变量提升 和 函数提升

     <1> 变量提升 : 把所有的变量声明提升到当前作用域的最前面 , **不提升赋值操作** 

     <2> 函数提升 : 把所有的函数声明提升到当前作用域的最前面 , **不调用函数** 

##### 案例-B

* 请判断以下代码的结果

  ```javascript
  var num = 10;
  fun();
  
  function fun(){
      console.log(num);
      var num = 20;
  }
  ```

  > 代码会先进行预解析 , 然后再执行 , 需要注意的是如何在作用域里 , 以及在哪个作用域里进行变量提升和函数提升

  ```javascript
  // 实际执行的内容相当于以下代码
  var num;
  function fun(){
      var num;
      console.log(num);
      num = 20;
  }
  num = 10;
  fun();
  // result : undefined -- 函数里仅仅进行了变量声明,没有赋值
  ```

##### 案例-C

* 请判断以下代码的结果

  ```javascript
  var num = 10;
  function fn(){
      console.log(num);
      var num = 20;
      console.log(num);
  }
  fn();
  ```

  > 和之前一样 , 预解析然后再进行代码执行操作

  ```javascript
  // 实际执行的内容相当于以下代码
  var num;
  function fn(){
      var num;
      console.log(num);
      num = 20;
      console.log(num);
  }
  num = 10;
  fn();
  // result : 
  // undefined -- 函数里开始仅仅进行了变量声明,没有赋值
  // 20 -- 函数里之后进行了变量赋值,值为 20
  ```

##### 案例-D

* 请判断以下代码的结果

  ```javascript
  var a = 18;
  f1();
  function f1(){
      var b = 9;
      console.log(a);
      console.log(b);
      var a = '123';
  }
  ```

  > 和之前一样 , 预解析然后再进行代码执行操作

  ```javascript
  // 实际执行的内容相当于以下代码
  var a;
  function f1(){
      var b;
      var a;
      b = 9;
      console.log(a); // undefined
      console.log(b); // 9
      a = '123';
  }
  a = 18;
  // 调用函数时没有传参,按照函数声明为准
  f1();
  // result : 
  // undefined -- 函数里开始仅仅进行了变量a的声明,但是没有赋值
  // 9 -- 函数里之后对变量b进行了变量赋值,值为 9
  ```

##### 案例-E

* 请判断以下代码的结果

  ```javascript
  f1();
  console.log(c);
  console.log(b);
  console.log(a);
  function f1(){
      var a = b = c = 9;
      console.log(a);
      console.log(b);
      console.log(c);
  }
  ```

  > 和之前一样 , 预解析然后再进行代码执行操作

  ```javascript
  // 实际执行的内容相当于以下代码
  function f1(){
      // var a = b = c = 9; 相当于下面的代码
      // var a = 9; b = 9; c = 9;
      // 即 b和c 是直接赋值,没有var声明,当全局变量看
      var a; // 局部变量
      a = b = c = 9;
      console.log(a); // 9
      console.log(b); // 9
      console.log(c); // 9
  }
  // 调用函数时没有传参,按照函数声明为准
  f1();
  console.log(c); // 9
  console.log(b); // 9
  console.log(a); // Uncaught ReferenceError: a is not defined
  ```



# JavaScript 基础 - 运算符和判断

----------------

> 所谓运算符 , 即操作符 , 是用于实现赋值 , 比较和执行算术运算等功能的符号.
>
> JS 中常用的运算符有 :
>
> * 算数运算符
> * 递增和递减运算符
> * 比较运算符
> * 逻辑运算符
> * 赋值运算符

--------------------------

### 算数运算符

------------------------

#### 算数运算符概述

* 算术运算使用的符号 , 用于执行两个变量或值的算数运算.

|  **运算符**  |   **描述**   |         **实例**         |
| :----------: | :----------: | :----------------------: |
| <kbd>+</kbd> |      加      |       10 + 20 = 30       |
| <kbd>-</kbd> |      减      |      10 - 20 = -10       |
| <kbd>*</kbd> |      乘      |      10 * 20 = 200       |
| <kbd>/</kbd> |      除      |      10 / 20 = 0.5       |
| <kbd>%</kbd> | 取余数(取模) | 返回除法的余数 9 % 2 = 1 |

* 在算数运算中 , 浮点数的算数运算会有一些可能的精度问题

* 比如下面这样的运算 : 

  ```javascript
  console.log(0.1 + 0.2); // 0.300000000000000004
  console.log(0.07 * 100); // 7.00000000000000001
  var num = 0.1 + 0.2;
  console.log(num == 0.3); // false
  ```

  > 直接使用小数参与运算 , 数字在转换为 2 进制运算并返回成 十进制 运算的过程中会产生误差
  >
  > 因此 <font color="#f44d59">尽量避免浮点数数直接运算的情况</font> 

#### △ 浮点数的精度问题

* 浮点数值的最高精度为 17 位小数 , 但是在进行算数计算时其精确度远远不如整数

  > <font color="#f44d59">**不要直接判断两个你认为应该相等的浮点数是否相等 !**</font>

#### 补充的一些思想

1. 我们如何判断一个数是否能够被整除呢 ?

   > 很简单 , 当余数为 0 的时候 , 就说明这个数能被整除 , 取余符号 ( % ) 的主要用途也就是这个

2. 需要注意 1 + 2 * 3 这种式子的运算优先级 .

   > 1 + 2 * 3 的结果为 7 , 注意算数运算符优先级 , 先乘除 , 后加减 , 有小括号的话先算小括号里面的

-------------------------

### 表达式和返回值

* 表达式 : 由数字 , 运算符 , 变量等以能求得数值的有意义的排列方法所得到的组合

  > 即由数字 , 运算符 , 变量等内容组成的式子 , 我们称之为表达式

* [PS] : <font color="#58bb58">表达式是有返回值的 , 并且表达式是将右边的结果赋值给左边的</font> 

------------------

### ★ 递增和递减运算符

* 为了解决变量持续或多次自增的问题 , 引入了递增和递减运算符

* 也就是把复杂的 `number = number +1;` 写为了 `num++` 或者 `++num` 的形式

  > 可以看到递增和递减运算符需要配合变量来进行使用

* 如果需要反复给数字变量添加或减去 1 , 可以使用 <font color="#f44d59">递增( ++ )和递减( -- )</font> 运算符来完成

  > 如果单独使用前置和后置自增 / 自减 , 其效果是一样的 , 只有在配合其他内容使用时才能显示出区别

* 在 JavaScript 中 , 递增和递减运算符即可以放在变量前也可以放在变量后 , 它们的区别为 :

  |      位置       |                       作用                       |
  | :-------------: | :----------------------------------------------: |
  | 前置递增 / 递减 | <font color="#f44d59">**先运算 , 后返回**</font> |
  | 后置递增 / 递减 | <font color="#f44d59">**先返回 , 再运算**</font> |

  ```javascript
  var p = 10;
  console.log(++p + 10); // 21,p 先自增变为 11,然后再和 10 相加得出 21
  var q = 10;
  console.log(p++ + 10); // 20,p 先返回值 10,同 10 相加得出 20 返回后,再自增变为 11 
  ```

#### ★ 相关练习 ( 笔面用 )

  ```javascript
var a = 10;
++a; // 11
var b = ++a + 2; // 12 + 2
console.log(b); // 14

var c = 10;
c++; // 11
var d = c++ + 2; // 11 + 2 = 13 , c + 1 = 12
console.log(d); // 13

var e = 10;
var f = e++ + ++e;
// (e++) + (++e),注意控制的是同一个变量
// 1. 无特殊顺序,按序计算,先算 e++,返回10,但是e值变为11
// 2. 再算 ++e,e值先变为 12,再返回,即12
// 3. 算两个返回值的和,即 10 + 12 =22
// 即结果为 22 ,但是 e 变为 12
console.log(f); // 22
  ```

#### 小结

* 前值递增和后置递增运算符可以简化代码的编写 , 让变量的值 +1 比以前的写法更简单
* 单独使用时 , 其运行结果相同
* 与其他代码连用时 , 结果不同 , 不论 ++a 还是 a++ 都要默认其有个小括号
* 注意前置和后置的区别 , 前置是先算后回 , 后置是先回后算
* 实际使用时 , 我们更多使用 i++ 这种形式 , 并且单独使用它 , 而不是和其他的去连用

---------------

### 比较运算符

* 比较运算符也称为关系运算符
* 即<font color="#e8f0d7">两个数据进行比较时所使用的运算符</font> , 比较运算后 , 会<font color="#7bc354">返回一个布尔值 ( true / false )</font> 作为比较运算的结果.

|   **运算符名称**    |           **说明**           |  **案例**   | **结果** |
| :-----------------: | :--------------------------: | :---------: | :------: |
|    <kbd><</kbd>     |            小于号            |    1 < 2    |   true   |
|    <kbd>></kbd>     |            大于号            |    1 > 2    |  false   |
|    <kbd>>=</kbd>    | 大于等于号 ( 大于或者等于 )  |   2 >= 2    |   true   |
|    <kbd><=</kbd>    |  小于等于号( 小于或者等于 )  |   3 <= 2    |  false   |
|    <kbd>==</kbd>    |  判等号 ( 会默认转型比较 )   |  37 == 37   |   true   |
|    <kbd>!=</kbd>    |            不等号            |  37 != 37   |  false   |
| <kbd>===  !==</kbd> | 全等 要求值和 数据类型都一致 | 37 === '37' |  false   |

* 当我们在运行以下代码时 , 会获得 true 的结果 , 即等于 ( == ) 操作会默认转换字符串类型为数字型再进行比较

  ```javascript
  console.log(18 == '18'); // true
  ```

* 为了禁止等于操作的默认转换 , 我们可以使用全等 ( === ) 操作进行判断比较

  ```javascript
  console.log(18 === '18'); // false,要求值和类型全等
  ```

* 为了便于对比 , 再确认一次 <kbd>=</kbd> 是赋值符号 , 而不是等于

-----------------

### 逻辑运算符

* 逻辑运算符是用来进行布尔值运算的运算符 , 其返回值也为布尔值
* 在实际开发中 , 逻辑运算符多用于判断 , 并且经常用于多个条件的判断情况

| **逻辑运算符**  | **说明** |    **案例**     |
| :-------------: | :------: | :-------------: |
|  <kbd>&&</kbd>  |  与 and  |  true && false  |
| <kbd>\|\|</kbd> |  或 or   | true \|\| false |
|  <kbd>!</kbd>   |  非 not  |     ! true      |

#### 逻辑与运算符 ( && )

```javascript
console.log(3 > 5 && 3 > 2); // false
```

> && 两侧都为 true , 结果才为 true , 只要有一侧为 false , 结果就为 false
>
> ![image-20210805162924665](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_basicfun_pic1.png) 

#### 逻辑或运算符 ( || )

```javascript
console.log(3 > 5 || 3 > 2); // true
```

> || 两侧都为 false , 结果才为 false , 只要有一侧为 true , 结果就为 true
>
> ![image-20210805163039110](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_basicfun_pic2.png) 

#### 逻辑非运算符 ( ! )

- 又称为 <font color="#a2cecb">取反符</font> , 用来取一个布尔值相反的值 , 如 true 的相反值是 false

```javascript
console.log(!true); // false
```

> 将其右侧表达式的结果颠倒 , 如果右侧表达式结果为 true , 逻辑非运算后结果变为 false

#### 相关练习

```javascript
var num = 7;
var str = "I love you my darling~"; // str.length=22

console.log(num >5 && str.length >= num); // true
console.log(num <5 && str.length >= num); // false
console.log(!(num < 10)); // false
console.log(!(num < 10 || str.length == num)); // false
```

-----------------------

### ★ 逻辑中断 ( 短路运算 )

* 当不是布尔值参与逻辑运算 , 而是值或者表达式参与逻辑运算的时候 , 其结果会有一些不同

* 比如 123 && 456 的时候 , 这种是值或者表达式参与逻辑运算时 , 其结果是什么呢 ?

  ★ **短路运算的原理 :** <font color="#f44d59">当有多个表达式 ( 值 ) 时 , 左边的表达式值可以确定结果时 , 就不再继续运算右边的表达式的值</font> 

-----------------------------

#### 逻辑与短路

* 语法 : <font color="#f44d59">表达式1 && 表达式2</font> 

* 如果 表达式1 的值为真 , 则返回 表达式2

* 如果 表达式1 的值为假 , 则返回 表达式1

  ```javascript
  console.log(123 && 456); // 456
  console.log(0 && 456); // 0
  console.log(0 && 456 && 1+3 && 68465); // 0
  ```

* 表示假的值有 : <font color="#f44d59">**0**</font> , <font color="#f44d59">**' '**</font> , <font color="#f44d59">**null**</font> , <font color="#f44d59">**undefined**</font> , <font color="#f44d59">**NaN**</font> 

* 除了上述的几种假值之外 , 其余的值均为真

------------

#### 逻辑或短路

* 语法 : <font color="#f44d59">表达式1 || 表达式2</font> 

* 如果 表达式1 的值为真 , 则返回 表达式1

* 如果 表达式1 的值为假 , 则返回 表达式2

  ```javascript
  console.log(123 || 456); // 123
  console.log(123 || 345 || 231); // 123
  console.log(0 || 345 || 231 + 123); // 345
  ```

* 当多个嵌套时 , 若 表达式1 为假 , 则从 表达式2 开始判断 , 直到判断出一个为真的 表达式n , 并返回 表达式n 

----------------

#### ▲ 逻辑短路的实际

```javascript
var num = 0;
console.log(213 || num++); // 213
console.log(num); // 0
```

* 逻辑短路 ( 中断 ) 会实际地影响到我们程序的运行结果

-------------------

### 赋值运算符

* 即用来把数据赋值给变量的运算符

  |    **赋值运算符**     |         **说明**         |           **案例**            |
  | :-------------------: | :----------------------: | :---------------------------: |
  |     <kbd>=</kbd>      |         直接赋值         |    var usrName = '我是值';    |
  |   <kbd>+=  -=</kbd>   | 加 , 减 一个 数 后再赋值 | var age = 10; age += 5; // 15 |
  | <kbd>*=  /=  %=</kbd> | 乘 , 除 , 取模 后再赋值  | var age = 2; age *= 5; // 10  |

* 我们知道 `num++` 表示的是自增 1 , 如果我们想要自增 2 , 自增 n 的话怎么办 ?

* 由此引出了赋值运算符的语法 , 用来给一个变量自增 m , 自减 n , 或者自乘 x ...

```javascript
var age = 10;
age += 5; // 相当于执行 age = age + 5;
age -= 5; // 相当于执行 age = age - 5;
age *= 10; // 相当于执行 age = age * 10;
```

-------------

### 运算符优先级

* 运算符的优先级按以下表格由上而下表示优先与否

| **优先级** |            **运算符**             |            **顺序**            |
| :--------: | :-------------------------------: | :----------------------------: |
|     1      |              小括号               |         <kbd>()</kbd>          |
|     2      | 一元运算符 ( 只需要一个运算变量 ) |       <kbd>++ -- !</kbd>       |
|     3      |     算数运算符 ( 二元运算符 )     | <kbd>**先 * / % 后 + -**</kbd> |
|     4      |            关系运算符             |      <kbd>> >= < <=</kbd>      |
|     5      |            相等运算符             |    <kbd>== != === !==</kbd>    |
|     6      |            逻辑运算符             |  <kbd>**先 && 后 \|\|**</kbd>  |
|     7      |            赋值运算符             |          <kbd>=</kbd>          |
|     8      |            逗号运算符             |          <kbd>,</kbd>          |

* 一元运算符里面的<font color="#cd102a">**逻辑非优先级很高**</font> 
* **逻辑与** 比 **逻辑或** 优先级高

---------------

#### 练习

```javascript
// 按照运算符的优先级,得出下面的内容结果
console.log(4 >= 6 || '人' != '阿凡达' && !(12 * 2 == 144) && true);
// 由于逻辑运算符在已有中权重最低,所以按逻辑运算符先分开
// 即 4 >= 6 , '人' != '阿凡达' , !(12 * 2 == 144) , true
// 分别算出结果,即 false , true , true , true
// 再算 false || true && true && true
// 逻辑与的权重大于逻辑或,故先算与的 true && true && true
// 结果为 true && true && true --> true && true --> true
// 再算 false || true , 结果为 true
var num = 10;
console.log(5 == num / 2 && (2 + 2 * num).toString() === '22');
// 由于逻辑运算符在已有中权重最低,所以按逻辑运算符先分开
// 即 5 == num / 2 , (2 + 2 * num).toString() === '22'
// 分别算出结果,即 true , (22).toString() === '22'--> true
// 得到结果为 true && true --> true
```

# JavaScript 基础 - 数组

------------------

> 之前学习的变量 , 只能存储一个值 , 如果我们想存储班级中所有学生的姓名 , 或者很多人的信息 , 则可以使用数组进行存储 , 数组可以把一组相关的数据一起存放 , 并提供方便的访问方式

## 数组

-----------

* 数组是指一组数据的集合 , 其中的每个数据被称作<font color=#25b2b8>元素</font> , 在数组中可以存放<font color=#e3318e>任意类型</font>的元素
* 换句话说 , 数组是一种将<font color=#e3318e>一组数据存储在单个变量名下</font>的优雅方式

```javascript
// 普通变量一次只能存储一个值
var num = 10;
// 数组一次可以存储多个值
var arr = [1,2,3,4,5];
```

### 创建数组的方式

#### 利用 new 创建数组

* ```javascript
  var arr = new Array(); // 创建了一个空的数组
  ```

  > 这种方式是通过对象创建的
  >
  > △ 注意 Array() 这里 A 是大写的

------------------------------

#### ★利用数组字面量创建数组

* ```javascript
  // 创建空数组
  var arrayName = [];
  // 创建带初始值的数组 (数组的初始化)
  var arrayName = ['white','black','yellow','Riky'];
  // 只有声明数组并赋值了才叫数组初始化
  
  // 数组中可以存放任意类型的数据,例如字符串,数字,布尔值
  var arrayStus = ['White',12,true,28.9];
  ```

  > 数据一定用逗号分隔 , 数组内的每个数据称为元素

### 获取数组元素

* 数组的索引 : 即下标 , 或者说就是元素的序号 , <font color=#d5de8c>从 0 开始</font> 

* 通过<font color=#cc0033>索引</font>来访问 , 设置 , 修改对应的数组元素 ( 访问即获取 , 得到的意思 ) , 我们可以通过 <font color=#cc0033>**arrayName[index]**</font> 的形式获取数组中的元素

  ```javascript
  let arr = [1,2,3];
  // 获取整个数组
  console.log(arr);
  // 获取数组的第三个元素 2
  console.log(arr[2]);
  // 由于没有第四个元素,故输出结果为 undefined
  console.log(arr[3]);
  ```


### 遍历数组

* 遍历数组 , 就是把数组中的每个元素从头到尾都访问一次 ( 类似我们每天早上学生的点名 )

* 使用循环可以方便地取出数组中的所有元素

  ```javascript
  let arr = [1,2,3,4,5,6,7,8,9,10]
  // 从0开始就不要再等于10了,否则得有11个元素才行
  for(let i = 0; i < 10; i++){
      console.log(arr[i]);
  }
  // 多加一步,计算数组的平均数
  let sum = 0;
  let average = 0;
  for(let i = 0; i < arr.length; i++){
      sum += arr[i];
  }
  average = sum / arr.length;
  console.log('The average of array is : ' + average);
  // 输出多个变量,用逗号分隔即可
  console.log(sum , average);
  ```

### 数组长度

* 当数组中的元素无法用肉眼输出来的时候 , 我们需要借助计算机来进行判断 , 即获取数组的 length
* 使用 <font color=#cc0033>**arrayName.length**</font> 可以访问数组元素的数量 ( 即数组的长度 )

> 数组的长度不要和索引号混淆 , 索引一般都比长度少一

------------------

### 数组案例

#### 案例A-求数组最大值

> 按照冒泡排序的思路 , 通过一个元素不断打擂台从而确定此元素是最大值
>
> 求一个数组元素中的最小值同理

```javascript
let arr = [12,58,46,33,11,18,99,55,44,125];
let maxNum = 0;
for(let i = 0; i < arr.length; i++){
    if(arr[i] > maxNum){
        maxNum = arr[i];
    }else{
        continue;
    }
}
console.log('The max number of this array is :' + maxNum);
```

#### 案例B-数组转换为分割字符串

> 在日常处理 JSON 格式内容的时候 ( 比如爬虫或者读取数据内容 ) , 经常需要分割字符串并将其内容保存在一个数组中 , 这里的这个案例能很好地帮助我们思考这种行为之后的行为

```javascript
// 假如我们切割出了这样一段文字,我们需要对其进行处理
let arr = ['red','green','black','blue','yellow'];
let str = '';
let sep = '!';
for(let i = 0; i < arr.length; i++){
    str += arr[i] + sep;
}
console.log(str);
```

### ★数组新增元素

* 当我们发现一个已有数组无法满足需求的时候 , 想要不修改其内容的情况下添加新内容 , 有以下方法可以实现这个效果

-------------------

#### **通过修改 length 长度添加元素**

* length 属性是可读写的~

  ```javascript
  let arr = ['red','green','black'];
  console.log(arr.length);
  // 手动修改数组长度
  arr.length = 5;
  console.log(arr); // 结果为 ['red','green','black',empty x 2]
  console.log(arr[4]); // undefined
  ```

-------------------

#### **通过索引号增加元素**

* 换句话说 , 就是直接追加元素 , 如果索引是已经有内容的 , 内容会被替换

  ```javascript
  let arr = ['red','green','black'];
  arr[3] = 'pink';
  console.log(arr); // ['red','green','black','pink']
  arr = 'Final'; // 直接赋值给数组会将数组变成一个字符串变量
  ```

  > 这种直接追加的方式更为常用

* 我们有时候可以通过循环创建数组 , 之后需要添加内容的话直接修改下循环计数器即可

  ```javascript
  // 给数组里依次填入数字,只使用循环计数器即可实现
  let arr = [];// 要给数组添加100个数字,直接输入要疯掉
  for(let i = 0; i < 100; i++){
      arr[i] = i + 1;
  }
  console.log(arr);
  ```

------------

#### 案例C-筛选数组

* 要求就是将一个数组中大于或者小于 N 的数筛选出来,形成一个新的数组

  ```javascript
  // 方法1
  let arr = [2,0,6,1,77,0,52,0,25,7,94,55,33,12,8];
  let resultArr = [];
  let counter = 0;
  for(let i = 0; i < arr.length; i++){
      if(arr[i] > 10){
          resultArr[counter] = arr[i];
          counter++;
      }else{
          continue;
      }
  }
  console.log(resultArr);
  // 方法2
  // 我们知道数组的长度会自动变化,借此可以省略计数器
  let arr = [2,0,6,1,77,0,52,0,25,7,94,55,33,12,8];
  let resultArr = [];
  for(let i = 0; i < arr.length; i++){
      if(arr[i] > 10){
          resultArr[resultArr.length] = arr[i];
      }else{
          continue;
      }
  }
  ```

* 删除指定元素的案例和这个思路差不多 , 只是条件改变了

  > 需要注意的就是<font color="#6fe2ff">**通过 length 可以实现消除额外计数器的效果**</font> 

#### 案例D-翻转数组

* 顾名思义 , 就是把一个数组元素的个数翻过来存放 , 类似于栈的操作 , 后进先出

  ```javascript
  let arr = [1,2,3,4,5,6,7,8,9,10];
  let newArr = [];
  // 长度和索引差一,少一个就要添上等于的条件
  for(let i = arr.length - 1; i >= 0; i--){
      // newArr长度是不断增加的
      newArr[newArr.length] = arr[i];
  }
  console.log(newArr);
  ```

### ★数组排序-冒泡排序

* 首先回想一下交换两个变量值的脚本 , 这种代码只需要修改原始的两个变量值就能实现转换

  ```javascript
  let num1 = 10;
  let num2 = 20;
  let temp;
  temp = num1;
  num1 = num2;
  num2 = temp;
  ```

* 由此我们有了冒泡排序的基本思路--即交换变量

* 所谓冒泡排序 , 就是对比数组中两个相邻的数 , 并将大数往前放 , 这种效果就是通过交换变量实现的

* 经过有限次的对比和交换之后 , 我们会得到一个从小到大或从大到小排列的数组 , 从而就实现了排序

  ```javascript
  // 一般调用冒泡排序,仅仅针对一个数组进行操作
  let arr = [1, 5, 2, 4, 6, 3, 9, 8, 7, 10, 15, 14, 12, 13, 11];
  //*******************************冒泡排序开始*******************************
  
  // 临时用于交换数的变量,声明在外面就不需要每次循环都创建它了
  let tempNum;
  // 每次都会对比两个数,这样算下来每次只需要执行比数组长度少一的轮次即可 
  for (let j = 0; j < arr.length - 1; j++) {
    // 临时变量在每轮循环都初始化
    tempNum = arr[0];
    // 每一轮都会摆好一个数,且在最后,而此时外层循环变量刚刚好会加一
    // 由此可知内层需要比较的次数即数组长度减去轮数即可
    for (let i = 1; i < arr.length - j; i++) {
      // 临时变量存的是前一个数,这里直接从第二个数即索引为一的元素开始比较
      if (arr[i] >= tempNum) {
        // 若元素大于临时变量,则保存此元素内容给临时变量
        // 第二个元素要是大于第一个元素,那么也不需要换位置了,直接下一步即可
        tempNum = arr[i];
      } else {
        // 若元素小于临时变量,由于临时变量存的是前一个数的值,则交换这两个位置的元素
        arr[i - 1] = arr[i];
        arr[i] = tempNum;
      }
    }
  }
  
  //*******************************冒泡排序结束*******************************
  
  // 输出数组检查结果
  console.log(arr);
  ```

* 上面的注释可能太多了,这里是没有注释的版本

  ```javascript
  let arr = [1, 5, 2, 4, 6, 3, 9, 8, 7, 10, 15, 14, 12, 13, 11];
  let tempNum;
  for (let j = 0; j < arr.length - 1; j++) {
    tempNum = arr[0];
    for (let i = 1; i < arr.length - j; i++) {
      if (arr[i] >= tempNum) {
        tempNum = arr[i];
      } else {
        arr[i - 1] = arr[i];
        arr[i] = tempNum;
      }
    }
  }
  console.log(arr);
  ```

* 同理实现由小到大排列 , 把判断条件的大于等于改成小于等于即可

  ```javascript
  let arr = [1, 5, 2, 4, 6, 3, 9, 8, 7, 10, 15, 14, 12, 13, 11];
  let tempNum;
  for (let j = 0; j < arr.length - 1; j++) {
    tempNum = arr[0];
    for (let i = 1; i < arr.length - j; i++) {
      if (arr[i] <= tempNum) {
        tempNum = arr[i];
      } else {
        arr[i - 1] = arr[i];
        arr[i] = tempNum;
      }
    }
  }
  console.log(arr);
  ```

* [PS] : 冒泡排序只是一种最简单的算法 , 其实排序甚至其他有关数组的算法还有很多 , 之后可以在算法部分专门看这些内容 , 而不是再回来写到数组这里

# JavaScript基础 - 进阶知识

---------------------

## 流程控制

* 在一个程序执行的过程中 ,  各条代码的执行顺序对程序的结果是有直接影响的
* 很多时候我们需要通过控制代码的执行顺序来实现我们要完成的功能

> 即 : <font color="#dab5d6">**流程控制就是来控制我们的代码按照什么结构顺序来执行**</font> 

* JS 中有三种流程控制结构 , 即 <font color="#dfd282">顺序结构</font> , <font color="#dfd282">分支结构</font> , <font color="#dfd282">循环结构</font> , 这三种结构代表三种代码执行的顺序

  ![image-20210806181052880](F:\LearningNotes\JavaScriptLearning\JS_advanced_pic1.png) 

-----------------------

## 顺序流程控制

* 顺序结构是程序中最简单 , 最基本的流程 , 没有特定的语法结构
* 即 <font color="#fa0a7c">程序按照代码的先后顺序 , 依次执行</font> , 程序中大多数的代码都是这样执行的 , 流程图如上图

----------------

## 分支流程控制

* 分支结构 : 由上到下执行代码的过程中 , 根据 <font color="#fa0a7c">不同的条件</font> , 执行 <font color="#fa0a7c">不同的路径代码</font> ( 执行代码多选一的过程 ) , 从而得到 <font color="#fa0a7c">不同的结果</font> , 一般用 **if 语句** 来完成这种流程 , 但是还有 **switch 语句** 也具有这种效果

### if 分支语句

* 其语法结构类似如下代码 , 具体的执行流程见下方左图

  ```javascript
  if ( 条件 ){
  	// 执行内容
  }
  // 例子
  if ( 3 > 5 ){
      alert('沙漠骆驼'); // 此内容不显示 , 因为 3 > 5 为 false
  }
  ```

  > 执行思路 : 若 if 的条件为真 , 则执行大括号里面的执行内容 , 否则不执行大括号里面的内容 , 执行 if 句块之后的代码

* ![单一if分支语句流程](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_advanced_pic2.png) ![if 双分支语句流程](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_advanced_pic3.png) 

### if 双分支语句

* 当我们想要在 if 条件 为 false 时也执行内容 , 可以使用以下的语法结构 , 具体流程如上方右图

  ```javascript
  if ( 条件 ){
      // 内容 1
  } else {
      // 内容 2
  }
  // 例子
  var age = prompt('Please press your age:');
  if (age >= 18){
      alert('我们去网吧走~');
  }else {
      alert('回家做作业去~');
  }
  ```

  > 执行思路 : 若 if 的条件为真 , 则执行内容1 , 否则执行内容2
  >
  > [PS] 值得注意的是 : 
  >
  > 1 . <font color="#fa0a7c">内容1 和 内容2 只有一个会被执行 </font> 
  >
  > 2 . <font color="#fa0a7c">else 后面是不存在判断条件的</font> 

### if-else-if 多分支语句

* 往往我们在实际判断的时候并不会只有"是和否"这样的双分支情况 , 我们一般会有多个情况分支用来进行判断
* 由此 **if-else-if** 就作为判断不同条件而选择不同语句执行的多分支语句出现了 [理论上能有无穷多个条件分支]
* ![](D:\GitHubFiles\LearningNotes\JavaScriptLearning\JS_advanced_pic4.png) 

```javascript
if (条件1){
    // 内容1
    // 注意 else if 中间是有空格的
}else if(条件2){
    // 内容2
}else if(条件3){
    // 内容3
}else if(条件n){
    // 内容n
    // .......
}else{
    // 最后の内容 上述皆不成立则执行此内容
}
```

> if-else-if 语句在执行满足任意一个条件的内容之后结束整个多分支语句
>
> <font color="#fa0a7c">内容1 , 内容2 , 内容n ... 只有一个会被执行 即多选一</font> 
>
> [PS] 只要执行到某一个 else , 就代表之前的 if 条件是不满足的 , 这样可以省略一些条件内容

### ★三元表达式

* 三元表达式是由三元运算符组成的式子 , 其性质类似于双分支语句 , 可以实现一些简单的条件选择

  > **一元  ++n** 
  >
  > **二元  3+5 ** 
  >
  > **三元  a?b:c **

* **语法结构** : <font color="#f66bd1">条件表达式 ? 表达式1 : 表达式2</font> 

* **执行思路** : 如果<font color="#f66bd1">条件表达式结果</font>为真 , 则返回 <font color="#f66bd1">表达式1</font> 的值 , 否则返回 <font color="#f66bd1">表达式2</font> 的值

```javascript
let num = 10;
var result = num > 5 ? 'yes' : 'nope'; // 返回 yes
console.log(result);
// 上述三元表达式功能类似于以下代码
// if (num > 5){
//     result = 'yes';
// }else{
//     result = 'nope';
// }
```

#### 案例 : 数字补0

> 要求 : 
>
> 用户输入数字 , 如果数字小于10 , 则在前面补0 , 比如 01 , 09
>
> 如果数字大于 10 , 则不需要补 , 比如 20

> 思路 :
>
> 通过一个判断就能解决 , >10 的情况以及 <10 的情况

```javascript
let time = prompt('plz press a number in 0~59');
// 使用三元表达式返回值,一行代码搞定业务
let result = time < 10 ? '0'+time : time;
alert(result);
```

---------------------------------

### ★switch 语句

* switch 语句也是一种多分支语句 , 用于基于不同条件执行不同的代码

* 当要针对变量设置一系列的<font color=#f370de>特定值</font>的选项时 , 就可以使用 switch 语句

* **语法结构** : switch 意为开关 , case 表示小例子或者选项的意思

  ```javascript
  switch(表达式) {
      case value1:
          // 表达式 等于 value1 时的执行语句;
          break;
      case value2:
          // 执行语句2;
          break;
          ...
      case valuen:
          // 执行语句n;
          break;
      default:
          // 执行最后的/没有匹配的语句;
          // 这里可以不用break,因为switch句柄只会执行一轮
  }
  ```

* **执行思路** : 

* 表达式的值须和 case 之后的选项值相匹配

* 如果匹配上 , 就执行该 case 中的语句 ; 

* 如果没有匹配上 , 那么执行 default 里面的语句

```javascript
// 代码示例
let yourCase = prompt('your case');
switch (yourCase){
    case 1:
        console.log('case 1');
        break;
    case 2:
        console.log('case 2');
        break;
    default:
        alert('This is default');
        break;
}
```

#### Switch 的注意事项

* 在开发时 , 一般将 switch 句柄中的表达式写为一个变量

* 在匹配时 , 表达式的值和 case 后的值是全等 ( === ) 的匹配关系 , 即数值和数据类型都相等

* break 并不是必须写的内容 , 但是为了防止依序执行程序导致选项无效 , 加上 break 可以实现执行跳转

  > 依序执行程序 : 即如果当前的 case 里面没有 break 则不会退出 switch 句柄 , 而是继续执行下一个 case

------------------------------

### ★switch 语句和 if-else类 语句的区别

* 一般情况下 , 两者是可以相互替换的
* **switch 语句** 通常用于处理 case 值较为确定的情况
* **if-else 语句** 更加灵活 , 常用于范围判断 ( 大于 , 等于某个范围的情况 )
* **switch 语句** 进行条件判断之后直接执行到程序的条件语句 , 效率更高 , 而 **if-else 语句** 有几种条件 , 就得判断多少次 , 从运算量来说 **if-else** 语句更耗时
* 当分支比较少的时候 , **if-else 语句** 的执行效率比 **switch 语句** 高
* 当分支比较多的时候 , **switch 语句** 的执行效率比较高 , 并且会使程序结构更加清晰

-----------------------------

## 循环控制语句

--------------------------------

### 循环

* 在实际问题中 , 有许多具有<font color=#deec95>规律性的重复操作</font> , 因此在程序中要完成此类操作就需要<font color=#deec95>重复执行某些语句</font> 

```javascript
// 循环道歉100次,注意这里i从1开始算起
for (let i = 1; i <= 100; i++){
    console.log('Sorry'); // 执行100次
}
```

* JavaScript 中 , 主要有三种类型的循环语句 : 
  * for 循环
  * while 循环
  * do...while 循环

* 在程序中 , 一组被重复执行的语句叫<font color=#44e0a6>循环体</font> , 能否继续重复执行 , 取决于循环的<font color=#44e0a6>终止条件</font>
* 由循环体及循环的终止条件组成的语句 , 被称之为<font color=#44e0a6>**循环语句**</font>

------------------------

#### for 循环

* for 循环主要用于把某些代码循环若干次 , 通常跟 计数 有关系

* 语法结构 : 

  ```javascript
  for( 初始化变量 ; 条件表达式 ; 操作表达式 ){
      // 循环体
  }
  ```

* **初始化变量** : 就是一个普通变量 , 不过此变量一般用于循环中的计数 , <font color=#f80c73>此句内容在循环中仅仅执行一次</font> 

* **条件表达式** : 就是用来决定每一次循环是否继续执行 , 即终止的条件 , 满足条件则执行循环体 , 否则退出循环

* **操作表达式** : 每次循环后执行的代码 , 通常用于我们计数器变量进行更新 ( 即计数器的递增或递减 )

  ```javascript
  let time = prompt('plz press a number in 0~59');
  // 使用三元表达式返回值
  let result = time < 10 ? '0' + time : time;
  // 通过循环输出多行
  for (let i = 0; i <= 10; i++) {
    console.log(result);
  }
  ```

* 我们可以让用户控制输出的次数

  ```javascript
  var num = prompt('plz press times')
  for (let i = 0; i <= num; i++) {
      console.log(num);
  }
  ```

---------------------------

#### for 循环重复不相同的代码

* for 循环还可以重复不同的代码 , 这主要是因为使用了计数器 , 计数器在每次循环过程中都会有变化

* 通过对计数器内容进行判断 , 就可以实现在不同情况下重复执行不同的代码了

  ```javascript
  for (let i = 0; i <= 100; i++) {
      if(i == 1){
          console.log('这个人今年1岁了,他出生了');
      }else if(i == 100){
          console.log('这个人生前是个体面人');
      }else{
          console.log('这个人今年' + i + '岁了');
      }
  }
  ```

----------------------

#### ★for 循环重复某些相同操作

* for 循环因为有了计数器的存在 , 我们还可以重复地执行某些操作 , 比如做一些算术运算

##### 案例 A : 求 1~100 之间所有奇数和偶数的累加和

```javascript
let sumOdd = 0;
let sumEven = 0;
for (let i =0; i <=100; i++) {
    // 分别算出奇偶数的和
    if (i % 2 == 1){
        console.log(i); // 每次都输出一下i
        sumOdd = sumOdd + i; // 也可以是 sumOdd += i
    }else if (i % 2 == 0){
        console.log(i); // 每次都输出一下i
        sumEven = sumEven + i; // 也可以是 sumEven += i
    }else {
        console.log('not a number in 1~100');
    }
}
console.log('sumOdd = ' + sumOdd); // 2500
console.log('sumEven = ' + sumEven); // 2550
```

##### 案例 B : 求 1~100 之间所有数的平均值

```javascript
// 先求和
let sum = 0;
let average = 0;
for (let i = 0; i <=100; i++) {
    sum = sum + i;
}
console.log('sum = ' + sum); // 5050
average = sum / 100;
console.log('ave = ' + average); // 50.5
```

##### 案例 C : 求班级的平均分

```javascript
let sum = 0;
let average = 0;
let num = prompt('plz press num of class');
for(let i = 1; i <= num; i++) {
    let score = prompt('plz enter the score of the number of ' + i + ' student');
    // 由于prompt返回的是字符串,故不强制转换会导致内容被强制定位字符串类型
    sum = sum + parseFloat(score); // 任何内容加字符串结果都是字符串
}
console.log('sum is ' + sum);
average = sum / num;
console.log('average is ' + average);
```

-----------------

#### 双重嵌套 for 循环

* 很多情况下 , 单层的 for 循环并不能满足我们的需求 , 比如我们要打印一个 5 行 5 列的图形 , 打印一个倒直角三角形等 , 此时就可以通过循环嵌套来实现.

* <font color=#d5788b>**循环嵌套**</font> , 是指<font color=#d5788b>在一个循环语句中再定义一个循环语句的语法结构</font> , 例如在 for 循环中 , 可以再嵌套一个 for 循环 , 这样的 for 循环语句我们称之为 <font color=#d5788b>双重for循环</font>

* **语法结构** : 

  ```javascript
  for (外层初始化变量 ; 外层条件表达式 ; 外层操作表达式){
      for (内层初始化变量 ; 内层条件表达式 ; 内层操作表达式){
          // 执行语句
      }
  }
  ```

  > 我们可以把内层的循环看做外层循环的语句
  >
  > 外层循环执行一次 , 内层循环执行一整轮

* **代码验证** : 

  ```javascript
  for (let i = 1; i <= 3; i++) {
      console.log('这是外层的第' + i + '次循环');
      for (let j = 1; j <= 4; j++) {
          console.log('这是内层的第' + j + '次循环');
      }
  }
  ```

  

##### ★案例 D : 用循环的方式打印星星 ( 双重 for 循环 )

* 打印五行五列的星星

  > 这个思路很简单 , 嵌套循环 , 一个是循环行 , 一个是循环列 , 每行 5 个 , 共打印 5 行

```javascript
let str_block = ""; // 空格
// 负责打印五行
for (let i = 1; i <= 5; i++) {
   // 负责一行打印五个星星,记得换行
   for (let j = 1; j <= 5; j++) {
   	// 为了最终显示,需要直接把结果慢慢保存给变量
    str_block = str_block + '★';
   }
   str_block = str_block + "\n";
}
console.log(str_block);
```

* 如果之后可以的话 , 可以把循环变量设置为可以用户自选的 , 这样就能实现打印 n 行 n 列的内容了

##### ★案例 D : 用循环的方式打印三角形的星星 ( 双重 for 循环 )

* 在实现循环打印的时候 , 正三角形 , 倒三角形 , 以及金字塔形都是常规的循环打印效果

* A : 打印倒三角形 ( 正 , 倒三角形是不需要打印空格的 )

  > 在外层循环中 , 显然外层的循环变量是不断增加的 , 那么内层每次都从外层循环变量的值开始算 , 这样每一次外层循环的迭代都会使内层循环次数变少

  ```javascript
  // 倒置三角形
  let starS = '';
  for (let i = 1; i <= 10; i++){
      for (let j = i; j <=10; j++){
          starS = starS + '★';
      }
      starS = starS + '\n';
  }
  console.log(starS);
  ```

* B : 打印正三角形 ( 正 , 倒三角形是不需要打印空格的 )

  > 如果是正置三角形 , 那么就是从星星最少的排数开始 , 并且对内层的循环进行次数控制

  ```javascript
  // 正置三角形
  let starS = '';
  for (let i = 1; i <= 10; i++){
      for (let j = 11-i; j <= 10; j++){
          starS = starS + '★';
      }
      starS = starS + '\n';
  }
  console.log(starS);
  ```

* C : 打印九九乘法表

  > 我们知道 i 和 j 的值会不断变化 , 刚刚好就能利用到它们 , 根据乘法表的规律 , 可以知道第二个乘数也代表着排数 , 刚刚好就能用到 i , 每一排最后一个式子必是 i = j 的情况 , 由此写出以下代码

  ```javascript
  let starS = ''; // 用来保存乘法表
  let strTe = ''; // 用来保存单个式子
  for (let i = 1; i <= 9; i++) {
    // 每一行的式子数刚刚好就是行数,使用j<=i来实现这个效果
    for (let j = 1; j <= i; j++) {
      // 每个式子都有 a*b=c 这样的形式
      strTe = j + 'x' + i + '=' + i * j;
      // 当结果大于10后会多占用空格,所以为了格式化需要做这样一个判断
      if (i * j >= 10) {
        starS = starS + strTe + ' ';
      } else {
        starS = starS + strTe + '  ';
      }
      // 使用下面的代码也可以达到上述效果,即使用换行符,不需要判断
      // starS = starS + strTe + '\t';
    }
    // 每行换行
    starS = starS + '\n';
  }
  console.log(starS); // 打印乘法表
  ```

* D : 打印等腰三角形 ( 考虑到打印空格的情况 )

  > 一般来说 , 这种三角形的打印实际上是一行中既打印空格也打印五角星的情况 , 空格即一个倒三角形 , 五角星需要呈现奇数型打印 , 即第一行打印一个 , 第二行打印三个 , 以此类推 ...
  >
  > 循环还是两层循环 , 只不过内层有两个循环进行打印内容

  ```javascript
  let starS = "";
  for (let i = 1; i <= 10; i++) {
    // 输出空白,大概2个空白占一个星星的位置
    for (let j = i; j <= 10; j++) {
      starS = starS + "  ";
    }
    // 输出星星,按奇数个数进行输出
    for (let j = 11 - (2 * i - 1); j <= 10; j++) {
      starS = starS + "★";
    }
    // 每输出一行就换行
    starS = starS + "\n";
  }
  console.log(starS);
  ```

---------------------------------

#### for 循环小结

* for 循环可以重复执行某些相同的 , 或有某种规律的代码
* for 循环可以重复执行某些操作 , 比如算数运算的加法等操作
* 通过多重 for 循环可以直接实现一些指数级的问题 , 如双重循环 , 外层迭代一次 , 内层执行一次完整的循环
* for 循环的条件和数字直接相关
* 在循环中 , 分析思路远比代码重要 , 一些核心算法也是同理 , 并不是要会它的代码 , 而是要学会它的执行思路

---------------------------

#### while 循环

* 与 for 循环 的 先执行一次然后判断 不同 , while 循环语句是在条件表达式为真的前提下 , 再循环执行指定的一段代码 , 直到表达式不为真时结束循环 , 其语法结构如下

  ```javascript
  // while loop
  while (条件表达式){
      // 循环体
  }
  ```

* **执行思路** : 

  1. 先执行条件表达式 , 若结果为 true , 则执行循环体代码 ; 如果为 false , 则退出循环 , 执行后面的代码
  2. 执行循环体代码 , 需要注意的是 , 操作表达式 ( 计数器加减 ) 是写在循环体中的
  3. 循环体代码执行完毕之后 , 程序会继续判断执行条件表达式 , 如果条件仍为 true , 则会继续执行循环体 , 直到循环条件为 false 时 , 整个循环过程才会结束

  ```javascript
  let num = 1;
  while (num <= 100){
      console.log('This is the ' + num + ' times');
      num++; // 千万别写成死循环
  } // 正好100句
  ```

* 优势 :

  * 相比于 for 循环 , while 循环能够进行更为复杂的判断 , 比如字符串是否相等

    ```javascript
    let message = prompt('Do you love me?');
    // while能判断一些更为复杂的情况
    while (message !== 'Yes'){
        message = prompt('Do you love me?');
    }
    alert('I love you too ~~');
    ```

------------------------

#### do-while 循环

* do-while 循环其实是 while 循环的变体 , 其循环结构为 : 

  ```javascript
  // do-while loop
  do {
      // 循环体
  } while (条件表达式)
  ```

* **执行思路** : 

  1. 与 while 不同的是 , do-while 会先执行一次循环体 , 之后再进行判断 , 若判断为真则继续迭代 , 否则跳出循环
  2. 也就是 do-while 循环必定会执行一次循环体

  ```javascript
  let i = 1;
  do {
      console.log('This is the ' + i + ' times');
      i++;
  } while ( i <= 10 )
  // 同样的,do-while也可以进行一些特殊的判断条件
  let message = '';
  do {
      message = prompt('Do you love me?');
  } while ( message !== 'Yes' )
  alert('I love you too~~');
  ```

-------------------

#### 循环小结

* 循环有 for , while , do-while 循环三种 , 最重要的是 for 循环 , 它是工作中最常用的
* 三种循环大部分情况下可以相互替代 , 在循环条件只是与数字相关时 , 更推荐用 for 循环
* while 和 do-while 循环可以做更加复杂的判断 , 比 for 循环灵活
* while 和 do-while 的区别在于循环的执行顺序不同 , do-while 总会先执行一次循环体 , while 可能不执行

---------------

#### continue 和 break

* **continue**关键字用于<font color="#c4332f">**立即跳出本次循环**</font> , 继续进行之后的循环 ( 循环体中 continue 后的代码会被跳过 )

  ```javascript
  for ( let i = 1; i <= 5; i++){
      if (i == 3){
          // 遇见continue,直接跳过之后的循环体
          continue;
      }
      console.log('This is the ' + i + ' times');
  }
  ```

* 案例 : 求 1~100 之间 , 除了能被 7 整除之外的数代码如下

  ```javascript
  for ( let i = 1; i <= 100; i++){
      if ( i % 7 == 0){
          continue;
      }
      console.log(i);
  }
  ```

* **break**关键字用于<font color="#c4332f">**跳出整个循环**</font> ( 直接结束循环 )

* 比如按照顺序输出 1~100 的数 , 当输出的数为 33 时 , 直接跳出循环

  ```javascript
  for ( let i = 1; i <= 100; i++){
      if ( i == 33 ){
          console.log(i);
          break;
      }
      console.log(i);
  }
  ```

--------------------

### 案例

* 求整数 1~100 的累加值 , 但要求跳过所有个位为3的数

```javascript
let sum = 0;
for ( let i = 1; i <= 100; i++){
    if ( i % 10 == 3 ){
        continue;
    }
    console.log('i is ' + i);
    sum += i;
}
console.log(sum);
```

* 可以创建一个简单的文字 ATM 机 , 要求为 : 
  1. 里面原本有 100 块
  2. 有四种情况 , 取钱 , 存钱 , 显示余额 , 退出
  3. 如果存钱 , 就输入存的钱 , 之后提示余额
  4. 如果取钱 , 就输入取的钱 , 之后提示余额
  5. 如果显示余额 , 就直接显示
  6. 如果退出 , 就弹出退出提示

```javascript
let money = 100;
let tempMoney = 0;
while (money) {
  let yourcase = prompt("Plz press the thing you want to do:\n1.Save money\n2.Take money\n3.Show your money\n4.Exit the ATM");
  switch (yourcase) {
    case "1":
      tempMoney = prompt("Plz enter the money you save:");
      money = money + parseFloat(tempMoney);
      if (money < 0) {
        alert("You are a poor guy now , go get your money!");
      } else {
        alert("You have " + money + " RMB now.");
      }
      break;
    case "2":
      tempMoney = prompt("Plz enter the money you take:");
      money = money - parseFloat(tempMoney);
      if (money < 0) {
        alert("You are a poor guy now , go get your money!");
      } else {
        alert("You have " + money + " RMB now.");
      }
      break;
    case "3":
      if (money < 0) {
        alert("You are a poor guy now , go get your money!");
      } else {
        alert("You have " + money + " RMB now.");
      }
      break;
    case "4":
      money = null;
      alert("You have exit the ATM now.");
      break;
  }
}
```

--------------------------------------

## [断点调试]

* 断点调试是指自己在程序的某一行设置一个断点 , 调试时 , 程序运行到这一行就会停住 , 然后你可以一步一步往下调试 , 调试过程中可以看各个变量当前的值 , 出错的话 , 调试到出错的代码行即显示错误 , 停下.
* <font color=#f80c73>**断点调试可以帮助我们观察程序的运行过程**</font> 
* 浏览器中按 <kbd>F12 → sources → 找到需要调试的文件 → 在程序的某一行设置断点</kbd> 
* Watch : 监视 , 通过 watch 可以监视变量的值的变化 , 非常的常用
* F11 : 程序单步执行 , 让程序一行一行地执行 , 这个时候 , 观察 watch 中变量的值的变化
* 代码调试的能力非常重要 , 只有学会了代码调试 , 才能学会自己解决 bug 的能力

# JavaScript基础 - 函数

-------------------------

> 为了防止多次重复编写相同逻辑或功能相似的代码 , 而这些代码一般都会大量使用到时
>
> 我们需要定义这组相同的代码 , 将其装配成一个盒子 , 从而实现每次需要它只来拿盒子即可的
>
> 这样一种随取随放的形式 , 这种逻辑虽然能有多种实现 , 但是我们一般会使用函数来解决这种问题

* <font color="#bce842">**函数 :**</font> 就是**封装**了一段<font color="#e13d6d">可以被重复调用执行的**代码块**</font> , 通过此代码块可以实现代码的重复使用 ( 即复用 )

  > 封装 : 就是把一个或多个功能装配在一个函数里面 , 对外只提供一个简单的函数接口

* 比如之前我们写过的累加和 , 我们可以通过定制起始数达到建立一个函数的效果

  ```javascript
  fuction getSum(num1 , num2){
      let sum = 0;
      for(let i = num1; i <= num2; i++){
          sum += i;
      }
      console.log(sum);
  }
  // 计算 1~100 的累加和
  getSum(1,100);
  // 计算 1~2000 的累加和
  getSum(1,2000);
  ```

### 函数的使用

* 函数在使用时分为两步 , 声明函数 和 调用函数

  > 上例中的 <kbd>function getSum(num1,num2)</kbd> 区块就是函数的声明区块
  >
  > <kbd>getSum(1,2000)</kbd> 就是调用函数

#### 函数的声明

* **function** 是函数的关键字 , 函数声明的语法结构为

  ```javascript
  // 函数名一般是动词
  function funName(){
      // 函数体
  }
  ```

* 函数声明和调用虽然是分开进行的 , 但是函数不调用就不会执行

* <font color="#38d8a3">**[注] 声明函数本身并不会执行代码 , 只有调用函数时才会执行函数体的代码**</font>

#### 函数的调用

* 假如我们有一个函数

  ```javascript
  function sayHello(){
      console.log('Hello world');
  }
  ```

* 那么调用它很方便 , 直接使用 <kbd>函数名(参数)</kbd> 的形式即可

  ```javascript
  sayHello();
  ```

------------------------

### 函数的参数

* 参数被写在函数声明时的小括号内 , 但是参数并不是必须的 , 使用参数的话 , 参数个数是不限的

  ```javascript
  // 无参函数
  function cook(){
      console.log('Ice cream~');
  }
  ```

* 利用参数可以实现函数运行不同的代码

* <font color="#adf135">需要注意的是 , 形参并不需要使用 <kbd>var</kbd> 或 <kbd>let</kbd> 声明 , 直接写个名字即可实现声明</font> 

  ```javascript
  // 含参函数
  function cook(name){
      console.log(name);
  }
  ```

* **参数作用是 : 在函数内部某些值无法固定时 , 通过调用函数时传递不同参数传值 , 从而实现代码的正常运行**

#### 形参和实参

> 实际在使用函数的时候 , 由于有声明和调用函数 , 从而使得参数也有了不同的性质 , 即形参和实参

| **参数** |                           **说明**                           |
| :------: | :----------------------------------------------------------: |
| **形参** | 形式上的参数 **函数定义**的时候传递的参数 声明时并不知道是什么 |
| **实参** | 实际上的参数 **函数调用**时传递的参数 实参是传递给形参实现函数运行的 |

* 我们知道含参函数的语法格式如下 , 这样就可以很容易地理解形参和实参的区别了

  ```javascript
  // 声明函数时小括号里的是形式参数
  // formal parameter 形参--形式参数 formal-正式的 parameter-参数
  // argument-参数(即实参--实际参数)
  function funName(forPara1,forPara2){
      // 函数体
  }
  // 调用函数时小括号里面的是实际参数
  funName(argument1,argument2);
  ```

* 形参和实参的关系可以看成 , 形参是声明变量 , 而实参则是给变量赋值

* 注意 , 形参和实参的数量在 Java 中必须一一对应 , 一旦不一致就会报错

* 但是 , 在 JavaScript 中 , 是没有这种规定的 , 我们建议延续 Java 的习惯 , 形参和实参个数相匹配

#### △ 形参实参匹配问题

* 对于下面这一段代码

  ```javascript
  function getSum(num1 , num2){
      console.log(num1 + num2);
  }
  getSum(1, 2); // 正常输出
  getSum(1, 2, 3); // 多实参,取形参个数
  // 任何一个数值型的变量 +undefined 结果为NaN
  getSum(1); // 少实参,结果为 NaN
  ```

  |    **参数个数**     |                 **说明**                  |
  | :-----------------: | :---------------------------------------: |
  | 实参个数 = 形参个数 |               输出正常结果                |
  | 实参个数 > 形参个数 |             只取到形参的个数              |
  | 实参个数 < 形参个数 | 多的形参定义为 undefined , 返回结果为 NaN |

#### 小结

* 函数既可以带参数也可以不带参数
* 声明函数的时候 , 函数名括号里面的是形参 , 形参的默认值为 undefined
* 调用函数的时候 , 函数名括号里面的是实参
* 多个参数之间用逗号分隔
* 形参的个数和实参的个数可以不匹配 , 但是尽量保证一一对应

--------------------

#### 案例A-求平均数

* 根据给定的两个数 , 求这两个数之间所有整数的平均数

  ```javascript
  function calcuAve(start , end){
      let aveNum = 0;
      for(let i = start; i <= end; i++){
          aveNum += i;
      }
      aveNum = aveNum / (end - start + 1);
      console.log(aveNum);
  }
  calcuAve(2,6); // 4
  ```


---------------

### 函数的返回值

* 我们使用函数的时候 , 往往是为了完成一系列有区别 , 但不完全相同的重复工作 , 这时候 , 在函数中写一些死语句就很不靠谱了 , 我们需要让函数能够处理我们给定的变量 , 并将处理的结果给我们 , 此时 , 我们就需要函数的返回值了
* 在实际中 , 我们希望函数将值返回给调用者 , 此时 , 就需要使用 return 语句来返回了

#### return 语句

* 函数返回内容的格式

  ```javascript
  // 函数只是实现某种功能,最终的结果通过return语句返回给调用者
  function functionName(){
      // 函数处理完毕,返回需要返回的结果
      return resultNeeded;
  }
  // 变量调用函数,并保存返回值
  let result1 = functionName();
  ```

* 以下是一个简单的返回值的例子

  ```javascript
  function getSomething(a,b){
      return a + b;
      // return终止函数
      alert('这句话永远都不会被执行');
  }
  let getSome = getSomething(1,2);
  console.log(getSome); // 3
  ```

#### ★ return 语句特点

* **[ return 终止函数 ]** 在上面的例子中 , return 语句之后有一句 alert 语句 , 这句话永远都不会被执行 , 这是因为执行完 return 语句之后 , 函数就算是执行完毕了 , 因此 return 语句之后的内容都不会被执行
* <font color="#fa9406">**return 只能返回一个值**</font> , 如果用逗号隔开多个值 , 以最后一个值为准进行返回 
* **如果想返回多个值的话 , 就需要使用数据结构了 , 你可以使用数组 , 使用 map 或者使用对象等结构返回内容** 
* 如果一个函数没有 return 语句 , 那么它也有返回值 , 其返回值为 undefined 

#### break continue return 的区别

* break : 结束当前的循环体 ( 如 for , while )
* continue : 跳出本次循环 , 继续执行下次循环 ( 如 for , while )
* return : 不仅可以退出循环 , 还能够返回 return 语句中的值 , 同时还可以结束当前的函数体内的代码

---------------

#### 案例B-求最大值

* 函数操作给定的两个实参 , 据此计算出两个数的最大值并返回 ( 复习三元表达式 )

  ```javascript
  // a>b吗?若大于则返回a,否则返回b
  function getMaxNum(a,b){
      if(a > b){
          return a;
      }else{
          return b;
      }
  }
  // 其实可以使用三元运算符,一行代码就能解决问题
  function getMaxNumFixed(a , b){
      // a>b吗?若大于则返回a,否则返回b
      return a > b ? a : b;
  }
  ```

* 更进一步 , 若要在一个数组中求最大值的话 , 我们不仅需要函数 , 还需要循环

  ```javascript
  let myArr = [5,2,99,101,67,77,98,55,123];
  function getMaxNum(arr){
      let maxNum = arr[0];
      // 从第0个数存起,则从第一个数比起
      for(let i = 1; i < arr.length; i++){
          if(arr[i] > maxNum){
              maxNum = arr[i];
          }
      }
      return maxNum;
  }
  // 实际中我们经常使用一个变量来接受函数的返回结果
  let result = getMaxNum(myArr);
  console.log(result);
  ```

-----------------

#### 案例C-素数判断

* 用户输入一个数 , 判断这个数是否为素数 ( 即质数 , 只能被 1 和自身整除的数 ) , 并返回结果

  ```javascript
  let num = 9;
  // prime number 素数,质数
  function isPrime(a) {
    if (a <= 1) {
      return a + ' is not a normal number !';
    } else {
      for (let i = 2; i < a; i++) {
        if (a % i != 0) {
          continue;
        } else {
          // the divisor 约数
          console.log('The divisor of ' + a + ' is : ' + i);
          return a + ' is not a prime number !';
        }
      }
      return a + ' is a prime number !';
    }
  }
  // The divisor of 9 is : 3
  // 9 is not a prime number !
  console.log(isPrime(num));
  ```

* **[ 延伸 ]** : 求两个数的最大公约数

* 任意给定两个数 , 判断这两个数的最大公约数

* 思路很简单 , 利用更相减损法 , 即首先判断两个数是否为偶数 , 若是则用 2 先约简一次 , 若是奇数则跳过此步

* 之后用较大的数减较小的数 , 接着把所得的差与较小的数比较 , 并以大数减小数 , 持续此操作 , 直到减数和差相等为止

  ```javascript
  // 首先判断是否为奇数或偶数,先写一个对任意数判断的情况
  function isOdd(a) {
    if (a < 1) {
      // 如果输入了错误的数则抛出异常
      throw SyntaxError();
    } else {
      if (a % 2 == 1) {
        return true;
      } else {
        return false;
      }
    }
  }
  // 接下来利用这个函数进行计算最大公约数
  function maxDivisor(a, b) {
    // 判断a的奇偶性
    if (isOdd(a) == true) {
      // 是奇数,不做任何事
    } else {
      a = a / 2;
    }
    // 判断b的奇偶性
    if (isOdd(b) == true) {
      // 是奇数,不做任何事
    } else {
      b = b / 2;
    }
    // 计算最大公约数
    while (a != b) {
      // 总归要执行减法,所以判断谁大就可以了,以免减出负数
      if (a < b) {
        b = b - a;
      } else {
        a = a - b;
      }
    }
    // 最后二者相等,输出哪个都一样
    return a;
  }
  console.log(maxDivisor(319, 377)); // 29
  ```


---------------

### △Arguments 的使用

* 当我们不确定有多少个参数传递的时候 , 可以使用 <font color="#d0bfea">arguments</font> 来获取 , 在 JS 中 , arguments 实际上是当前函数的一个<font color="#d0bfea">内置对象</font> 

* 需要注意的是 , **有且仅有所有函数内置了** arguments 对象 , 并且 <font color="#d0bfea">arguments 对象中</font><font color="#86eb40">**存储了传递过来的所有实参**</font> 

  ```javascript
  function newFn(){
      // Arguments(3) [1,2,5,...]
      console.log(arguments);
      // 3
      console.log(arguments.length);
      // 5
      console.log(arguments[2]);
  }
  fn(1,2,5);
  ```

* Arguments 展示的形式是一个 <font color="#e1d78d">伪数组</font> , 因此可以对其进行遍历

* 但是要明确的是 <font color="#e604b2">**伪数组 并不是真正意义上的数组**</font> 

* **伪数组** 具有以下的特点 :

  * 具有 length 属性 , 因此可以按照数组的方式进行遍历 arguments 的内容
  * 按索引方式进行存储
  * 不具有数组的 push() , pop() 等方法

* ★ 由此可见 , <font color="#91d108">有了 arguments 之后我们不再需要给函数写形参了</font> 

#### 案例D-利用函数求两个数的最小公倍数

* 之前案例中刚刚好计算了最大公约数 , 利用它就能很方便地进行最小公倍数的计算了

* 原则 : <font color="#34dc99">**两个数的乘积等于二者的最大公约数和最小公倍数的乘积**</font> 

  ```javascript
  // 为了避免出问题,把之前写的求最大公约数的代码贴下来
  // ************* PreCode Start *************
  // 首先判断是否为奇数或偶数,先写一个对任意数判断的情况
  function isOdd(a) {
    if (a < 1) {
      // 如果输入了错误的数则抛出异常
      throw SyntaxError();
    } else {
      if (a % 2 == 1) {
        return true;
      } else {
        return false;
      }
    }
  }
  // 接下来利用这个函数进行计算最大公约数
  function maxDivisor(a, b) {
    // 判断a的奇偶性
    if (isOdd(a) == true) {
      // 是奇数,不做任何事
    } else {
      a = a / 2;
    }
    // 判断b的奇偶性
    if (isOdd(b) == true) {
      // 是奇数,不做任何事
    } else {
      b = b / 2;
    }
    // 计算最大公约数
    while (a != b) {
      // 总归要执行减法,所以判断谁大就可以了,以免减出负数
      if (a < b) {
        b = b - a;
      } else {
        a = a - b;
      }
    }
    // 最后二者相等,输出哪个都一样
    return a;
  }
  // ************* PreCode End *************
  // 利用结果求出两个数的最小公倍数
  function minCommonMultiple(a, b){
      // 先求两个数的乘积,再用乘积除以最大公约数
      return (a * b) / maxDivisor(a, b);
  }
  console.log(minCommonMultiple(9, 12)); // 36
  ```

#### 案例E-翻转数组

* 使用函数将一个数组翻转过来 , 并且不使用栈这个数据结构 , 仅仅是将一个数组按序颠倒

* 和之前存给新数组不一样 , 我们这次直接在形参中通过一个临时变量来进行一个数组本身的内容替换

  ```javascript
  let arr1 = [1, 2, 3, 4, 5];
  let arr2 = [1, 2, 3, 4, 5, 6];
  // 翻转倒置的单词有invert和reverse,由此还能引申到revert
  // invert 侧重指(在数或量上呈)反向变化的,上下颠倒的,倒置的
  // reverse 侧重于顺序,方向上的相反,即逆向的,逆序的,背面的
  // revert 则是回复,恢复原状的意思,和翻转无关,有点类似重复一次的意思
  function reverseArr(arr) {
    // 临时变量用于交换数字防止当前元素数据丢失
    let temp = 0;
    // 通过仅迭代数组的一半,来实现数组自身的翻转
    for (let i = 0; i < (arr.length / 2); i++) {
      temp = arr[i];
      arr[i] = arr[arr.length - 1 - i];
      arr[arr.length - 1 - i] = temp;
    }
    return arr;
    }
  console.log(reverseArr(arr1));
  console.log(reverseArr(arr2));
  ```

#### 案例F-封装冒泡排序

* 冒泡排序的原理不需要再进行解释了 , 我们现在就是把这个逻辑给封装起来 , 传入数组实现排序 , 返回排好的数组

  ```javascript
  function bubbleSort(arr){
      // 还是一样,使用两层循环完成,首先定义出来用于交换元素的临时变量
      let temp = 0;
      // 第一层循环控制交换轮数,轮数比元素个数小1
      for(let i = 0; i < arr.length - 1; i++){
          // 第二层循环控制每次的交换次数,交换的是哪个元素,刚刚好利用序号,也就是i
          for(let j = 0; j < arr.length - i - 1 ; j++){
              // 如果前一个数大于后一个数,就交换这两个数
              if(arr[j] > arr[j + 1]){
                  temp = arr[j];
                  arr[j] = arr[j + 1];
                  arr[j + 1] = temp;
              }
          }
      }
      // 最终返回排好序的数组
      return arr;
  }
  let arr = [7,6,9,8,4,5,1,2,3];
  console.log(bubbleSort(arr));
  ```

--------------------------

### △ 函数调用

* 由于每个函数都是相对独立的代码块 , 并且都用于完成一些重复且特定的任务 , 因此我们经常使用到函数相互调用的情况 , 之前的计算最大公约数和计算最小公倍数的例子里就是这样做的
* 当函数调用自身的时候 , 就会形成递归函数 , 递归函数也算是一种特殊的循环方式

-------------

### ★ 函数的两种声明方式

* **利用函数关键字自定义函数** ( 命名函数 )

  ```javascript
  // 我们一直在使用的函数声明方式就是这种
  function funName(){
      // Program block
  }
  // Calling
  funName();
  ```

* **使用函数表达式进行声明使用** ( 匿名函数 ) -- **函数指针** 

  ```javascript
  var varName = function(){
      // Program block
  };
  // Calling
  varName(); // varName是变量名,不是函数名
  ```

  * 通过函数表达式声明函数 , 类似于变量命名一样
  * 不过变量里面存的是值 , 而函数表达式里面存的是函数
  * 调用的时候也很特别 , 这种函数并没有函数名 , 调用时是通过变量名调用函数使用的
  * 需要注意的是 , 匿名函数是没有办法写递归的 , 可以把这种声明形式看做 **函数指针** 

[PS] **函数指针** 

* 在 C 语言中 , 有一种概念叫做函数指针 , 什么叫函数指针呢 ? 

* 我们知道 , 如果在程序中定义了一个函数 , 那么在编译时系统就会给这段函数代码分配一段存储空间

* <font color="#faa63d">这段存储空间的首地址就称做这个函数的地址</font> , 函数名就表示这个地址

* 由于是地址 , 所以我们可以定义一个指针变量存放它 , 这个指针变量就叫做**函数指针变量** , 即**函数指针** 

* 其定义方式为 : 

  ```c
  // 函数返回值类型 (* 指针变量名) (函数参数列表);
  returnType (* pointVar)(para1,para2,...);
  // 例如
  int(*p)(int, int);
  // 这个语句的意思是：
  // 定义一个指针变量 p,该指针变量可以指向返回值类型为 int 型,且有两个整型参数的函数
  // p 的类型为 int(*)(int,int)
  ```

* 值得注意的是 , (* 指针变量名) 这一部分的括号是不能省略的

* 使用函数指针调用函数的例子如下 :

  ```c
  /* 声明一个函数 */
  int Func(int x);
  /* 定义一个函数指针 */
  int(*p)(int x);
  /* 将Func函数的首地址赋给指针变量p */
  p = Func;
  ```

* 由于函数名 `Func` 代表函数的首地址 , 所以给指针 p 赋值时函数 `Func` 不带括号 , 也不带参数

* 为了深入理解 , 我们可以看下面这个例子

  ```c
  # include <stdio.h>
  // 声明函数
  int Max(int, int);
  // 主程序
  int main(void)
  {
      // 定义一个函数指针
      int(*p)(int, int);
      int a, b, c;
      // 把函数 Max 首地址赋给指针变量 p,使 p 指向 Max 函数
      p = Max;
      printf("please enter a and b:");
      // 扫描输入 %d 代表需要获取的内容,一个 %d 就是一个参数
      scanf("%d%d", &a, &b);
      // 通过函数指针调用 Max 函数
      c = (*p)(a, b);
      // 打印结果
      printf("a = %d\nb = %d\nmax = %d\n", a, b, c);
      return 0;
  }
  // 定义 Max 函数,用于寻找最大值
  int Max(int x, int y)
  {
      int z;
      if (x > y)
      {
          z = x;
      }
      else
      {
          z = y;
      }
      return z;
  }
  ```


# JavaScript 对象

--------------------

## 对象

* JS中 , 对象就是一组无序<font color="#705438">(没有索引)</font>的相关属性和方法的集合 , 所有的事物都可以是对象 , 例如字符串 , 数值 , 函数

* 对象是由 <font color="#ce3b3b">属性</font> 和 <font color="#ce3b3b">方法</font> 组成的 , 一种代表事物普适性的抽象集

  * 属性 : 事物的<font color="#ce3b3b">特征</font> , 在对象中用<font color="#ce3b3b">属性</font>来表示 ( 属性多用名词表示 )
  * 方法 : 事物的<font color="#ce3b3b">行为</font> , 在对象中用<font color="#ce3b3b">方法</font>来表示 ( 方法多用动词表示 )

  > 为什么需要对象 : 
  >
  > 如果我们只想保存一个值时 , 我们可以使用<font color="#ce3b3b">变量</font> , 保存多个值 ( 一组值 ) 的时候 , 我们可以使用 <font color="#ce3b3b">数组</font>
  >
  > 但是当我们要保存一个对象的信息的时候 , 仅仅使用这些就不能满足需求了
  >
  > 如果使用变量 , 我们需要创建若干个变量 , 如果使用数组 , 我们就像在使用一条没有表头的表格
  >
  > 因此 , 我们就需要对象来保存

* 使用对象我们可以将对象的结构表达更清晰 , 比如一个人的个人信息他的对象结构可以这样去表示

  ```javascript
  person.name = 'Cyber';
  person.sex = 'male';
  person.age = 26;
  person.height = 174;
  ```

### 创建对象的三种方式

* 在 JavaScript 中 , 现阶段我们可以用三种方式去创建对象 ( Object ) : 
* 1. 利用 <font color="#15ee6d">**字面量**</font> 创建对象
  2. 利用 <font color="#15ee6d">**new Object**</font> 创建对象
  3. 利用 <font color="#15ee6d">**构造函数**</font> 创建对象

-------------------

#### 利用字面量创建对象

* <font color="#15ee6d">对象字面量</font> : 就是花括号 { } 里面包含了表达这个具体事务( 对象 ) 的属性和方法 .

  ```javascript
  var obj = {}; // Empty object
  
  // 一个具体的对象
  var obj1 = {
      uname: 'Cyber',
      age: 18,
      sex: 'male',
      sayHi: function(){
          console.log('Hello~');
      }
  }
  ```

* A. 对象中的属性或者方法我们采取 <font color="#f8332f">**键值对**</font> 的形式表示 , 即类似于 <kbd>(键)→属性名: 值←(属性值)</kbd> 

* B. 多个属性或者方法之间是使用 <font color="#f8332f">**逗号**</font> 隔开的 , 最后一个属性或者方法之后不需要逗号

* C. 方法冒号后面跟的是一个匿名函数

* 当对象创建完毕之后 , 我们需要使用它 , 使用的方式为通过 <kbd>.</kbd> 的方式去使用 , 把 <kbd>.</kbd> 当做 "的" 来看待即可

* A. 调用对象的属性 , 我们采取 `objectName.attributeName` 的方式调用

  ```javascript
  var obj = {
      uname: 'Cyber',
      age: 18,
      sex: 'male',
      sayHi: function(){
          console.log('Hello~');
      }
  }
  console.log(obj.uname);
  ```

* B. 调用对象的属性 , 还有另外一种方法 , 即采取 `objectName['attributeName']` 的方式调用

  ```javascript
  console.log(obj['age']);
  ```

* C. 调用对象的方法 , 依然可以使用 `objectName.functionName()` 的形式调用

  > 一定不能忘记方法就是函数 , 是需要有小括号的

  ```javascript
  var obj = {
      uname: 'Cyber',
      age: 18,
      sex: 'male',
      sayHi: function(){
          console.log('Hello~');
      }
  }
  obj.sayHi();
  ```

------------------------

##### 变量方法等对比

* **变量 , 属性 , 函数 , 方法的区别**

* 变量和属性相同的地方是 , 他们都是用来存储数据的

  ```javascript
  // variable
  var num = 10;
  // object
  var obj = {
      age: 18
  }
  console.log(obj.age);
  console.log(num);
  ```

  > 变量单独声明并赋值 , 使用的时候需要直接写变量名 , 每个变量是 **单独存在** 的
  >
  > 属性是在对象里面的 , 并不需要像变量一样声明 , 但是使用的时候必须用 <kbd>obj.att</kbd> 的方式调用

* 函数和方法相同的地方是 , 他们都是用来实现某种功能 , 做某种事情的

  ```javascript
  // function
  function fn(){
      console.log('function');
  }
  // object
  var obj = {
      age: 18,
      catch: function(){
          console.log('catch!');
      }
  }
  ```

  > 函数是 单独声明 并且单独调用的 , 通过 <kbd>functionName()</kbd> 的方式 **单独存在** 和调用
  >
  > 方法存在于对象里面 , 调用的时候必须用 <kbd>obj.fun()</kbd> 的方式调用

--------------------------

#### 利用new Obj创建对象

* 我们可以使用 <kbd>new Object()</kbd> 的形式创建对象

  > 这种方法和我们之前创建数组的原理一致 , 即类似于 `new Array()` 的形式

* 具体我们可以这样去编写代码

  ```javascript
  var obj = new Object(); // 创建一个空对象
  obj.uname = '张三'; // 通过追加属性的方式去添加内容
  obj.age = 18;
  obj.sex = '男';
  obj.sayHello = function(){
      console.log('Hello');
  }
  // 调用对象属性或方法是一样的
  console.log(obj.uname);
  console.log(obj['age']); // 注意这种形式的调用
  obj.sayHello(); // 注意对象方法的调用也是在调用函数
  ```

  > 上面的例子中我们使用了追加属性的方法去添加了对象的属性和方法
  >
  > 利用 等号 = 赋值 的方式添加追加内容
  >
  > 每个属性的方法之间会用分号结束 , 而不是像创建对象的时候那样去用逗号隔开

---------------------

### ★构造函数

* 在之前 , 我们可以使用下面这两种方法去创建对象

  ```javascript
  // 利用字面量创建对象
  var naruto = {
      name: 'naruto',
      age: 22,
      sayYoo: function(){
          console.log('Hello there~');
      }
  }
  // 利用 new Object() 的形式创建对象
  var car = new Object();
  car.name = 'Das Auto';
  car.size = 'Small';
  car.sayYoo = function(){
      console.log('Yoo there~');
  }
  ```

* 这两种创建对象的方法 , 每次只能创建一个对象

* 如果我们想要创建多个属性有共同点的对象的话 , 就可以利用构造函数

* 我们将重复的对象代码写在函数里面 , 这样函数内容不是普通的逻辑代码 , 而是对象 , 因此称为构造函数

* <font color="#f8332f">**构造函数 : **</font>是一种特殊的函数 , 主要用来初始化对象 , 即为对象成员变量附初始值 , 它总与 new 运算符一起使用 , 我们可以把对象中一些公共的属性和方法抽取出来 , 然后封装到这个函数里面 . 

* 我们一般使用下面的格式来声明构造函数

  ```javascript
  function constructFunction(){
      // 当前的对象用this来代替
      this.attName = value;
      this.functionName = function(){}
  }
  // 在调用的时候,需要用下面的格式
  new constructFunction();
  ```

* ★我们一般用**首字母大写**来规范构造函数的命名

  ```javascript
  // 构造函数既然有属性,就需要传参
  function Star(sname, size, age){
      this.name = sname;
      this.size = size;
      this.age = age;
      // 不需要return
      this.sing = function(sang){
          console.log(sang + '♪~~~~');
      }
  }
  // 在使用的时候要传参完成变量的赋值操作
  var mars = new Star('Mars', 'Little', 7000);
  console.log(typeof mars); // Obj
  console.log(mars['name']);
  console.log(mars.size);
  mars.sing('冰雨'); // ★调用对象内部函数
  // 这样,只要我们new一下就会有新对象了
  var sun = new Star('Sun', 'Bigggg', 90000);
  console.log(sun.name);
  ```
  
  > <font color="#8ee8e4">构造函数不需要 return 就可以返回结果</font> 
  >
  > 调用构造函数 , 必须使用 new , 在上面的例子中 , 我们只需要 new Star() 调用构造函数就会创建新对象
  
* 比如我们有这样的需求 , 我们现在有两个英雄 , 每个英雄有一些公共部分的内容
  
* 姓名 name , 类型 type , 血量 health , 攻击方式 attack
  
* 根据这种公共属性 , 我们可以创建出如下的对象构造函数
  
  ```javascript
  function Heros(name, type, health, attack){
      this.name = name;
      if(type == 1){
          this.type = 'Power Hero';
      }else{
          this.type = 'Shooter Hero';
      }
      this.health = health;
      this.attack = attack;
  }
  var hy = new Heros('后羿', 2, 500, '射手');
  var zz = new Heros('庄周', 1, 900, '战士');
  console.log(hy.name);
  console.log(zz.type);
  ```
  
* 不难发现 , 构造函数泛指某一大类的东西 , 相当于 Java 中的 类(class)

* 而对象就是特指的具体事物 , 是个<font color="#92b95a">实例</font> 

* 我们<font color="#18eec1">利用构造函数创建对象的过程 , 就是对象的实例化</font> 

----------------------

### ★ new关键字

* 当我们在一个使用构造函数时 new 了一个新对象时 , 开始会在内存中先创建一个空对象

* 此时 this 就会指向刚刚创建的空对象 , 此时执行构造函数内的代码 , 从而填充对象

* 最后将有完整属性和内容的对象返回出来 , 并赋值给用来接收 new 的新对象的变量

  > 也就是说 , new 在执行的时候会做这些事情 : 
  >
  > 1. 在内存中创建一个新的空对象
  > 2. 让 this 指向新对象
  > 3. 执行构造函数内部代码 , 给新对象添加属性和方法
  > 4. 返回新对象 ( 这也是为什么构造函数里面不需要 return 的原因 )

------------------

### 遍历对象

* 之前我们在调用对象内属性或者方法的时候 , 是用的单行输出的形式

* 为了重复这个操作 , 我们要遍历对象 , 但对象内容是无序的 , 很显然不能用 for 循环

* 由此 , 我们引出了 <font color="#e60039">**for...in 语句**</font> , 它用于对数组或者对象的属性进行循环操作

  > 我们推荐用 for...in 语句遍历对象 , 而不是在遍历数组等结构的时候使用它

* <font color="#e60039">**for...in**</font> 的遍历格式如下

  ```javascript
  for ( variableState in objectName){
  	// other codes
  }
  ```

* 假如我们有这样一个对象

  ```javascript
  var obj = {
      name: 'CyberYui',
      age: 25,
      sex: 'male',
      type: 'Smart',
      sayHi: function(){
          console.log('Here is a function in the obj');
      }
  }
  ```

* 我们可以这样去遍历它 , 这种方式不仅可以遍历属性 , 也可以遍历方法

  > 值的注意的是 , 遍历方法不会调用方法 , 而是输出方法代码

  ```javascript
  // 不需要给k赋值
  for(var k in obj){
      // 直接输出变量,会循环输出属性名
      console.log(k);
      // 利用中括号这种形式,可以输出相应的属性值,以及方法的代码内容
      console.log(obj[k]);
  }
  // 对于 console.log(obj[k]) ,
  // 区别下直接从对象中调用变量的中括号
  console.log(obj['sex']);
  ```

  > for...in 里面的临时变量 , 一般我们习惯命名为 <font color="#e60039">**k**</font> 或者 <font color="#e60039">**key**</font> 

--------------

### 对象小结

* 对象可以使代码结构更加严谨 , 清晰
* 对象复杂数据类型是 Object 
* 本质上 , 对象就是一组无序的相关属性和方法的集合
* 构造函数实际上就是一个抽象出来的共性内容 , 比如苹果 , 不论红苹果还是绿苹果 , 都是苹果
* 对象实例特指一个事物 , 比如你正在吃的苹果 , 它是实际存在的 , 可以被调取的
* 使用 for...in 可以遍历对象的内容

-------------

### 案例A

* 写一个函数 , 实现反转任意数组

  ```javascript
  function invertArray(arr){
      // Show the source array
      for(let i = 0; i < arr.length; i++){
          console.log(arr[i] + ' ');
      }
      // Invert array and show it
      for(let i = arr.length - 1; i >= 0; i--){
          console.log(arr[i] + ' ');
      }
  }
  ```

-----------

### 案例B

* 写一个函数 , 实现对数字数组的排序 ( 不要使用冒泡排序了 )

  ```javascript
  function fastsort(arr){
    // 递归停止条件
    if (arr.length <= 1){
      // 当数组长度不足时直接输出数组,即单数自行排序
      return arr;
    }
    // 确定数据开始中心,即第一项元素
    let pivot = arr[0];
    // 定义左右数组,便于进行递归操作
    let left = [];
    let right = [];
    // 开始排序,当当前元素小于中心值时,放入左数组,否则放入右数组
    for (let i = 1; i < arr.length; i++){
      if (arr[i] < pivot){
        left.push(arr[i]);
      } else {
        right.push(arr[i]);
      }
    }
    // 一次比较之后,会确定最中间的元素,左边是比它小的,右边是比它大的
    // 接下来利用concat方法连接左数组,中间数和右数组三项
    // 但是由于左右数组在一次比较之后没有单独排序,所以要实行递归操作
    // 这样,在fastsort(left)和fastsort(right)中会对左右数组进行类似操作
    // 直到数组为一项,则会进入递归的停止条件,返回数组(即单数数组)
    return fastsort(left).concat(pivot, fastsort(right));
  }
  ```

----------

### 案例C

* 写一个简易的计算器 , 根据用户输入的数字进入不同的运算或者退出 , 主要针对两个数进行操作

* 1. 加法运算
  2. 减法运算
  3. 乘法运算
  4. 除法运算
  5. 退出

* 用户通过输入数字从而进行操作

  ```javascript
  // 首先要求用户选择自己需要的操作,这项其实可以直接写到函数里面
  var mod = prompt(
      "Please choose the calculate mod you want :\n1. plus\n2. minus\n3. multiply\n4. divide\n5. quit"
    );
  // 根据选项进行函数操作
  function calculator(mod) {
    var num1 = prompt("Please input the first number");
    var num2 = prompt("Please input the second number");
    // 使用多重循环进行计算,这里可能会有计算错误,还需要修改
    if (mod == 1) {
      alert(num1 + num2);
    } else if (mod == 2) {
      alert(num1 - num2);
    } else if (mod == 3) {
      alert(num1 * num2);
    } else if (mod == 4) {
      alert(num1 / num2);
    } else if (mod == 5) {
      alert("Bye");
    } else {
      alert("Please input the correct number");
    }
  }
  // 调用函数,使用刚刚用户输入的数字进行计算
  calculator(mod);
  ```

------------

## JavaScript 内置对象

- JavaScript 中的对象分为3种 : 自定义对象 , 内置对象 , 浏览器对象

- 自定义对象 和 内置对象 是 JS 的基础内容 , 属于 ECMAScript

- 浏览器对象 是 JS 独有的 , 会在之后的 JS API 中讲解

- **内置对象** 就是指 JS 语言自带的一些对象 , 这些对象供开发者使用 , 并提供了一些常用的基本功能的对象

  > 使用内置对象可以方便程序员快速开发

- JavaScript 提供了多个内置对象 , 如 Math , Date , Array , String 等

-----------

### 查文档

> MDN ( Mozilla Developer Network ) , 即 Mozilla 开发者网络 , 这里提供了有关开放网络技术的信息 , 包括但不限于 HTML , CSS 以及 HTML5 应用的 API https://developer.mozilla.org/zh-CN/

- **如何学习对象中的方法** 
  1. 查阅该方法的功能
  2. 查看里面 **参数** 的意义和类型 ( 当参数由中括号包裹 , 代表参数并不是必须的 )
  3. 查看 **返回值** 的意义和类型
  4. 通过 demo 进行测试

### Math对象

- Math 不是一个构造函数 , 因此我们不需要用 new 关键字来调用它 , 而是可以直接使用其里面的属性和方法

  > 具体的相关方法可以直接查询网络文档 , 如果想要知道原理则需要去查看方法的代码

  ```javascript
  console.log(Math.PI); // 输出圆周率
  console.log(Math.max(1,99,33)); // 输出传入参数组的最大值
  ```

  > 每种方法的输出结果以及边界值都有在文档中给出

- 跟数学相关的运算 ( 如求绝对值 , 取整 , 最大值等 ) 均可以使用 Math 中的成员

  ```javascript
  Math.PI // 圆周率
  Math.floor() // 下取整
  Math.ceil() // 上取整
  Math.round() // 四舍五入就近取整 注意-3.5的结果是-3,这个取值默认按坐标轴取近的,但唯独.5例外,它是取轴值大的
  Math.abs() // 绝对值 (absolute value)
  Math.max() // 求最大值
  Math.min() // 求最小值
  // 尝试一下这些方法
  console.log(Math.abs('-1')); // 隐式转换,会把字符串型-1转换为数字型然后进行计算
  console.log(Math.round(-4.6)); // -5,按坐标轴取近的
  ```

- Math 对象中常用的是取随机数的方法 , 即 `random()` 方法

--------------

### 案例A

- 封装一个你自己的数学对象 , 里面需要有 PI , 最大值和最小值方法

  ```javascript
  var myMath = {
    PI: 3.14159265354,
    max: function () {
      // 使用arguments来获取不存在的实参
      var max = arguments[0];
      for (var i = 1; i < arguments.length; i++) {
        if (arguments[i] > max) {
          max = arguments[i];
        }
      }
      return max;
    },
    min: function () {
      // 使用arguments来获取不存在的实参
      var min = arguments[0];
      for (var i = 1; i < arguments.length; i++) {
        if (arguments[i] < min) {
          min = arguments[i];
        }
      }
      return min;
    }
  };
  // 使用自己的对象方法
  console.log(myMath.PI);
  console.log(myMath.min(99,15,1,2));
  ```

  
