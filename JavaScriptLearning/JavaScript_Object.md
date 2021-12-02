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
  ```

------------

## JavaScript 内置对象

