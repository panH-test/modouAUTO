#@Author:Hanpan
#@Time:2021/12/13  18:12
#@File:runModou.py

# 1.开启appium服务
# 2.运行case: 创建套件，然后添加测试用例，生成测试报告
import time
import unittest
import multiprocessing

from mobileUtil.baseReport import Report
from mobileUtil.server import Server

# 启动appium服务
from mobileUtil.write_user_command import WriteUserCommand
from testSuite.modouLoginSuite import MoDouLogin


def appium_init():
    server = Server()
    # 启动了appium的服务
    server.main()

# 运行测试用例
def runnerCaseApp(i):
    '''

    :return:
    '''
    # 创建suite
    suite = unittest.TestSuite()
    suite.addTest(MoDouLogin('test_case_01', parame=i))
    runner = Report("测试报告", '测试结果')
    runner.start_run(suite)


# todo 现在连了几台设备
def get_count():
    write_file = WriteUserCommand()
    # count就是设备的数量
    count = write_file.get_file_lines()
    return count


if __name__ == '__main__':
    # 启动服务
    appium_init()
    time.sleep(30)
    process_list = []
    for i in range(get_count()):
        p = multiprocessing.Process(target=runnerCaseApp,args=(i,))
        process_list.append(p)
    for j in process_list:
        j.start()