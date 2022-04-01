'''
业务
思考：
i这个参数如何传递？？？？=>重新__init__方法

'''
import time
import unittest

from page.loginModou import LoginPage

''''
重写__init__：目的就是能传递参数，只是想加一个参数，所以要先继承之前的init方法
然后在进行重写。
'''

class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=0):
        # 继承之前的init方法
        super(ParameTestCase, self).__init__(methodName)
        # 重写自己的init方法
        # 让i变成一个全局的变量
        global i
        i = parame


class MoDouLogin(ParameTestCase):
    login = None
    @classmethod
    def setUpClass(cls) -> object:
        # 实例化page的对象，组合业务逻辑的方法是封装在page里面
        cls.login = LoginPage(i)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.login.quit_driver()

    def test_case_01(self):
        # 调用登录这个业务
        self.login.login_page('19900000001','123456')
        time.sleep(10)
        # 准备开始断言
        self.login.click_my()
        time.sleep(3)
        self.assertIn('赵文文',self.login.get_page_source)