# 从零开始 Linux

-----------------------

### 1. 安装

* 首先准备需要的介质 ( U盘 或者 光盘 ) , 系统安装镜像 , 以及一台空闲设备

> 关于 Linux 发行版 : 
>
> 不要让百度指路 , 通过下面的官网去进行系统下载
>
> Fedora的下载官网：[Get Fedora](https://link.zhihu.com/?target=https%3A//getfedora.org/en/)
>
> Ubuntu桌面版的下载官网：[https://ubuntu.com/download/desktop](https://link.zhihu.com/?target=https%3A//ubuntu.com/download/desktop)
>
> CentOS的下载官网：[Download CentOS](https://link.zhihu.com/?target=https%3A//www.centos.org/download/)
>
> Debian的下载官网：[https://www.debian.org/distrib/](https://link.zhihu.com/?target=https%3A//www.debian.org/distrib/)
>
> 甚至是RHEL为开发者准备的官方下载地址：[Red Hat Enterprise Linux Download](https://link.zhihu.com/?target=https%3A//developers.redhat.com/products/rhel/download)

* 但是不推荐使用 RHEL , 因为 RHEL 针对的是提供 bug report/fix 的开发者
* 作为初学者 , 我们使用 Fedora , Ubuntu , CentOS 这些有强大社区支持的 Linux 版本就好
* 这里我选择的是 CentOS7 的版本 , 具体的官方安装镜像存在我的网盘里 , 有需要可以给我发邮箱
* email : YuiNozomi@vip.qq.com

---------------------------

#### 介质制作

-----------------

* 我使用的是 U盘 作为介质
* 创建系统U盘的软件为 rufus , 这是一个开源的 U盘 介质创建程序
* 当有了带有 Linux 的介质之后 , 我们就可以进入安装了
* 整机直接安装即可 , 如果要使用虚拟机推荐使用 VirtualBox
* windows 10 自带一个虚拟机 Hyper-V , 可以通过在微软商店添加不同的 Linux 发行版
* 一般使用 Docker 的话 , 就会用到 Hyper-V

----------------

#### 安装 CentOS

-------------

具体的安装可以参照下面这四个页面

> https://www.zhihu.com/question/272024481
>
> https://www.runoob.com/linux/linux-install.html
>
> https://www.cnblogs.com/yaohong/p/7240387.html
>
> http://www.sa-log.com/276.html

* 即通过安装设置好 语言 , 键盘布局 , 硬盘设置 , 时区 之后 , 就可以进入下一步了
* 一般来说直接安装 Minimal Install 即可安装一个原生的 CentOS 了 , 使用命令行 shell 即可控制系统
* 其他的一些版本会有图形界面 , 但是一般我们用命令行系统即可
* 安装系统并不困难 , 让我们直接快进到使用 Linux 吧 ( 我这里安装的是 CentOS 7 )

----------------

### 2. 使用 Linux

------------------

> 还是以 CentOS 7 为例 , 我们开始进行使用 Linux

* 当我们拿到一台 Linux 主机的时候 , 第一件事必定是给它创建一个静态 ip 地址 , 这样我们在每次重启后 , Linux 主机的 ip 就不会自动分配了 , 否则可能会导致一些不必要的麻烦

* 具体的设定可以查阅这里

  > https://blog.csdn.net/u010521062/article/details/114067036

-------------------------

### yum 的使用

* 在 CentOS 7 的级精简版中 , 你都可以使用 yum 进行安装软件操作

* 常用的指令有 :

  ```shell
  # yum 针对软件包操作常用命令
  # 使用 yum 查找软件包
  yum search 软件包名
  # 列出所有可安装的软件包
  yum list
  # 列出所有可更新的软件包
  yum list updates
  # 列出所有已安装的软件包
  yum list installed
  # 列出所有已安装但不在 Yum Repository 内的软件包
  yum list extras
  # 列出所指定的软件包
  yum list 软件包名
  # 使用YUM获取软件包信息
  yum info 软件包名
  # 列出所有软件包的信息
  yum info
  # 列出所有可更新的软件包信息
  yum info updates
  # 列出所有已安装的软件包信息
  yum info installed
  # 列出所有已安装但不在 Yum Repository 内的软件包信息
  yum info extras
  # 列出软件包提供哪些文件
  yum provides 软件包名
  ```

  

------------------------

## 我遇到的问题

### 云服务器被攻击

- 有时候会突然收到短信表示云服务器被某个特定IP登录或者爆破密码了 , 这种时候可以通过以下方法阻止一个网段的 IP 访问云服务器

- 优先级为先检查 <kbd>/etc/hosts.deny</kbd> , 再检查 <kbd>hosts.allow</kbd> , 后者设定可越过前者限制

  > 例如：  
  >
  > 1.**限制所有的ssh**
  >
  > 除非从216.64.87.0 - 127上来。  
  >
  > hosts.deny文件添加 : 
  >
  > in.sshd:ALL
  >
  > hosts.allow文件添加 : 
  >
  > in.sshd:216.64.87.0/255.255.255.128 
  >
  >   
  >
  > 2.**封掉216.64.87.0 - 127的telnet** 连接  
  >
  > hosts.deny文件添加 : 
  >
  > in.sshd:216.64.87.0/255.255.255.128 
  >
  >  
  >
  > 3.**限制所有人的TCP连接 , 除非从216.64.87.0 - 127访问**  
  >
  > hosts.deny文件添加 :
  >
  > ALL:ALL  
  >
  > hosts.allow文件添加 : 
  >
  > ALL:216.64.87.0/255.255.255.128 
  >
  >  
  >
  > 4.**限制216.64.87.0 - 127对所有服务的访问**
  >
  > hosts.deny文件添加 : 
  >
  > ALL:216.64.87.0/255.255.255.128 
  >
  >  
  >
  > 其中冒号前面是TCP daemon的服务进程名称，通常系统  
  >
  > 进程在/etc/inetd.conf中指定 , 比如 in.ftpd , in.telnetd , in.sshd  
  >
  >   
  >
  > 其中IP地址范围的写法有若干中，主要的三种是：  
  >
  > 1.**网络地址--子网掩码** 方式：  
  >
  > 216.64.87.0/255.255.255.0 
  >
  > 2.**网段方式**
  >
  > 216.64.\*.\* , 即以216.64打头的网段IP地址
  >
  > 3.**缩略子网掩码方式** , 既数一数二进制子网掩码前面有多少个“1”比如：  
  >
  > 216.64.87.0/255.255.255.0 -- 216.64.87.0/24
