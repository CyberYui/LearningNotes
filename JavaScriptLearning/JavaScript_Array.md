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

  
