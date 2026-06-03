# 表单标签

> 创建用户交互界面

## 标签列表

### `<form>`

**作用:** 定义表单，用于收集用户输入

**常用场景:**
- 登录表单
- 注册表单
- 搜索表单

**深度示例:** 见 [[Learning/form-tags.html]]

```html
<form action="/submit" method="POST">
  <label for="username">用户名:</label>
  <input type="text" id="username" name="username">
  <button type="submit">提交</button>
</form>
```

---

### `<input>`

**作用:** 定义输入控件

**常用场景:**
- 文本输入框
- 密码框
- 复选框
- 单选按钮
- 文件上传
- 日期选择

```html
<input type="text" name="username">
<input type="password" name="password">
<input type="email" name="email">
<input type="number" name="age" min="0" max="120">
<input type="checkbox" name="agree" id="agree">
<input type="radio" name="gender" value="male" id="male">
<input type="file" name="avatar">
<input type="date" name="birthday">
<input type="submit" value="提交">
<input type="reset" value="重置">
```

---

### `<select>`

**作用:** 定义下拉选择列表

**常用场景:**
- 选择省份
- 选择类别
- 单选下拉

```html
<select name="city">
  <option value="">请选择城市</option>
  <option value="beijing">北京</option>
  <option value="shanghai">上海</option>
  <option value="guangzhou">广州</option>
</select>

<!-- 多选 -->
<select name="hobbies" multiple>
  <option value="reading">阅读</option>
  <option value="gaming">游戏</option>
  <option value="traveling">旅行</option>
</select>
```

---

### `<option>`

**作用:** 定义下拉列表中的选项

**常用场景:**
- 作为 `<select>` 的子元素
- 可以设置默认选中

```html
<select name="country">
  <option value="china" selected>中国</option>
  <option value="usa">美国</option>
  <option value="japan">日本</option>
</select>
```

---

### `<textarea>`

**作用:** 定义多行文本输入框

**常用场景:**
- 留言框
- 评论区
- 长文本输入

```html
<textarea name="message" rows="5" cols="50" placeholder="请输入留言..."></textarea>
```

---

### `<button>`

**作用:** 定义按钮

**常用场景:**
- 提交按钮
- 重置按钮
- 普通按钮

```html
<button type="submit">提交</button>
<button type="reset">重置</button>
<button type="button" onclick="alert('点击了')">普通按钮</button>
```

---

### `<label>`

**作用:** 定义输入控件的标签

**常用场景:**
- 提升可访问性
- 点击标签聚焦输入框

```html
<label for="email">邮箱:</label>
<input type="email" id="email" name="email">
```

---

### `<fieldset>`

**作用:** 定义表单中的分组

**常用场景:**
- 将相关输入分组
- 提升表单可读性

```html
<fieldset>
  <legend>个人信息</legend>
  <label for="name">姓名:</label>
  <input type="text" id="name" name="name">
  <label for="age">年龄:</label>
  <input type="number" id="age" name="age">
</fieldset>
```

---

### `<legend>`

**作用:** 定义 `<fieldset>` 的标题

**常用场景:**
- 描述分组内容

```html
<fieldset>
  <legend>登录信息</legend>
  <!-- 表单内容 -->
</fieldset>
```

---

### `<datalist>`

**作用:** 定义输入控件的预定义选项

**常用场景:**
- 自动完成
- 搜索建议

```html
<input list="browsers" name="browser">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Safari">
  <option value="Edge">
</datalist>
```

---

### `<output>`

**作用:** 定义计算结果

**常用场景:**
- 显示计算结果
- 实时反馈

```html
<input type="number" id="num1" value="0">
<input type="number" id="num2" value="0">
<output id="result">0</output>
```

---

### `<progress>`

**作用:** 定义进度条

**常用场景:**
- 文件上传进度
- 任务完成度

```html
<progress value="70" max="100">70%</progress>
```

---

### `<meter>`

**作用:** 定义度量衡（标量测量）

**常用场景:**
- 磁盘使用量
- 评分显示

```html
<meter value="0.7" min="0" max="1">70%</meter>
<meter value="60" min="0" max="100" low="30" high="70" optimum="50">60分</meter>
```
