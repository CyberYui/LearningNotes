# CSS 工程化

> 在大型项目中组织和管理 CSS 代码, 提升开发效率和代码质量

## 基础概念

即 (CSS engineering), 随着项目规模增长, CSS 代码会变得难以维护。工程化方法帮助团队更好地组织、管理和优化 CSS 代码。

## CSS 变量 (常用)

即 (CSS custom properties / CSS variables), CSS 变量允许存储和复用值, 是实现主题切换和全局配置的核心技术。

### 定义和使用

```css
/* 定义变量 */
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --font-size-base: 16px;
  --spacing-unit: 8px;
  --border-radius: 8px;
  --transition-speed: 0.3s;
}

/* 使用变量 */
.btn-primary {
  background-color: var(--primary-color);
  font-size: var(--font-size-base);
  border-radius: var(--border-radius);
  transition: background-color var(--transition-speed);
}
```

### 变量作用域

```css
:root {
  --color: blue;    /* 全局变量 */
}

.component {
  --color: red;     /* 局部覆盖, 只影响 .component 及其后代 */
}

.component .child {
  color: var(--color);  /* 红色 (继承局部变量) */
}

.other {
  color: var(--color);  /* 蓝色 (使用全局变量) */
}
```

### 变量回退值

```css
.element {
  color: var(--text-color, #333);              /* 单个回退 */
  font-family: var(--font-stack, system-ui, sans-serif); /* 多个回退 */
}
```

### 主题切换示例

```css
:root {
  --bg-color: white;
  --text-color: #333;
  --card-bg: #fff;
  --border-color: #ddd;
}

[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #e0e0e0;
  --card-bg: #2d2d2d;
  --border-color: #444;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}

.card {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
}
```

```html
<!-- 切换主题 -->
<button onclick="document.documentElement.setAttribute('data-theme', 'dark')">
  暗色主题
</button>
```

## CSS 架构 (中等)

即 (CSS architecture), 合理的命名和组织方式可以避免样式冲突, 提高代码可维护性。

### BEM 命名法

即 (Block Element Modifier), 最流行的 CSS 命名方法论。

**命名规则:**
- **Block (块):** 独立的、可复用的组件, 如 `.card`、`.navbar`
- **Element (元素):** 块内部的组成部分, 用 `__` 分隔, 如 `.card__title`
- **Modifier (修饰符):** 表示块或元素的不同状态或变体, 用 `--` 分隔, 如 `.card--featured`

```html
<!-- 一个卡片组件 -->
<div class="card card--featured">
  <img class="card__image" src="image.jpg" alt="图片">
  <div class="card__body">
    <h3 class="card__title">卡片标题</h3>
    <p class="card__description">卡片描述</p>
    <button class="card__btn card__btn--primary">主要按钮</button>
    <button class="card__btn card__btn--secondary">次要按钮</button>
  </div>
</div>
```

```css
/* Block */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

/* Modifier */
.card--featured {
  border-color: #007bff;
  box-shadow: 0 4px 12px rgba(0, 123, 255, 0.2);
}

/* Elements */
.card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card__body {
  padding: 16px;
}

.card__title {
  font-size: 1.25rem;
  margin-bottom: 8px;
}

.card__description {
  color: #666;
  margin-bottom: 16px;
}

.card__btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.card__btn--primary {
  background-color: #007bff;
  color: white;
}

.card__btn--secondary {
  background-color: #f5f5f5;
  color: #333;
}
```

### BEM 的优势

- **可读性:** 从命名就能看出元素的结构关系
- **可复用性:** 块可以在不同页面复用
- **低 specificity:** 避免过高的优先级, 减少冲突
- **团队协作:** 统一的命名规范, 便于团队沟通

## 选择器性能 (了解)

即 (selector performance), CSS 选择器从右到左匹配, 了解这一机制可以写出更高效的样式。

### 匹配原理

```css
/* 浏览器匹配顺序: 先找到所有 .item, 再过滤 .list > .item, 最后匹配 .container > .list > .item */
.container > .list > .item {
  color: red;
}
```

### 性能建议

```css
/* ❌ 避免过深的选择器 */
div > ul > li > a > span { }

/* ✅ 尽量简短 */
.nav-link { }

/* ❌ 避免使用通配符作为关键选择器 */
.container * { }

/* ✅ 使用具体的类名 */
.container .item { }

/* ❌ 避免不必要的标签名修饰 */
div.container { }

/* ✅ 直接使用类名 */
.container { }
```

## CSS 新特性 (了解)

即 (modern CSS), CSS 近年来增加了很多强大的新特性。

### 容器查询 @container

即 (container queries), 根据父容器的大小 (而非视口) 应用样式, 是组件级响应式的核心。

```css
/* 定义容器 */
.card-container {
  container-type: inline-size;
}

/* 容器宽度大于 400px 时的样式 */
@container (min-width: 400px) {
  .card {
    display: flex;
    flex-direction: row;
  }
}

/* 容器宽度小于 400px 时的样式 */
@container (max-width: 399px) {
  .card {
    display: flex;
    flex-direction: column;
  }
}
```

### 层叠层 @layer

即 (cascade layers), 允许显式控制层叠顺序, 解决大型项目中样式优先级混乱的问题。

```css
/* 定义层级顺序 (先定义的优先级低) */
@layer reset, base, components, utilities;

/* 在指定层级中定义样式 */
@layer base {
  body { font-family: sans-serif; }
}

@layer components {
  .btn { padding: 8px 16px; }
}

@layer utilities {
  .text-center { text-align: center; }
}
```

### :has() 选择器

即 (relational pseudo-class), 可以根据子元素的状态来设置父元素的样式, 被称为 "父选择器"。

```css
/* 如果 .card 包含 .badge, 则添加边框 */
.card:has(.badge) {
  border-color: #007bff;
}

/* 如果表单包含无效输入, 显示错误提示 */
form:has(:invalid) {
  border-color: red;
}

/* 选择后面紧跟 <h2> 的 <h1> */
h1:has(+ h2) {
  margin-bottom: 0;
}
```

### CSS 嵌套 (原生)

即 (native CSS nesting), CSS 现在原生支持嵌套语法, 类似 Sass/SCSS。

```css
/* 传统写法 */
.card { border: 1px solid #ddd; }
.card .title { font-size: 1.25rem; }
.card .description { color: #666; }
.card:hover { box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }

/* 嵌套写法 */
.card {
  border: 1px solid #ddd;

  & .title {
    font-size: 1.25rem;
  }

  & .description {
    color: #666;
  }

  &:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
}
```

**注意:** CSS 嵌套虽然方便, 但过度嵌套会增加选择器复杂度, 建议嵌套不超过 3 层。
