# 其他标签

> 提供特殊功能和增强内容

## 标签列表

### `<div>`

**作用:** 定义文档中的分区或节（通用容器）

**常用场景:**
- 布局容器
- 分组元素
- 应用 CSS 样式

```html
<div class="container">
  <h2>标题</h2>
  <p>内容</p>
</div>
```

---

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

---

### `<mark>`

**作用:** 定义高亮文本

**常用场景:**
- 搜索结果高亮
- 强调重要内容

```html
<p>这是<mark>高亮</mark>文本。</p>
```

---

### `<time>`

**作用:** 定义时间

**常用场景:**
- 日期和时间
- 机器可读的时间格式

```html
<p>发布于 <time datetime="2024-01-15">2024年1月15日</time></p>
<p>会议时间: <time datetime="14:00">下午2点</time></p>
```

---

### `<wbr>`

**作用:** 定义文本在何处换行

**常用场景:**
- 长 URL 或单词
- 防止在不合适的位置换行

```html
<p>
  这是一个很长的URL: https://example.com/this/is/a/very/long/path/that/should/wrap/at/this/point
</p>
```

---

### `<bdi>` 和 `<bdo>`

**作用:** 定义文本方向

**常用场景:**
- 双向文本隔离
- 覆盖文本方向

```html
<p>这段文字包含 <bdi>RTL 文本</bdi> 和 LTR 文本。</p>
<p><bdo dir="rtl">这段文字从右到左显示。</bdo></p>
```

---

### `<ruby>`, `<rt>`, `<rp>`

**作用:** 定义东亚字符的注音

**常用场景:**
- 中文拼音
- 日文假名

```html
<ruby>
  汉 <rp>(</rp><rt>hàn</rt><rp>)</rp>
  字 <rp>(</rp><rt>zì</rt><rp>)</rp>
</ruby>
```
