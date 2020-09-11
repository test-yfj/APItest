#
import json
import unittest
from common.configHttp import ConfigHttp
import paramunittest
import geturlParams
import readExcel

url = geturlParams.GeturlParams().get_url()
login_xls = readExcel.ReadExcel().get_xls('test.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class TestUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method, code):  # setParameters()中参数与login_xls中key一致
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.code = str(code)

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    def test_case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        new_url = url + self.path  # 系统地址后追加接口路径，如 http://123.56.183.13:8086 + /v1/mds-pc/sys-user/vpn-token
        data = json.loads(self.query)  # 请求参数由字符串类型转换成json类型
        info = ConfigHttp().run_main(self.method, new_url, data)
        s = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == "登录成功":
            self.assertEqual(s['code'], self.code)
        if self.case_name == "账户错误":
            self.assertEqual(s['code'], self.code)
        if self.case_name == "密码错误":
            self.assertEqual(s['code'], self.code)
        if self.case_name == "账号密码为空":
            self.assertEqual(s['code'], self.code)
