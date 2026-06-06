# 表格标签

> 展示结构化数据

## 标签列表

### `<table>`

**作用:** 定义表格

**常用场景:**
- 展示数据表格
- 布局（不推荐）

**深度示例:** 见 [[Learning/table-tags.html]]

```html
<table>
  <tr>
    <th>姓名</th>
    <th>年龄</th>
  </tr>
  <tr>
    <td>张三</td>
    <td>25</td>
  </tr>
</table>
```

---

### `<tr>`

**作用:** 定义表格行

**常用场景:**
- 作为 `<table>` 的子元素
- 包含 `<td>` 或 `<th>`

```html
<table>
  <tr>
    <td>单元格 1</td>
    <td>单元格 2</td>
  </tr>
</table>
```

---

### `<td>`

**作用:** 定义表格数据单元格

**常用场景:**
- 表格数据内容
- 可以 colspan 和 rowspan

```html
<table>
  <tr>
    <td colspan="2">合并两个单元格</td>
  </tr>
  <tr>
    <td rowspan="2">合并两行</td>
    <td>单元格</td>
  </tr>
</table>
```

---

### `<th>`

**作用:** 定义表头单元格

**常用场景:**
- 表格标题行
- 默认加粗居中

```html
<table>
  <tr>
    <th>表头 1</th>
    <th>表头 2</th>
  </tr>
</table>
```

---

### `<thead>`

**作用:** 定义表格头部

**常用场景:**
- 语义化表格结构
- 配合 `<tbody>` 和 `<tfoot>`

```html
<table>
  <thead>
    <tr>
      <th>标题</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>内容</td>
    </tr>
  </tbody>
</table>
```

---

### `<tbody>`

**作用:** 定义表格主体

**常用场景:**
- 包含表格主要内容
- 可以独立滚动

```html
<table>
  <tbody>
    <tr>
      <td>数据 1</td>
    </tr>
    <tr>
      <td>数据 2</td>
    </tr>
  </tbody>
</table>
```

---

### `<tfoot>`

**作用:** 定义表格尾部

**常用场景:**
- 汇总信息
- 表格注释

```html
<table>
  <tfoot>
    <tr>
      <td>合计</td>
    </tr>
  </tfoot>
</table>
```

---

### `<caption>`

**作用:** 定义表格标题

**常用场景:**
- 描述表格内容
- 提升可访问性

```html
<table>
  <caption>用户信息表</caption>
  <tr>
    <th>姓名</th>
    <th>年龄</th>
  </tr>
</table>
```
