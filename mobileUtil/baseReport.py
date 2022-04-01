
from mobileUtil import htmlTestRunner
import os
import time
'''
    生成测试报告，默认存放在Report文件夹下
'''


class Report:
    def __init__(self, title, description):

        self.report_folder = 'report'
        self.title = title
        self.des = description

    '''
        生成测试报告
        :param name:HTML测试报告名称，如login
        :param title:HTML测试报告中展示的标题
    '''
    def start_run(self, suite):
        '''

        :param suite: 套件
        :return:
        '''
        package_path = os.path.abspath("..")
        file_path = os.path.join(package_path, self.report_folder)
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        file_name = file_path +'/'+ self.title + now + ".html"
        print(file_name)
        fp = open(file_name, "wb")
        runner = htmlTestRunner.HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(suite)
        fp.close()

if __name__ == '__main__':
    Report('11','11').start_run(11)