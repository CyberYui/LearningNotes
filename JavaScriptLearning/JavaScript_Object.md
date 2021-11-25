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

#### 变量方法等对比

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