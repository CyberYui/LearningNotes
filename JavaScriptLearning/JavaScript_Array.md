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
