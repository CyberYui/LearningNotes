# docker操作笔记

### 如何将自己正在使用的某个容器推送到dockerhub上

- 首先要将容器保存为镜像

  ```shell
  docker commit container_name newImage_name
  ```

  > 即 docker commit 之后跟上容器名称和新的镜像名称即可

- 创建完成之后可以通过 `docker images -a` 命令查看下

  ```shell
  REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
  cyberql                     latest              d1c75e805ed4        14 hours ago        779 MB
  cyberyui/cyberql            v1                  d1c75e805ed4        14 hours ago        779 MB
  docker.io/whyour/qinglong   latest              2172ff47be69        11 days ago         452 MB
  docker.io/centos            centos7             eeb6ee3f44bd        7 months ago        204 MB
  ```

- 可以看到我这里创建的自己的青龙面板就有了 , 确认无误之后 , 就可以使用此本地镜像创建自己的容器了

- 接下来需要将这个本地镜像推送到 docker hub 上

- 首先确保你有一个 Docker Hub 的账号

- 注册后在控制台输入以下内容登录账号

  ```shell
  docker login -u cyberyui
  Password:
  Login Succeeded
  ```

  > 输密码的时候就和输 Linux 系统密码一样 , 输了不显示

- 当出现 `Login Succeeded` 之后代表登陆成功 , 接下来修改一下镜像的 Repository

- 即上传镜像之前需要通过 docker tag 命令修改镜像的 repositiory , 使之同 Docker Hub 账号匹配

  > 需要注意的是 , 镜像的 registry 中需要包含用户名 , 即 `username/xxx:tag` 这样的命令才行

- 比如我们要将上面的青龙面板上传 , 则是

  ```shell
  docker tag qinglong cyberyui/qinglong:v1
  ```

- 完成后可以通过 `docker images` 看到

- 接下来上传该镜像

  ```shell
  docker push cyberyui/qinglong:v1
  ```

- 如果你已经上传过一次了 , 想上传同一个 repository 中的镜像 , 那么可以省略 tag 部分

- 接下来登录 Docker Hub 官网 , 在你的 repo 中就可以看到这个镜像啦

- 拉取镜像的方法也很简单 , 输入以下命令即可

  ```shell
  # 具体是否要用v1版本请按情况输
  docker push cyberyui/cyberql:v1
  ```
  
- 现在我在用的青龙面板是 2022-04-20 更新的 , 运行在 5700 端口上 , 并且有一个基本的账号密码 ( 自查 )

- 拖到本地之后 , 直接通过 docker 命令运行即可

  ```shell
  [root@VM-4-12-centos ~]# docker pull cyberyui/cyberql:v1
  v1: Pulling from cyberyui/cyberql
  df9b9388f04a: Pull complete 
  62f6113b2624: Pull complete 
  c3f98107bf94: Pull complete 
  db93f8d654ea: Pull complete 
  cf194cf43fd1: Pull complete 
  39ac09d7cbd6: Pull complete 
  b57bae199346: Pull complete 
  Digest: sha256:91f0cbe0bb5fa9e99030a810130cd279f000f525bf4ab902021b22c7e67f0149
  Status: Downloaded newer image for cyberyui/cyberql:v1
  docker.io/cyberyui/cyberql:v1
  [root@VM-4-12-centos ~]# docker images
  REPOSITORY         TAG       IMAGE ID       CREATED        SIZE
  cyberyui/cyberql   v1        d1c75e805ed4   19 hours ago   779MB
  ```

- 可以看到已经拖下来了 , 接下来就是运行了 , 首先通过映射 5700 端口运行 , 然后打开防火墙相应规则即可 , 记得要在服务器的控制台也改一次 ( 这里为了方便查看 , 我把 CREATED 和 STATUS 两个内容删掉了 )

  ```shell
  [root@VM-4-12-centos ~]# docker run -itd -p 5700:5700 cyberyui/cyberql:v1 /bin/bash
  fc97a7e13765d3a02d5cc256b047f5ca687fe895adad87a87554d3dfc25b8024
  [root@VM-4-12-centos ~]# docker ps -a
  CONTAINER ID   IMAGE                 COMMAND                  PORTS					             NAMES
  fc97a7e13765   cyberyui/cyberql:v1   "./docker/docker-ent…"   0.0.0.0:5700->5700/tcp, :::5700->5700/tcp   stupefied_mccarthy
  [root@VM-4-12-centos ~]# firewall-cmd --zone=public --add-port=5700/tcp --permanent
  success
  [root@VM-4-12-centos ~]# firewall-cmd --reload
  success
  [root@VM-4-12-centos ~]# docker ps -a
  CONTAINER ID   IMAGE                 COMMAND                  PORTS						         NAMES
  fc97a7e13765   cyberyui/cyberql:v1   "./docker/docker-ent…"   0.0.0.0:5700->5700/tcp, :::5700->5700/tcp   stupefied_mccarthy
  ```

  