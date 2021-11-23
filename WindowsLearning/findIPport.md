# Windows 10 贴士

------------------------

### 如何查看端口被是否被占用

* 首先查看所有的端口情况

  ```shell
  netstat -ano
  ```

  > 输入此命令会列出所有的端口情况 , 并以 IP:Port 的方式展示出来
  >
  > 首先找到需要检查的端口 , 比如是 8080 , 然后获取最后一列的 PID

* 如果已经知道被占用的端口是哪个了 , 只想获取它而不是检查列表 , 比如 8080

* 那么可以使用此命令

  ```shell
  netstat -ano|findstr "8080"
  ```

  > 这样就能获取 8080 端口对应的单条数据了

* 假如我们获取到 8080 端口对应的占用应用 PID 为 2720

* 那么我们可以通过以下命令查看实际的应用信息

  ```shell
  tasklist|findstr "2720"
  ```

  > 假如结果是 svchost.exe

* 这样我们就可以在任务管理器的进程中关闭它了

* 结束的方式可以直接在任务管理器中结束进程

* 也可以在命令行中输入以下命令结束

  ```shell
  taskkill /f /t /im svchost.exe
  ```

* 另外 , 在任务管理器中可以点击查看看到 PID 的开启选项
