# JavaScript 进阶知识

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

* ![单一if分支语句流程](JS_advanced_pic2.png) ![if 双分支语句流程](JS_advanced_pic3.png) 

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
* ![](JS_advanced_pic4.png) 

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
  for (let i = 1; i <= 3; i++){
      console.log('这是外层的第' + i + '次循环');
      for (let j = 1; j <= 4; j++){
          console.log('这是内层的第' + j + '次循环');
      }
  }
  ```

  

##### ★案例 D : 用循环的方式打印星星 ( 双重 for 循环 )

```javascript
```



---------------------------













--------------------------------------

## [断点调试]

* 断点调试是指自己在程序的某一行设置一个断点 , 调试时 , 程序运行到这一行就会停住 , 然后你可以一步一步往下调试 , 调试过程中可以看各个变量当前的值 , 出错的话 , 调试到出错的代码行即显示错误 , 停下.
* <font color=#f80c73>**断点调试可以帮助我们观察程序的运行过程**</font> 
* 浏览器中按 <kbd>F12 → sources → 找到需要调试的文件 → 在程序的某一行设置断点</kbd> 
* Watch : 监视 , 通过 watch 可以监视变量的值的变化 , 非常的常用
* F11 : 程序单步执行 , 让程序一行一行地执行 , 这个时候 , 观察 watch 中变量的值的变化
* 代码调试的能力非常重要 , 只有学会了代码调试 , 才能学会自己解决 bug 的能力
