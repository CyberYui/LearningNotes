## Hash 类型

-----------

### 存储的困惑

> 在 String 类型中 , 我们可以使用以下方式存储数据
>
> ```json
> h_user user:id:3506728370{
> 	name:春晚,
> 	fans:1222515345,
> 	blogs:5684,
> 	focus:83
> }
> ```
>
> 这种方式存储的数据 , 当遇到我们需要频繁更新的时候 , 会显得笨重
>
> 当然我们有单值控制的方式
>
> ```sql
> h_user user:id:3506728370    :name --> 春晚
> h_user user:id:3506728370    :fans --> 1222515345
> h_user user:id:3506728370    :blogs --> 5684
> ```
>
> 由于左边的主键是不变的 , 那如果我们将其属性合一的话 , 会有这样一种数据结构
> $$
> h\_user\ user:id:3506728370\{{name:春晚} & \\{fans:1225135863}
> $$

