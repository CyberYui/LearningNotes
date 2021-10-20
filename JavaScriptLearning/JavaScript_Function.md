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
  // prime number 素数,质数
  function isPrime(a){
      
  }
  ```

  

