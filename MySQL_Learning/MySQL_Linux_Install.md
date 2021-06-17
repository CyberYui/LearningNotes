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

-------------------------

### 下载安装 XShell 套件连接 Linux 

* **( 不想使用此方法可以跳过此项 , 使用后面的另一种下载方式下载 MySQL 解压版 )**

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

  ![XShell_connectLinux](\XShell_connectLinux.png)

* 接下来把我们刚刚下好的 <kbd>mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz</kbd> 包放进 Linux

* 打开刚刚连接了的 Linux 标签 , 从 XShell 上侧工具栏选择 XFTP 工具 ![XShell_xftp](\XShell_xftp.png) 

* 接下来 XFTP 界面会直接弹出并连接好 Linux , 并展示出你的 Windows 和 Linux 目录

* 把包直接从左侧的 Windows 目录列表拖入右侧的 Linux 目录列表 , 会自动上传文件到指定位置

  ![XFTP_dis](\XFTP_dis.png) 

* 准备工作已经完成了 , 接下来返回 XShell 操作 Linux 系统

--------------------------

### [PS] 另一种下载 MySQL 解压包的方式

* 一般我们使用 Linux 的时候 , 不会都有 FTP 工具 , 那么我们就需要使用一些 Linux 应用来进行下载

* 比如我们会常用 <kbd>wget</kbd> 来进行下载 :

* 当然我们首先要先安装 <kbd>wget</kbd> 才能使用它

  ```shell
  yum install wget
  ```

* 首先创建好我们想要下载解压包的目录 , 并进入此目录 , 执行 wget 命令 , 完成下载后解压包就会显示在 **运行 wget 命令的目录下** 

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ /]cd home
  [root@iZ2vceob6zm3176giqpowfZ home]# ls
  [root@iZ2vceob6zm3176giqpowfZ home]# mkdir test
  [root@iZ2vceob6zm3176giqpowfZ home]# ls
  test
  [root@iZ2vceob6zm3176giqpowfZ home]# cd test
  [root@iZ2vceob6zm3176giqpowfZ test]# wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz
  [root@iZ2vceob6zm3176giqpowfZ test]# ls
  mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz
  ```

---------------------------

### 继续安装 

* 笔者上传的 <kbd>mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz</kbd> 包放在了 <kbd>/home/MySQL</kbd> 目录中

* 个人习惯 , 将解压包和安装包都放在 home 目录中 , 不同软件创建不同的文件夹名称 , 便于识别和记忆

* 在 bash 中进入本目录

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ /]# cd /home/MySQL/
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# ls
  mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz
  ```

* 解压压缩包到当前目录下

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# tar -zxvf mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz 
  ```

* 解压完成之后查看一下当前目录结构

  ```bash
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# ls
  mysql-5.7.34-linux-glibc2.12-x86_64  mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz
  ```

* 可以看到 mysql-5.7.34-linux-glibc2.12-x86_64 是一个目录 , 我们的包文件也还在

  ---------------------------

* **为了防止有所冲突 , 检查一下电脑是否本身就有 MySQL **

### 卸载已有的 MySQL

* 查找是否以前有安装过 mysql

  ```shell
  rpm -qa|grep -i mysql
  ```

* 停止 mysql 服务 , 卸载之前安装的 mysql , 为防止依赖报错 , 添加参数卸载

  ```shell
  rpm -ev 包名 --nodeps
  ```

* 回到 Linux 根目录 , 查找之前老版本的 mysql 文件并删除所有查找到的目录和文件 , 一个一个删除即可

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# whereis mysql
  mysql:
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# whereis mysqld
  mysqld:
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# cd /
  [root@iZ2vceob6zm3176giqpowfZ /]# find / -name mysql
  /home/MySQL/mysql-5.7.34-linux-glibc2.12-x86_64/bin/mysql
  /home/MySQL/mysql-5.7.34-linux-glibc2.12-x86_64/include/mysql
  [root@iZ2vceob6zm3176giqpowfZ /]# find / -name mysqld
  /home/MySQL/mysql-5.7.34-linux-glibc2.12-x86_64/bin/mysqld
  ```

* 会查到刚刚上传上去的文件和刚刚解包的文件 , 不要误伤友军

  ```shell
  whereis mysql
  whereis mysqld
  find / -name mysql
  find / -name mysqld
  ```

* 当输入以上四条命令不再输出目录或文件路径时 , 代表 mysql 已经删干净了 , 接下来开始继续安装 mysql

* [PS] Linux 的删除命令为 <kbd>rm -rf 路径</kbd> , 这一命令会直接删除所指定路径以及其下的所有文件

------------------------------

### 继续安装

* 安装 MySQL 之前需要确保系统中有 libaio 的依赖

  ```shell
  # 搜索依赖
  yum search libaio
  # 安装依赖
  yum install libaio
  ```

* 如果安装过该依赖会提示如下内容

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ /]# yum install libaio
  Last metadata expiration check: 2:06:57 ago on Thu 17 Jun 2021 04:19:25 PM CST.
  Package libaio-0.3.112-1.el8.x86_64 is already installed.
  Dependencies resolved.
  Nothing to do.
  Complete!
  ```

* 为了权限操作 , 我们需要单独创建一个 mysql 用户组 , 并添加 mysql 用户到组中

  ```shell
  #添加用户组
  groupadd mysql
  #添加用户mysql 到用户组mysql(使用-r参数表示mysql用户是一个系统用户，不能登录)
  useradd -r -g mysql mysql
  #添加完用下面命令测试,能看到mysql用户的信息
  id mysql
  ```

* 为了能正常使用 mysql 我们需要将其放到 /usr/ 目录的文件夹下

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ home]# cd /usr
  [root@iZ2vceob6zm3176giqpowfZ usr]# cd local/
  [root@iZ2vceob6zm3176giqpowfZ local]# ls
  aegis  bin  etc  games  include  lib  lib64  libexec  sbin  share  src
  [root@iZ2vceob6zm3176giqpowfZ local]# mkdir MySQL
  [root@iZ2vceob6zm3176giqpowfZ local]# ls
  aegis  bin  etc  games  include  lib  lib64  libexec  MySQL  sbin  share  src
  [root@iZ2vceob6zm3176giqpowfZ local]# cd MySQL
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# 
  ```

* 个人习惯 , 笔者多把此类工具应用放在 /usr/local 目录中的特定文件夹下 ( 例如这里的 MySQL 文件夹 )

* 回到之前解压 MySQL 解压包的路径中 , 复制相关文件到我们创建的 /usr/local/MySQL 文件夹下

  ```shell
  [root@iZ2vceob6zm3176giqpowfZ MySQL]# cd /home/MySQL/mysql-5.7.34-linux-glibc2.12-x86_64/
  [root@iZ2vceob6zm3176giqpowfZ mysql-5.7.34-linux-glibc2.12-x86_64]# ls
  bin  docs  include  lib  LICENSE  man  README  share  support-files
  [root@iZ2vceob6zm3176giqpowfZ mysql-5.7.34-linux-glibc2.12-x86_64]# cp * /usr/local/MySQL/ -r
  [root@iZ2vceob6zm3176giqpowfZ mysql-5.7.34-linux-glibc2.12-x86_64]# ls /usr/local/MySQL/
  bin  docs  include  lib  LICENSE  man  README  share  support-files
  [root@iZ2vceob6zm3176giqpowfZ mysql-5.7.34-linux-glibc2.12-x86_64]# 
  ```

* 接下来我们需要修改 /usr/local/MySQL 目录的权限