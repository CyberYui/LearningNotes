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

#### ★利用构造函数

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
  }
  // 在使用的时候要传参完成变量的赋值操作
  var mars = new Star('Mars', 'Little', 7000);
  console.log(typeof mars); // Obj
  console.log(mars['name']);
  console.log(mars.size);
  // 这样,只要我们new一下就会有新对象了
  var sun = new Star('Sun', 'Bigggg', 90000);
  console.log(sun.name);
  ```
  
  > <font color="#8ee8e4">构造函数不需要 return 就可以返回结果</font> 