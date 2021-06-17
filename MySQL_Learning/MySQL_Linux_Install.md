# MySQL 的安装 ( tar.gz ) - for Linux

--------------------

### 下载

* [PS] 以 CentOS 7 为例 , 在此系统中安装解压版 MySQL

* 进入以下页面下载适用于 Linux 的 MySQL 数据库

* https://dev.mysql.com/downloads/mysql/

  > 一般来说我们使用 Linux 是为了开发和部署环境 , 我们会安装最为稳定和市场上常用的 MySQL 版本
  >
  > 比如现在常用 5.7 版本的 MySQL , 但是至写下此文章时 MySQL 已有 8.0.25 的版本了
  >
  > 所以我们需要去下载先前版本的 MySQL
  >
  > 在下载页面选择以下选项进入先前版本的相关页面 : 
  >
  > ![MySQL_Linux_Download](\MySQL_Linux_Download.png)
  >
  > 一般会直接跳转到 5.7 版本的 MySQL 下载目录
  >
  > 在这里选择系统为 <kbd>Linux - Generic</kbd> 然后在下面的下载中选择类似于这样的版本
  >
  > <kbd>Linux - Generic(glibc 2.12)(x86, 64-bit),Compressed TAR Archive</kbd> 
  >
  > 注意这里的下载版本只有 Archive 后缀 , 没有或者多出 Test Suite 都是不行的
  >
  > ![MySQL_Linux_Download_1](\MySQL_Linux_Download_1.png)
  >
  > [PS] 下载的时候可能需要使用 VPN 等工具 , 下载页面会提示登录 , 选择左下角的 <font color="#b1e1d2">No thanks , just start my download</font>即可正常下载了

### 安装

* 当我们下载完成之后 , 会获得一个 *.tar.gz 的压缩包 , 接下来就是把它放到 Linux 里面并且解压了

* 比如我这里下载的是 <kbd>mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz</kbd> 

* 不同于 Windows 的解压方式 , 我们一般使用的 Linux 都是命令行界面 , 一般我们会用到 XShell 工具套件

* 首先进入 NETSARANG 的下载地址页面 https://www.netsarang.com/en/xshell-download/

* XShell 套件商业授权版是要收费的 , 我们只是用于个人用途 , 点击页面右侧的 Free Licensing Page

  ![XShell_Download](\XShell_Download.png)

* 在进入的页面中输入你的名字和邮箱 , 我们需要 XShell 和 XFTP 两款软件 , 直接勾选 both 选项即可

  ![XShell_Download_person](\XShell_Download_person.png)

* XShell 的使用也十分简单 , 当安装完成后 , 桌面会有相应的图标 , 它们分别长这样

  ![XShell](\XShell.png) ![XFTP](\XFTP.png)

* 双击 Xshell 打开程序 , 我们要通过它建立和 Linux 系统的连接

* 首先需要知道你的 Linux 系统 ip 是多少 , 有时候我们 Linux 系统的 ip 地址是自动分配的

* 这种自动 ip 地址虽然不需要过多配置 , 但是一旦我们重启服务器可能就会有一个新的 ip 地址

* 为了方便使用 , 建议给 Linux 配置一下静态 ip 地址

* 首先进入 Linux 系统查看系统的 ip 地址 , 我们一般使用 ifconfig 即可获取 Linux 主机的 IP 地址

  ```shell
  [root@localhost ~]# ifconfig
  enp1s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
          inet 192.168.2.34  netmask 255.255.255.0  broadcast 192.168.2.255
          inet6 fe80::1e1b:dff:fe9a:b02  prefixlen 64  scopeid 0x20<link>
          ether 1c:1b:0d:9a:0b:02  txqueuelen 1000  (Ethernet)
          RX packets 1523547  bytes 1862955308 (1.7 GiB)
          RX errors 0  dropped 0  overruns 0  frame 0
          TX packets 203711  bytes 19072508 (18.1 MiB)
          TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  
  lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
          inet 127.0.0.1  netmask 255.0.0.0
          inet6 ::1  prefixlen 128  scopeid 0x10<host>
          loop  txqueuelen 1000  (Local Loopback)
          RX packets 68  bytes 5768 (5.6 KiB)
          RX errors 0  dropped 0  overruns 0  frame 0
          TX packets 68  bytes 5768 (5.6 KiB)
          TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  ```

* 有的时候你的电脑可能会提示没有 ifconfig 这个命令 , 执行 <kbd>yum install net-tools.x86_64</kbd> 安装一下即可

* 在最精简版的 CentOS 7 中 , 如果没有安装 ifconfig 相关工具 , 只有使用 <kbd>ip addr</kbd> 才能直接查看 ip 地址

* 查完 ip 地址 , 记住 enxxx 后面的 inet 内容即可开始下一步连接操作了 , 比如我这里的 ip 是 <kbd>192.168.2.34</kbd> 

* [PS] 需要保证 Linux 系统中有 ssh 插件 , 一般我们安装好的 Linux 系统都有 , 直接在这里建立连接即可

* 单机文件下方的新建 ![](\XShell_newCo.png) 图标 , 在打开的表单中修改和输入以下内容创建和 Linux 的连接

  ![XShell_new](\XShell_new.png)

* 确定之后会自动打开命令行界面 , 也就是可以直接使用 shell 控制 Linux 系统了

  

