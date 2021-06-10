# 通过域名直接访问部署在 tomcat 下的工程

--------

### 准备工作 ( 基本流程 ) : 

> 一台服务器 / 虚拟机
>
> 在服务器上配置好项目环境 , 安装好 tomcat
>
> 将项目放到 tomcat 下面的 <kbd>webapps</kbd> 目录里面
>
> 找到 tomcat 的 conf 目录下的 <kbd>server.xml</kbd> 文件修改配置
>
> 在浏览器输入项目入口 , 运行项目

### 额外的准备工作 : 

* 确保防火墙端口开放 , 如 80 , 8080 , 8181 之类的

* > 如果没有开放请添加入站规则 (以 windows 为例)
  >
  > <kbd>控制面板</kbd>→<kbd>大图标</kbd>→<kbd>Windows Defender 防火墙</kbd>→<kbd>高级设置</kbd>→<kbd>入站规则</kbd>→<kbd>新建规则</kbd>

### 单个项目直接访问  : 

* tomcat 默认运行在电脑的 8080 端口下

* 假如我们放到 <kbd>webapps</kbd> 目录下的 jar 包名为 demo , tomcat 自动解压出来的文件夹也叫 demo

* 将 web 项目打包为 jar 包 , 放在 tomcat 路径下的 <kbd>webapps</kbd> 目录下 , 运行 tomcat , tomcat 自动解压之后 , 就可以通过以下方式访问了

* 比如要访问 demo 路径下的 index.html 文件 , 就可以通过这样去访问

  ```http
  localhost:8080/demo/index.html
  ```

### 不修改端口  , 部署多个项目 : 

* > 我们知道在 tomcat 的 <kbd>webapps</kbd> 目录下我们要放项目 , 那么如果放多个项目是不是就能同时运行了呢 ?
  >
  > 答案是肯定的 , 二话不说 , 把项目都扔进去就可以了吗 ? 那么要怎么访问呢 ?
  
  <font color="#9f7fac">**使用流程很简单**</font>
  
* 比如我们有两个项目 , 都在 <kbd>webapps</kbd> 里面 , 一个是 index/index.html , 另一个是 demo/demo.html

* 为了方便 , 我们仅仅在两个目录里面分别创建了一个 html 文件 , 也就是用最基本的页面进行测试运行 , 实际的项目也是一样的 , 不同项目在不同的目录下 , 你只需要知道每个项目的入口即可

* >比如说 , 我们要想访问 webapps/index/index.html 的话,就是这样的路径
  >
  >```http
  >localhost:8080/index/index.html
  >```
  >
  >要想访问 webapps/demo/index.html 的话,就是这样的访问路径
  >
  >```http
  >localhost:8080/demo/index.html
  >```

* 可以看到我们都需要使用 <kbd>:8080</kbd> 这一后缀访问不同项目 , 如果只输入 ip 和项目路径就能访问的话 , 需要配置一些内容 , 比如将 80 端口配置给一个 service , 这样直接通过 ip 就能访问到配置的项目 , 往后看就可以自己了解这个方法了

  * 需要注意的是 , 在某些机器上 , 本地能通过这样的方式访问项目 , 但是如果是在 windows server 服务器里面的话 , 还需要在服务器的 tomcat 的 server.xml 里面配置一下以下内容

* 定位到 server.xml 文件的 Host 标签内 在 <kbd>Valve</kbd> 标签下面添加 <kbd>Context</kbd> 标签 , 其内容有多种写法

* ```xml
  <Context path="/index.html" docBase="/erp/" reloadble="true" />
  <Context path="/ningmengban/index.html" docBase="ningmengban" reloadble="true" />
  <Context path="/" docBase="/thinktank/" debug="5" reloadable="true"/>
  ```

  以上内容的解释如下:

  > **docBase属性:** 指定Web应用的文件路径，可以是绝对路径，也可以给定相对路径
  > **path属性:** 指定访问该Web应用的URL入口
  >
  > <font color="#c461d4">[PS] docbase 是 web 应用和本地路径 , 即项目的路径 , path是 tomcat 访问这个应用的 URL 路径</font>
  >
  > **debug属性:** 设定debug level , 0表示提供最少的信息 , 9表示提供最多的信息 , 这是tomcat日志调试信息 , 数字越高 , 日志越详细
  >
  > > 这里要提醒一下 , 比如我们原先访问 /erp 项目中的 index.html , 需要这样输入地址
  > >
  > > ( 假定服务器的 ip地址 为 1.1.1.1 )
  > >
  > > ```http
  > > 1.1.1.1:8080/erp/index.html
  > > ```
  > >
  > > 当我们配置了 <kbd>Context</kbd> 标签内容之后 , 我们可以直接输入端口和目标项进行访问
  > >
  > > * 比如我们配置 <kbd>Context</kbd> 内容为
  > >
  > > ```xml
  > > <Context path="/index.html" docBase="/erp/" reloadble="true" />
  > > ```
  > >
  > > 这样就能通过以下地址直接访问 /erp/ 目录下的 index.html 了
  > >
  > > ```http
  > > 1.1.1.1:8080/index.html
  > > ```
  > >
  > > * 再比如我们这样配置
  > >
  > > ```xml
  > > <Context path="/ningmengban/index.html" docBase="ningmengban" reloadble="true" />
  > > ```
  > >
  > > 这样就能通过以下地址直接访问 /ningmengban/ 目录下的 index.html 了
  > >
  > > ```http
  > > 1.1.1.1:8080/ningmengban
  > > ```
  > >
  > > * 综上可得 , 当我们配置了 80 端口之后 , 就可以通过给项目配置 <kbd>Context</kbd> 内容的方式去掩盖项目路径了
  > >
  > > 比如我们有个项目其入口原地址为
  > >
  > > ```http
  > > 1.1.1.1:8080/thinktank/login/user/index.html
  > > ```
  > >
  > > 那么我们可以通过这样配置 <kbd>Context</kbd> 内容进行直接访问 index.html
  > >
  > > ```xml
  > > <Context path="/" docBase="/thinktank/login/user/" debug="5" reloadable="true"/>
  > > ```
  > >
  > > [PS]显然 , 当多个项目都有 index.html 时 , 如果给多个项目都配置了 <kbd>Context</kbd> 标签内容 , 那么键入不同的docBase 名称就能访问到不同的项目了
  >
  > **reloadable属性:** 若这个属性为true，tomcat服务器在运行状态下会监视WEB-INF/classes和WEB-INF/lib目录下class文件的改动，如果监测到class文件被更新，服务器会自动重新加载Web应用。

* 有了这些配置之后 , 重启 tomcat 即可实现通过不同的地址访问不同的项目

* localhost:8080 会直接显示 tomcat 的欢迎页面 , 实际是进入了 <kbd>webapps</kbd> 目录里面的 <kbd>ROOT</kbd> 项目

有了上面的基础 , 我们就可以配置多个项目了 , 首先是直接将项目扔进 <kbd>webapps</kbd> 目录里面进行运行 tomcat 访问

* 想要访问第一个项目 , 就这样访问即可 , register.html 是我项目的入口

* ```html
  localhost:8080/ningmengban/app/register/regiseter.html
  <!-- 或者 -->
  本机ip:8080/ningmengban/app/register/regiseter.html
  ```

* 同理访问第二个项目

* ```html
  localhost:8080/erp/regist
  <!-- 或者 -->
  ip:8080/erp/regist
  ```
  
* 当然 , 可以把 /ningmengban/app/register/ 这种路径省去 , 具体的 Context 配置略

--------------------------------

#### 针对错误的提示

* 可以通过 tomcat 的 manager 查看项目是否启动了 , 在 http://localhost:8080/manager/html 上查看

* 在 tomcat → conf → tomcat-users.xml 里面的 <kbd>tomcat-users</kbd> 标签内部设置以下内容

* ```xml
    <role rolename="tomcat"/>
    <role rolename="role1"/>
    <role rolename="manager-gui"/>
    <user username="tomcat" password="tomcat" roles="tomcat,manager-gui"/>
  ```

* [运行项目的时候 , 出错时一定要看]

  1. tomcat 的启动端口是否正确
  2. 是否输入了正确的路径地址
  3. 项目打包前是否指定了 tomcat 的版本
  4. 项目内部是否有针对 tomcat 的设置

-----------------------

### 修改端口 , 部署多个项目 :

* 在之前的部署我们可以看到 , 我们的多个项目都跑在 8080 端口上面 , 计算机里面这么多端口 , 能不能多用几个呢?
* 也就是是不是可以通过配置 tomcat , 实现在不同端口跑不同项目的结果呢?
* 答案也是肯定的

> 事实上整个电脑可供使用的端口一共有 65535 个

* 我们知道之前我们的项目都放在 <kbd>webapps</kbd> 目录里面就是通过 8080 端口访问

* 那么计算机怎么知道我们的 8080 端口就是对应 <kbd>webapps</kbd> 目录呢?

* 事实上也是在 <kbd>server.xml</kbd> 里面配置了的

* 定位 tomcat 的 <kbd>server.xml</kbd> 里面的如下内容

* ```xml
  <Service name="Catalina">
  ```

* 在它的里面有这么一段

* ```xml
  <Connector connectionTimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443"/>
  ```

* 很显然 , <kbd>Connector</kbd> 标签里面定义了一个名为 Catalina 的 Service 跑在 8080 端口上

* 下面进行解释

* connectionTimeout 表示超时时间 , 20000 就表示 20000s

* protocol 属性定义了协议类型 , 这里是 http 协议 , 同类的还有 AJP 协议 , 其配置类似这样

* ```xml
  <Connector port="8010" protocol="AJP/1.3" redirectPort="8443" />
  ```

* port 定义了 Service 通过不同 protocol 协议跑的端口位置 , redirectPort 是重定向端口

  -------------------------

* 再往下

* ```xml
  <Engine defaultHost="localhost" name="Catalina">
  ```

* 这里设定了默认主机为 localhost , 并且再次说明了本 Service 的名字是 Catalina

* 接着往下

* ```xml
  <Host appBase="webapps" autoDeploy="true" name="localhost" unpackWARs="true">
  ```

* 看到了吗 , 这里定义了 appBase 是 webapps , 也就是说跑在 8080 端口上的名为 Catalina 的 Service 其应用基地是 webapps 文件夹

* 至此,我们算是明白了基本的一些配置 , 下面我们可以创建我们自己的 Service 了

  --------------------

* 首先直接复制一个 Service 出来 , 并把它改成这样

* ```xml
  <!-- 第二个项目配置 -->
  <Service name="Catalina1">
    <!-- 8080为http访问端口，为避免冲突，修改端口 -->
    <Connector port="8081" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
    <!-- 8009为AJP端口，Apache能通过AJP协议访问Tomcat的8009端口，避免冲突,修改 -->
    <Connector port="8010" protocol="AJP/1.3" redirectPort="8443" />
    <!-- Engine节点，name修改为Catalina1 -->
    <Engine name="Catalina1" defaultHost="localhost">
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm" resourceName="UserDatabase"/>
      </Realm>
      <!-- 修改Host节点，appBase修改为webapps1 -->
      <Host name="localhost"  appBase="webapps1" unpackWARs="true" autoDeploy="true">
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />
      </Host>
    </Engine>
  </Service>
  ```
  
* 总共修改的有这些:

* <kbd>Service</kbd> 标签的 <font color="#dc307b">**name**</font> 属性修改为 **Catelina1**
  http 协议访问 ,  <kbd>Connector</kbd> 标签的 <font color="#dc307b">**port**</font> 属性修改为 **8081**
  AJP 协议访问的 <kbd>Connector</kbd> 标签的 <font color="#dc307b">**port**</font> 属性修改为 **8010**
  <kbd>Engine</kbd> 标签的 <font color="#dc307b">**name**</font> 属性修改为 **Catelina1**
  <kbd>Host</kbd> 标签的 <font color="#dc307b">**appBase**</font> 属性修改为 **webapps1**

* 接下来就可以通过不同的端口访问不同的项目了

* 比如要访问第一个跑在 8080 端口 <kbd>Service</kbd> 里面的项目

* 即可通过以下地址访问

* ```html
  localhost:8080/ningmengban/app/register/regiseter.html
  <!-- 或者 -->
  ip:8080/ningmengban/app/register/regiseter.html
  ```

* 第二个项目跑在 8081 端口上 , 访问地址为

* ```html
  localhost:8081/erp/regist
  <!-- 或者 -->
  ip:8081/erp/regist
  ```

#### 以上就是如何在 tomcat 里面部署项目的说明 , 希望能帮到正在看文档的你