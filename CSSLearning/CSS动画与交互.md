# CSS 动画与交互

> 为页面元素添加动态效果和交互反馈, 提升用户体验

## 基础概念

即 (CSS animations), CSS 提供了三种方式创建动画效果: **Transition (过渡)**、**Transform (变换)** 和 **Animation (关键帧动画)**。

CSS 动画 vs JS 动画:
- **CSS 动画:** 适合简单的状态变化和装饰性动画, 性能更好, 代码更简洁
- **JS 动画:** 适合复杂的交互动画和需要精确控制的场景

**性能提示:** 优先使用 `transform` 和 `opacity` 做动画, 这两个属性不会触发重排 (reflow), 只触发重绘 (repaint) 或合成 (composite), 性能最好。

## Transition (常用)

即 (transition), 用于在两个状态之间平滑过渡, 当元素的状态改变 (如 hover、focus) 时自动播放。

### 基本语法

```css
.element {
  transition: property duration timing-function delay;
  /* 属性 时长 缓动函数 延迟 */
}

/* 示例 */
.btn {
  background-color: #007bff;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}
```

### transition-property

指定要过渡的 CSS 属性。

```css
.element {
  transition-property: all;           /* 所有属性 (默认) */
  transition-property: background;   /* 仅背景 */
  transition-property: background, transform; /* 多个属性 */
  transition-property: none;          /* 无过渡 */
}
```

### transition-duration

指定过渡的时长。

```css
.element {
  transition-duration: 0.3s;    /* 300ms */
  transition-duration: 300ms;
}
```

### transition-timing-function

指定过渡的速度曲线。

```css
.element {
  transition-timing-function: ease;          /* 慢-快-慢 (默认) */
  transition-timing-function: ease-in;       /* 慢入 */
  transition-timing-function: ease-out;      /* 慢出 */
  transition-timing-function: ease-in-out;   /* 慢入慢出 */
  transition-timing-function: linear;        /* 匀速 */
  transition-timing-function: cubic-bezier(0.68, -0.55, 0.27, 1.55); /* 自定义 */
}
```

### transition-delay

指定过渡的延迟时间。

```css
.element {
  transition-delay: 0.2s;    /* 延迟 200ms 后开始 */
}
```

### 多个过渡

```css
.element {
  transition:
    background-color 0.3s ease,
    transform 0.2s ease-in-out,
    box-shadow 0.3s ease;
}
```

## Transform (常用)

即 (transform), 用于对元素进行位移、旋转、缩放、倾斜等变换, 不触发重排。

### translate (位移)

```css
.element {
  transform: translateX(50px);      /* 水平移动 */
  transform: translateY(-20px);     /* 垂直移动 */
  transform: translate(50px, -20px); /* 同时水平+垂直 */
  transform: translate(-50%, -50%);  /* 居中常用 */
}
```

### rotate (旋转)

```css
.element {
  transform: rotate(45deg);     /* 顺时针 45° */
  transform: rotate(-90deg);    /* 逆时针 90° */
  transform: rotateX(180deg);   /* 绕 X 轴旋转 */
  transform: rotateY(180deg);   /* 绕 Y 轴旋转 */
}
```

### scale (缩放)

```css
.element {
  transform: scale(1.2);        /* 放大 1.2 倍 */
  transform: scale(0.8);        /* 缩小到 80% */
  transform: scaleX(1.5);       /* 仅水平缩放 */
  transform: scaleY(0.5);       /* 仅垂直缩放 */
}
```

### skew (倾斜)

```css
.element {
  transform: skewX(15deg);      /* 水平倾斜 */
  transform: skewY(-10deg);     /* 垂直倾斜 */
  transform: skew(15deg, -10deg); /* 同时倾斜 */
}
```

### transform-origin

指定变换的原点。

```css
.element {
  transform-origin: center;           /* 中心 (默认) */
  transform-origin: top left;         /* 左上角 */
  transform-origin: 50% 100%;         /* 底部中心 */
  transform-origin: 10px 20px;        /* 指定坐标 */
}
```

### 组合变换

```css
.element {
  transform: translateX(50px) rotate(45deg) scale(1.2);
  /* 注意: 顺序很重要, 先写的先执行 */
}
```

## Animation (中等)

即 (keyframes animation), 通过 `@keyframes` 定义动画的关键帧, 创建更复杂的动画效果。

### 基本语法

```css
/* 定义动画 */
@keyframes animation-name {
  0% {
    /* 起始状态 */
  }
  100% {
    /* 结束状态 */
  }
}

/* 使用动画 */
.element {
  animation: name duration timing-function delay iteration-count direction fill-mode;
}
```

### 示例详解

```css
.element {
  animation-name: fadeIn;                    /* 动画名称 */
  animation-duration: 1s;                  /* 动画时长 */
  animation-timing-function: ease-in-out;   /* 速度曲线 */
  animation-delay: 0.5s;                   /* 延迟 */
  animation-iteration-count: infinite;     /* 播放次数 (数字或 infinite) */
  animation-direction: alternate;          /* 播放方向 */
  animation-fill-mode: forwards;           /* 结束后状态 */
  animation-play-state: running;            /* 播放状态 */
}

/* 简写 */
.element {
  animation: fadeIn 1s ease-in-out 0.5s infinite alternate forwards;
}
```

### animation-direction

```css
.element {
  animation-direction: normal;        /* 正向播放 */
  animation-direction: reverse;       /* 反向播放 */
  animation-direction: alternate;     /* 正反交替 */
  animation-direction: alternate-reverse; /* 反正交替 */
}
```

### animation-fill-mode

```css
.element {
  animation-fill-mode: none;       /* 默认, 回到初始状态 */
  animation-fill-mode: forwards;   /* 保持结束状态 */
  animation-fill-mode: backwards;  /* 保持开始状态 (有延迟时) */
  animation-fill-mode: both;      /* forwards + backwards */
}
```

### 示例动画

#### 淡入动画

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: fadeIn 0.5s ease-in forwards;
}
```

#### 弹跳动画

```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.bounce {
  animation: bounce 1s ease-in-out infinite;
}
```

#### 加载动画 (旋转)

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
```

#### 脉冲动画

```css
@keyframes pulse {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.7; }
  100% { transform: scale(1); opacity: 1; }
}

.pulse {
  animation: pulse 2s ease-in-out infinite;
}
```

## 性能优化提示

即 (performance tips), CSS 动画的性能直接影响用户体验。

### 高性能属性 (推荐)

以下属性不会触发重排, 只做合成, 性能最好:

```css
/* 使用 transform 代替 top/left */
/* ❌ 差 */
.element {
  position: absolute;
  top: 100px;
  left: 200px;
  transition: top 0.3s, left 0.3s;
}

/* ✅ 好 */
.element {
  position: absolute;
  transform: translate(200px, 100px);
  transition: transform 0.3s;
}

/* 使用 opacity 代替 visibility/display 做淡入淡出 */
.element {
  opacity: 0;
  transition: opacity 0.3s;
}
```

### will-change (谨慎使用)

提示浏览器哪些属性即将变化, 让浏览器提前优化:

```css
.element {
  will-change: transform, opacity;
}

/* 动画结束后移除 */
.element.animation-done {
  will-change: auto;
}
```

### 避免动画过多

- 同时动画的元素不要太多
- 移动端减少动画效果
- 考虑用户的 `prefers-reduced-motion` 设置:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
