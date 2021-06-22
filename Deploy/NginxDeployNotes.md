# 通过域名直接访问部署在 nginx 下的工程

----------------------





### Nginx 隐藏端口号

-------

* 给指定的项目配置以下内容

  ```shell
  server {  
  	listen      80;  
  	server_name localhost;  
  	proxy_set_header Host $host:$server_port;  
  	proxy_set_header X-Real-IP $remote_addr;  
  	proxy_set_header REMOTE-HOST $remote_addr;  
  	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
  	location / {  
  		proxy_pass http://127.0.0.1:8080/;  
         }  
     }  
  ```

  > proxy_set_header Host $host : $server_port;  
  >
  > 这段比较关键之前我没加$server_port就老是到下级请求出现真实端口号
