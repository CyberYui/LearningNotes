# 通过域名直接访问部署在 tomcat 下的工程

--------

### 准备工作 : 

> 一台服务器 / 虚拟机
>
> 在服务器上配置好项目环境 , 安装好 tomcat
>
> 将项目放到 tomcat 下面的 webapp 目录里面
>
> 找到 tomcat 的 conf 目录下的 server.xml 文件

### 额外的准备工作 : 

* 确保防火墙端口开放 , 如 80 , 8080 , 8181 之类的

* > 如果没有开放请添加入站规则 (以 windows 为例)
  >
  > <kbd>控制面板</kbd>→<kbd>大图标</kbd>→<kbd>Windows Defender 防火墙</kbd>→<kbd>高级设置</kbd>→<kbd>入站规则</kbd>→<kbd>新建规则</kbd>

### 单个项目直接访问  : 

* tomcat 默认运行在电脑的 8080 端口下

* 假如我们放到 webapps 目录下的 jar 包名为 demo , tomcat 自动解压出来的文件夹也叫 demo

* 将 web 项目打包为 jar 包 , 放在 tomcat 路径下的 webapps 目录下 , 运行 tomcat , 就可以通过以下路径访问了

* 比如要访问 demo 路径下的 index.html 文件 , 就可以通过这样去访问

  ```http
  localhost:8080/demo/index.html
  ```

### 不修改端口  , 部署多个项目 : 

* > 我们知道在 tomcat 的 webapps 目录下我们要放项目 , 那么如果放多个项目是不是就能同时运行了呢 ?
  >
  > 答案是肯定的 , 二话不说都扔进去就可以了 , 那么要怎么访问呢 ?
  
* 比如我们有两个项目 , 都在 webapps 里面 , 一个是 index/index.html , 另一个是 demo/demo.html

* 我们用最基本的页面进行测试 , 实际的项目也是一样的 , 不同项目不同路径 , 你只要知道自己项目的入口即可

* >也就是说 , 我们要想访问 index/index.html 的话,就是这样的路径
  >
  >```http
  >localhost:8080/index/index.html
  >```
  >
  >要想访问 index/index.html 的话,就是这样的访问路径
  >
  >```http
  >localhost:8080/demo/index.html
  >```

* 可以看到我们都需要使用 <kbd>:8080</kbd> 这一后缀访问不同项目 , 如果只输入 ip 和项目路径就能访问的话 , 需要配置一些内容

  * 需要注意的是 , 本地能这样访问 , 但是服务器里面的话 , 还需要在 server.xml 里面配置一下

* 定位到 server.xml 文件的 Host 标签内 在 <kbd><Valve></kbd> 标签下面添加 <kbd>Context</kbd> 标签

* ```xml
  <Context docBase="erp" path="/erp" reloadble="true" />
  <Context docBase="ningmengban" path="/ningmengban" reloadble="true" />
  ```

  以上内容的解释如下:

  > **docBase属性:** 指定Web应用的文件路径，可以是绝对路径，也可以给定相对路径
  > **path属性:** 指定访问该Web应用的URL入口
  > **reloadable属性:** 若这个属性为true，tomcat服务器在运行状态下会监视WEB-INF/classes和WEB-INF/lib目录下class文件的改动，如果监测到class文件被更新，服务器会自动重新加载Web应用。

* 