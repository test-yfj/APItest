# 读取Excel的方法
import os
import getpathInfo
from xlrd import open_workbook

path = getpathInfo.get_path()


class ReadExcel:
    def get_xls(self, xls_name, sheet_name):
        cls = []
        xls_path = os.path.join(path, "testFile", "case", xls_name)  # 获取用例文件路径
        file = open_workbook(xls_path)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        nrows = sheet.nrows  # 获取这个sheet内容行数
        for i in range(nrows):  # 根据行数循环
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == "__main__":
    print(ReadExcel().get_xls("test.xlsx", "login"))
    print(ReadExcel().get_xls("test.xlsx", "login")[0][1])
    print(ReadExcel().get_xls("test.xlsx", "login")[1][2])
