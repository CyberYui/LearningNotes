# JavaScript 关键字和保留字

## ---------------------------------------摘录自《JavaScript高级程序设计(第三版)》

### 关键字

> ECMA-262 描述了一组具有特定用途的**关键字**,这些关键字可用于表示控制语句的开始或结束,或者用于执行特定操作等.按照规则,关键字也是语言保留的,不能用作标识符.以下为 ECMAScript 的全部关键字(带*号上标的是第5版新增的关键字):

| Keywords 关键字 |          |            |        |
| :-------------: | :------: | :--------: | :----: |
|      break      |    do    | instanceof | typeof |
|      case       |   else   |    new     |  var   |
|      catch      | finally  |   return   |  void  |
|    continue     |   for    |   switch   | while  |
|    debugger*    | function |    this    |  with  |
|     default     |    if    |   throw    |        |
|     delete      |    in    |    try     |        |

### 保留字

> ECMA-262 还描述了另外一组不能用作标识符的**保留字**.尽管保留字在这门语言中还没有任何特定的用途,但它们有可能在将来被用作关键字.以下是 ECMA-262 定义的全部保留字:

| Reserved words 保留字 |            |           |              |
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

[注意]

​		let 和 yield 是 ECMAScript 5 新增的保留字: 其他保留字都是 ECMAScript 3 定义的. 在实现 ECMAScript 3 的 JS 引擎中使用关键字作为标识符, 会导致 "Identifier Expected" 错误. 而使用宝录制作为标识符可能会也可能不会导致相同的错误, 具体取决于特定的引擎.

​		在上述中, eval 和 arguments 虽然并不是作为关键字或者保留字留存的, 但是在严格模式下, 这两个名字也不能作为标识符或属性名, 否则会抛出错误.

