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

