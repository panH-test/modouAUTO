'''
需要从外部去导入模块，而不是继承的
'''
import time

from mobileUtil.baseOperate import OperateElement
from mobileUtil.baseDriver import BaseDriver
from mobileUtil.inihelper import IniHelper


class LoginPage:
    # 获取登录页面的所有页面元素信息
    def __init__(self, i):
        # 实例化operateElement self.driver 随便取的名字，叫什么都行
        self.driver = OperateElement(BaseDriver().android_driver(i))
        self.source = IniHelper()

    #同意墨斗授权
    def click_positive(self):
        self.driver.click(self.source.get_value('modouPage.ini','Button','首次同意'))
        time.sleep(3)

    #同意华为媒体权限
    def click_huaweiAllow(self):
        self.driver.click(self.source.get_value('modouPage.ini','Button','华为媒体权限同意'))
        time.sleep(3)

    #同意小米媒体权限
    def click_xiaomiallow(self):
        self.driver.click(self.source.get_value('modouPage.ini','Button','小米媒体权限同意'))
        time.sleep(3)


    #点击我的
    def click_my(self):
        self.driver.click(self.source.get_value('modouPage.ini','Button','我的'))
        time.sleep(3)

    #点击请点击登录
    def click_clklogin(self):
        self.driver.click(self.source.get_value('modouPage.ini','Button','点击登录'))
        time.sleep(10)


    # 输入账号
    def input_username(self,username):
        self.driver.type(self.source.get_value('modouPage.ini','TextInput','账号'),username)
        time.sleep(3)

    # 输入验证码
    def input_password(self, password):
        self.driver.type(self.source.get_value('modouPage.ini', 'TextInput', '验证码'), password)
        time.sleep(3)

    # 勾选协议
    def click_agree(self):
        self.driver.type(self.source.get_value('modouPage.ini','Button','同意协议'))
        time.sleep(3)

    # 点击登录
    def click_login_button(self):
        self.driver.click(self.source.get_value('modouPage.ini', 'Button', '登录按钮'))
        time.sleep(3)

    # 为了断言  点击我的
    #def click_me(self):
     #   self.driver.click(self.source.get_value('doubanPage.ini', 'Button', '我的'))
      #  time.sleep(3)

    # 获取page_source

    @property
    def get_page_source(self):
        return self.driver.page_source
    # 退出
    def quit_driver(self):
        self.driver.quit_driver()


    # 组合业务方法
    def login_page(self,username,password):

        self.click_positive()
        # self.click_xiaomiallow()
        self.click_huaweiAllow()
        self.click_my()
        self.click_clklogin()
        self.input_username(username)
        self.input_password(password)
        self.click_agree()
        self.click_login_button()
        self.quit_driver()

