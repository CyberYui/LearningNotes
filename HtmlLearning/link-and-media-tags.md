# 链接与媒体标签

> 创建超链接和嵌入多媒体内容

## 标签列表

### `<a>`

**作用:** 创建超链接

**常用场景:**
- 链接到其他页面
- 锚点链接
- 下载链接
- 邮件链接

**深度示例:** 见 [[Learning/link-media-tags.html]]

```html
<a href="https://www.example.com">外部链接</a>
<a href="#section1">锚点链接</a>
<a href="file.pdf" download>下载链接</a>
<a href="mailto:test@example.com">邮件链接</a>
<a href="tel:+1234567890">电话链接</a>
```

---

### `<img>`

**作用:** 嵌入图片

**常用场景:**
- 显示图片
- 响应式图片
- 图片加载失败时的替代文本

```html
<img src="image.jpg" alt="图片描述" width="300" height="200">
<img src="image.jpg" alt="图片描述" loading="lazy">
```

---

### `<video>`

**作用:** 嵌入视频

**常用场景:**
- 播放视频
- 自动播放
- 循环播放

```html
<video src="video.mp4" controls width="600">
  您的浏览器不支持视频播放。
</video>

<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
</video>
```

---

### `<audio>`

**作用:** 嵌入音频

**常用场景:**
- 播放音频
- 背景音乐

```html
<audio src="audio.mp3" controls>
  您的浏览器不支持音频播放。
</audio>
```

---

### `<source>`

**作用:** 为 `<video>` 或 `<audio>` 定义多个媒体源

**常用场景:**
- 提供多种格式兼容不同浏览器

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
</video>
```

---

### `<iframe>`

**作用:** 嵌入其他页面或内容

**常用场景:**
- 嵌入视频（YouTube）
- 嵌入地图
- 嵌入第三方内容

```html
<iframe src="https://www.example.com" width="600" height="400"></iframe>
<iframe src="https://www.youtube.com/embed/xxx" width="560" height="315"></iframe>
```

---

### `<map>` 和 `<area>`

**作用:** 创建图片热区链接

**常用场景:**
- 图片不同区域链接到不同页面
- 创建交互式图片地图

```html
<img src="map.jpg" alt="地图" usemap="#workmap">
<map name="workmap">
  <area shape="rect" coords="34,44,270,350" href="computer.html">
  <area shape="circle" coords="337,300,44" href="phone.html">
</map>
```
