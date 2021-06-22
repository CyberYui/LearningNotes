# Linux 中安装 Redis

--------------

> 在现阶段的工作中 , 我们越来越不满足于 MySQL 在处理大数据上的卡顿 , 越来越注重高并发 , 多数据源等技术 , 随之开始使用 Redis 等一众内存数据库 , 今天笔者就来演示一下如何在 Linux 云服务器中安装 Redis 数据库
>
> 话不多说 , 从下载开始

* 笔者之前在 MySQL 和 Tomcat 等工具的安装演示中 , 有提到过如何寻找一个软件的压缩版下载链接并通过 wget 下载它 , 这里也使用此方法下载 Redis 解压版包

* 首先进入 Redis 官方下载页面 http://www.redis.cn/download.html

* 在下面获取到 **Redis 6.0.6** 的下载链接 http://download.redis.io/releases/redis-6.0.6.tar.gz

  ![Redis_Linux_Installing](Redis_Linux_Installing.png) 

  > [ps] 不用在乎这个版本是否是 Windows 版本 , 因为 Redis 是一个明确的 , 只专注于提供 Linux 版本的工具 , 当然它也有 Windows 版本 , 但是不是在这里下载的 , 所以我们直接复制这个下载地址即可

* 进入 Linux 系统 , 创建放置解压版包的目录 , 并通过 <kbd>wget</kbd> 命令获取解压版包

* 老习惯了 , 我将它放置在了 <kbd>/home/Redis/</kbd> 目录下

  ```shell
  cd /home/
  # 创建文件夹
  mkdir Redis
  # 检查目录
  ls
  # 可以看到Redis目录创建成功
  Java  MySQL  Nginx  Redis  Tomcat
  # 进入目录下载相关解压版包
  cd Redis
  # 下载目标
  wget http://download.redis.io/releases/redis-6.0.6.tar.gz
  --2021-06-22 17:08:22--  http://download.redis.io/releases/redis-6.0.6.tar.gz
  Resolving download.redis.io (download.redis.io)... 45.60.125.1
  Connecting to download.redis.io (download.redis.io)|45.60.125.1|:80... connected.
  HTTP request sent, awaiting response... 200 OK
  Length: 2228781 (2.1M) [application/octet-stream]
  Saving to: ‘redis-6.0.6.tar.gz’
  redis-6.0.6.tar.gz        100%[==================================>]   2.12M  81.1KB/s    in 24s   
  2021-06-22 17:08:47 (89.9 KB/s) - ‘redis-6.0.6.tar.gz’ saved [2228781/2228781]
  ```

* 接下来解压此文件并将其内容递归复制到 <kbd>/usr/local/redis/</kbd> 目录下 , 没有此目录就创建一个 , 具体咋创建不说啦

  ```
  ```

  

