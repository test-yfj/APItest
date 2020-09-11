# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
import requests

url = "http://123.56.183.13:8086/v1/mds-pc/sys-user/vpn-token"
data = {"userName": "", "password": ""}
res = requests.post(url, json=data)
print(res.text)
