import unittest
from common import HTMLTestRunner
import os
import readConfig
import getpathInfo
from common.configEmail import SendEmail
import common.log

send_mail = SendEmail(
    username=readConfig.ReadConfig().get_email("sender"),  # 发件人
    passwd=readConfig.ReadConfig().get_email("password"),  # 密码
    recv=['1028306133@qq.com'],  # 收件人,多个收件人用逗号隔开，如：['1@qq.com', '2@qq.com']
    title='接口自动化测试',  # 标题
    content='三病系统接口测试',  # 正文
    file=os.path.join(getpathInfo.get_path(), "result", "report.html"),  # 附件  report.html
    ssl=True,
)
path = getpathInfo.get_path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
logger = common.log.logger


class AllTest:
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path, "report.html")  # result\report.html
        print(os.path.join(getpathInfo.get_path(), "result", "report.html"))
        self.caseListFile = os.path.join(path, "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
        self.caseList = []

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        """
        fb = open(self.caseListFile, encoding="utf-8")
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以“#”开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为“\n”，去掉每行数据中的"\n"
        fb.close()

    def set_case_suite(self):
        self.set_case_list()  # 拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_modele = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name + ".py")  # 打印取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第二个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + ".py", top_level_dir=None)
            suite_modele.append(discover)  # 将discover存入suite_module元素组
            print("suitr_module:" + str(suite_modele))
        if len(suite_modele) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_modele:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name,使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite  # 返回测试集

    def run(self):
        try:
            suit = self.set_case_suite()  # 获取test_suite
            if suit is not None:  # 判断test_suite是否为空
                logger.info("********** 开始测试ing **********")
                fp = open(resultPath, "wb")  # 打开result/report.html测试报告文件，如果不存在就创建
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='', verbosity=2)
                runner.run(suit)
            else:
                logger.info("没有执行测试.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            # fp.close()
            logger.info("********** 测试结束 **********")
        # 判断邮件发送的开关
        if on_off == "on":
            send_mail.send_email()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


if __name__ == "__main__":
    AllTest().run()
