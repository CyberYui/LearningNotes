# MySQL 的安装 ( msi 以及 zip) - for Windows

-----------------

## msi 版本安装

### 下载

* 进入以下页面下载 MySQL 数据库

* https://dev.mysql.com/downloads/installer/

  > 一般来说我们下载的是最新版或者是 5.7 的版本 , 所以下载这两个版本的数据库即可
  >
  > ![MySQL_Download_msi](\MySQL_Download_msi.png)
  >
  > <font color="#f863c8">**图片上是 8.0.25 版本的下载 , 我们还需要下一个 5.7 版本的 MySQL**</font>
  >
  > [PS] 下载的时候可能需要使用 VPN 等工具 , 下载页面会提示登录 , 选择左下角的 <font color="#b1e1d2">No thanks , just start my download</font>即可正常下载了

### 安装

* 当我们下载完成之后 , 会获得一个将近 300MB~500MB 的 msi 文件 , 请注意如果你的安装包很小的话在你配置完安装路径之后会自动下载安装包 , 如果你的网络连接外网还是有些小问题的话 , 尽量不要使用这种方式 , 最好去找一个 msi 安装包
* 双击 msi 文件打开安装程序 , 比如我这里的是 <kbd>mysql-installer-community-8.0.25.0.msi</kbd> 
* 

--------------

## zip 版本安装

----------------------------

> 因为我最常用的就是这个版本 , 所以从这个版本开始说起

### 下载

* 进入以下页面下载 MySQL 数据库

* https://dev.mysql.com/downloads/mysql/

  > 一般来说我们下载的是最新版或者是 5.7 的版本 , 所以下载这两个版本的数据库即可
  >
  > ![MySQL_Download](\MySQL_Download.png)
  >
  > <font color="#f863c8">**图片上是 8.0.25 版本的下载 , 我们还需要下一个 5.7 版本的 MySQL**</font>
  >
  > [PS] 下载的时候可能需要使用 VPN 等工具 , 下载页面会提示登录 , 选择左下角的 <font color="#b1e1d2">No thanks , just start my download</font>即可正常下载了

### 安装

* 当我们下载完成之后 , 会获得一个 zip 压缩包 , 使用解压工具将其解压到你想存放数据库的目录即可

* 比如我这里下载的是 <kbd>mysql-5.7.34-winx64.zip</kbd>

* [PS] 解压工具请自行寻找 , WINRAR , Bandizip , 7-zip 都是可以的

* 事实上解压之后你就可以开始使用数据库了 , 但是为了方便使用 , 我们需要配置一下它

  > 就像我们使用 java 一样 , 我们也需要给 MySQL 添加一个环境变量从而能够实现这种方式开启数据库 , 打开控制台而不需要再进入 MySQL 目录就可以直接访问数据库

* 我的 windows 10 版本为 20H2 , 不同 windows 版本配置是差不多的

* 逐级进入 鼠标右键计算机→属性→高级系统设置→环境变量

* 在变量 Path 上双击并添加以下内容 , 我的路径是这样 , 根据自己路径调整即可

* 建议像我这样设置 , 添加一个主目录 MySQL , 方便我们之后的双 MySQL 数据库安装

* ```bash
  F:\MySQL\mysql-5.7.34-winx64\bin;
  ```

* 配置完成之后就可以通过控制台 ( cmd ) 直接运行 mysql 了 , 但是先别急 , 还需要配置一下数据库的默认配置 , 以及数据库的存放位置

* 如果你之前用过 MySQL , 那么你一定知道有一个 <kbd>mysql.ini</kbd> 文件需要进行设置 , 但是 zip 版数据库可能没有这个文件 , 不用担心 , 自己创建一个就可以了

  ---------------------

  #### 开始配置

  * 首先进入你解压好的 mysql 数据库目录 , 它看起来会像是这样的 <kbd>mysql-5.7.34-winx64</kbd>

  * 创建一个 data 文件夹 , 创建一个 mysql.ini 文件

    [PS] mysql.ini 文件需要你首先新建一个笔记本文件 (.txt) 然后手动更改它的后缀和文件名

  * 修改前后的目录对比应该差不多是这样的

    ![MySQL_zip_Install](\MySQLzipInstall.png)

  * **data** 目录会在之后存放我们的数据库 , mysql 在读取配置文件的相关配置之后就会知道这个目录在哪啦

  * **my.ini** 文件就是我们需要的配置文件啦 , 首先打开 my.ini 文件 , 设定其内容如下

    ```ini
    [mysql]
    # 设置mysql客户端默认字符集
    default-character-set=utf8 
    
    [mysqld]
    #设置数据库启动在3306端口
    port = 3306 
    
    # 设置mysql的安装目录
    basedir=F:\MySQL\mysql-5.7.34-winx64
    
    # 设置mysql数据库的数据的存放目录
    datadir=F:\MySQL\mysql-5.7.34-winx64\data
    
    # 允许最大连接数
    max_connections=200
    
    # 服务端使用的字符集默认为8比特编码的latin1字符集
    character-set-server=utf8
    
    # 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    
    # 设置数据库的模式用于生产开发环境,防止非法数据插入
    # STRICT_TRANS_TABLES : 在该模式下,如果一个值不能插入到一个事务表中,则中断当前的操作,对非事务表不做限制
    # NO_ENGINE_SUBSTITUTION : 如果需要的存储引擎被禁用或未编译,那么抛出错误。不设置此值时,用默认的存储引擎替代,并抛出一个异常
    sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
    
    # mysql 中有这样的一个默认行为:
    # 当一行数据中某些列被更新时,如果这一行中有timestamp类型的值
    # 那么这个timestamp列的数据也会被自动更新到更新操作所发生的那个时间点
    # 这个操作是由explicit_defaults_for_timestamp 控制的
    explicit_defaults_for_timestamp=1
    ```

  * [PS] 关于数据库的模式 sql_mode 的相关内容参照下面这个链接

  * https://developer.aliyun.com/article/710525
  
  * 数据库的存放地点和配置我们都调好了 , 接下来就让 mysql 按照我们的配置初始化一下即可

  * [PS] 你的电脑可能还需要一些必须的运行库才能执行以下命令

    > 如果在使用命令的时候电脑报错了 , 记得去搜索这个错误查找解决方法
  
  * 以管理员身份打开控制台 , 输入以下命令 , 让 mysql 通过我们的配置文件自行安装 , 并产生一个名叫 MySQL 的 windows 服务

  * 一般直接输入这样的命令即可

    ```sql
    mysqld install
    ```

  * 有时候我们需要在开始安装的时候就使用我们的配置文件 , 那么会用这样的命令
  
    ```sql
    mysqld install MySQL --default-file="F:\MySQL\mysql-5.7.34-winx64\my.ini"
    ```

  * 有时候可能直接使用上面这句命令更管用
  
  * 成功安装之后控制台会有提示

    ```powershell
    Service successfully installed
    ```

  * 安装成功后就可以初始化数据库了 , 否则是无法启动服务的
  
  * 有可能此时你已经能够启动服务 , 那是因为你已经创建好了 **data** 目录 , 实际上 , 当你的文件夹中没有 **data** 目录时 , 在执行 <kbd>mysqld --initialize</kbd> 操作时 mysql 会自动创建 **data** 目录
  
  * 一般来说 , 这一步我们需要进入 mysql 的 bin 目录执行以下命令
  
    ```powershell
    F:\MySQL\mysql-5.7.34-winx64\bin>mysqld --initialize-insecure
    ```
  
  * 但是由于我们事先配置了环境变量 , 所以现在我们就可以直接执行下面的命令了
  
    ```powershell
    C:\Users\Administrator>mysqld --initialize-insecure
    ```
  
  * **-insecure** 命令的作用是创建 mysql 的 root 用户时不创建密码 , mysql 应该会向你提示这个警告
  
  * 如果事先没有创建 **data** 目录 , 你可能会看到这样的错误
  
    ```bash
    mysqld: Can't change dir to 'F:\MySQL\mysql-5.7.34-winx64\data\' (Errcode: 2 - No such file or directory)
    2021-06-16T10:11:07.073465Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
    2021-06-16T10:11:07.073528Z 0 [Warning] 'NO_ZERO_DATE', 'NO_ZERO_IN_DATE' and 'ERROR_FOR_DIVISION_BY_ZERO' sql modes should be used with strict mode. They will be merged with strict mode in a future release.
    2021-06-16T10:11:07.073531Z 0 [Warning] 'NO_AUTO_CREATE_USER' sql mode was not set.
    2021-06-16T10:11:07.073551Z 0 [Note] --secure-file-priv is set to NULL. Operations related to importing and exporting data are disabled
    2021-06-16T10:11:07.074484Z 0 [Note] mysqld (mysqld 5.7.34) starting as process 5348 ...
    2021-06-16T10:11:07.079686Z 0 [Warning] Can't create test file F:\MySQL\mysql-5.7.34-winx64\data\DESKTOP-S2QLF38.lower-test
    2021-06-16T10:11:07.079956Z 0 [Warning] Can't create test file F:\MySQL\mysql-5.7.34-winx64\data\DESKTOP-S2QLF38.lower-test
    2021-06-16T10:11:07.081526Z 0 [ERROR] failed to set datadir to F:\MySQL\mysql-5.7.34-winx64\data\
    2021-06-16T10:11:07.082564Z 0 [ERROR] Aborting
    
    2021-06-16T10:11:07.083277Z 0 [Note] Binlog end
    2021-06-16T10:11:07.084010Z 0 [Note] mysqld: Shutdown complete
    ```
  
  * 不用担心 , 把 **data** 目录创建一下就行了 , 也别管是否会自动生成 **data** 目录了
  
  * 初始化成功后 , 命令行会没有任何提示
  
  * 但检查我们的数据库目录 , 文件夹中已经自动生成了 **data** 目录
  
  * 接下来执行以下命令 , 开启我们刚刚创建的 MySQL 服务
  
    ```powershell
    C:\Users\Administrator>net start mysql
    MySQL 服务正在启动 ....
    MySQL 服务已经启动成功。
    ```
  
  * [PS] 在这里可能还会遇到一些问题 , 比如出现这样的结果
  
  * ```powershell
    MySQL 服务正在启动 .
    MySQL 服务无法启动。
    
    服务没有报告任何错误。
    
    请键入 NET HELPMSG 3534 以获得更多的帮助。
    ```
  
  * 这种问题的原因是我们刚刚使用了自己的配置文件安装了 mysql 服务 , 但是 windows 自己设定的注册信息不对
  
  * <kbd>WIN+R</kbd> 输入 regedit 进入注册表
  
  * 定位 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL
  
  * 修改 <kbd>ImagePath</kbd> 的内容为类似以下内容 , 保存注册表并退出
  
  * ```sql
    F:\MySQL\mysql-5.7.34-winx64\bin\mysqld MySQL
    ```
  
  * 到这里的时候记得检查以下你的 **data** 目录下是否有东西 , 如果里面有内容的话记得删除 ,否则会报如下错误
  
  * ```bash
    F:\MySQL\mysql-5.7.34-winx64\bin>mysqld --initialize
    2021-06-16T10:30:35.060528Z 0 [Warning] 'NO_ZERO_DATE', 'NO_ZERO_IN_DATE' and 'ERROR_FOR_DIVISION_BY_ZERO' sql modes should be used with strict mode. They will be merged with strict mode in a future release.
    2021-06-16T10:30:35.060580Z 0 [Warning] 'NO_AUTO_CREATE_USER' sql mode was not set.
    2021-06-16T10:30:35.062612Z 0 [ERROR] --initialize specified but the data directory has files in it. Aborting.
    2021-06-16T10:30:35.063722Z 0 [ERROR] Aborting
    ```
  
  * 至此应该基本问题都解决了 , 下面再使用 <kbd>net start mysql</kbd> 命令启动数据库 , 应该就成功了的
  
  * 接下来进入数据库 , 首次进入数据库应该是没有密码的 , 输入密码阶段直接回车继续即可
  
    ```powershell
    C:\Users\Administrator>mysql -u root -p
    ```
  
  * 至此 , 我们的解压版 MySQL 已经安装成功了
  
  * 可以使用命令行或者数据库可视化链接软件 ( 如 Navicat ) 链接数据库了
  
  * 使用 zip 解压版 mysql 的好处是 , 当你想删除 MySQL 的时候 , 只需要进行如下操作
  
    1. 停止 MySQL 服务 , 并删除服务
  
       ```powershell
       C:\Windows\system32>net stop MySQL
       MySQL 服务正在停止.
       MySQL 服务已成功停止。
       C:\Windows\system32>sc delete MySQL
       [SC] DeleteService 成功
       ```
  
    2. 删除配置的 MySQL 环境变量
  
       逐级进入 鼠标右键计算机→属性→高级系统设置→环境变量
  
       删除之前在 Path 变量中配置的 MySQL 内容
  
       ```powershell
       F:\MySQL\mysql-5.7.34-winx64\bin;
       ```
  
    3. 删除 MySQL 目录 , 即你的数据库解压目录以及其中的所有文件
  
       ```powershell
       F:\MySQL\mysql-5.7.34-winx64
       ```
  
  * 至此 , 一次完整的 MySQL 下载 , 安装 和 删除 就完成了
  
  

