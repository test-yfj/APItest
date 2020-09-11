# 通过get、post、put、delete等方法来进行http请求，并拿到请求响应
import requests
import json


class ConfigHttp:

    def send_post(self, url, data):
        result = requests.post(url=url, json=data).json()  # post()中json属性具体看公司接口参数类型
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, indent=2)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == "post":
            result = self.send_post(url, data)
        elif method == "get":
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result


if __name__ == "__main__":
    result = ConfigHttp().run_main("post", "http://123.56.183.13:8086/v1/mds-pc/sys-user/vpn-token", {"userName": "530000sys", "password": "12345678"})
    print(result)
