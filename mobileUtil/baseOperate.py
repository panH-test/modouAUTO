
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import os
from mobileUtil.logger import GetLogger
logger = GetLogger().get_logger()


'''
# 此脚本主要用于查找元素是否存在，操作页面元素
'''


class OperateElement:
    def __init__(self, driver):
        '''
        复写了driver
        :param driver:
        '''
        self.driver = driver
        logger.info("Init a mobileDriver.")


    # 封装常用的标签
    def get_element(self, css):
        '''
        css 指的就是 xpath=>//android.widget.TextView[@text='我的']
        通过get_value获取的值
        Judge element positioning way, and returns the element.
        xpath=>//android.widget.TextView[@text='我的']
        xpath 定位方式
        //android.widget.TextView[@text='我的'] 表达式
        '''
        element = ''
        ele_type = css.split("=>")[0]
        value = css.split("=>")[1]
        if ele_type == "" or value == "":
            raise NameError("Grammatical errors,reference: 'id=>username'.")

        if ele_type == "id":
            try:
                element = self.driver.find_element_by_id(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "name":
            try:
                element = self.driver.find_element_by_name(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "link":
            try:
                element = self.driver.find_element_by_link_text(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "p_link":
            try:
                element = self.driver.find_element_by_partial_link_text(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "android_uiautomator":
            try:
                element = self.driver.find_element_by_android_uiautomator(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "class":
            try:
                element = self.driver.find_element_by_class_name(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "xpath":
            try:
                element = self.driver.find_element_by_xpath(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        else:
            logger.error("NoSuchElementTypeException: %s" % ele_type)
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element


    # 点击坐标
    def click_coordinate(self, x, y):
        '''
        某个元素被遮挡了
        :param x:
        :param y:
        :return:
        '''
        TouchAction(self.driver).tap(x=x, y=y).perform()
        time.sleep(2)

        logger.info("click coodinate " + x + " " + y)

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        el = self.get_element(css)
        el.click()
        logger.info("click element css")

    # code 事件
    def press_keycode(self, code):
        self.driver.press_keycode(code)
        logger.info("send code:" + code)

    def press_home(self):
        self.driver.press_keycode(3)
        logger.info("press Home button")


    # 单元素滑动
    def swipe_single_element(self,css,n,flag):
        '''
        :param el: 在el元素这个范围进行滑动
        :param n: 滑动的次数
        :param flag: 滑动的方向 1:swipe_up,-1:swipe_down
        :return:
        '''
        # 获取元素的宽高
        el = self.get_element(css)
        el_size = el.size
        el_width = el_size['width']
        el_height = el_size['height']
        # 获取元素的x,y坐标
        el_location = el.location
        el_x = el_location['x']
        el_y = el_location['y']
        swipe_x1 = int((el_x+el_width)*0.9)
        swipe_y1 = el_y
        swipe_y2 = int((el_y+el_height)*0.9)
        if flag == -1:
            print('{}元素开始向下滑动'.format(el))
            for i in range(n):
                self.driver.swipe(swipe_x1,swipe_y1,swipe_x1,swipe_y2)
                time.sleep(1)
        else:
            print('{}元素开始向上滑动'.format(el))
            for i in range(n):
                self.driver.swipe(swipe_x1,swipe_y2,swipe_x1,swipe_y1)
                time.sleep(1)

    # 左滑动
    def swipeToLeft(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        x1 = int(width * 0.75)
        y1 = int(height * 0.5)
        x2 = int(width * 0.05)
        self.driver(x1, y1, x2, y1, 600)
        logger.info("swipeLeft")

    # swipe start_x: 200, start_y: 200, end_x: 200, end_y: 400, duration: 2000 从200滑动到400
    def swipeToDown(self):
        height = self.driver.get_window_size()["height"]
        x1 = int(self.driver.get_window_size()["width"] * 0.5)
        y1 = int(height * 0.25)
        y2 = int(height * 0.75)

        self.driver.swipe(x1, y1, x1, y2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToDown--")
        logger.info("swipeToDown")

    def swipeToUp(self):
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4)
        print("执行上拉")
        logger.info("swipeToUp")
        # for i in range(n):
        #     self.driver.swipe(540, 800, 540, 560, 0)
        #     time.sleep(2)

    def swipeToRight(self):
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        x1 = int(width * 0.05)
        y1 = int(height * 0.5)
        x2 = int(width * 0.75)
        self.driver.swipe(x1, y1, x1, x2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToUp--")
        logger.info("swipeToUp")

    def find_element_with_scroll(self,css,dir="up"):
        """
        按照 dir 的方向滑动，并且找到 feature 这个特征的元素
        :param dir:
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return: 找到的元素
        """
        while True:
            try:
                # 如果找到关于手机，就段点进去
                # driver.find_element_by_xpath("//*[@text='用户']").click()
                return self.get_element(css)
            except:

                # 记录一下滑动之前的page_source
                old_page_source = self.driver.page_source

                if dir == 'up':
                    self.swipeToUp()
                elif dir == 'down':
                    self.swipeToDown()
                elif dir == 'left':
                    self.swipeToLeft()
                else:
                    self.swipeToRight()

                # 判断滑动之后是不是和之前的页面一样
                if old_page_source == self.driver.page_source:
                    raise Exception("到底了！请检查传入的元素的特征")

    def type(self, css, text):
        '''
        Operation input box.

        Usage:
        driver.type("css=>#el","selenium")
        '''
        el = self.get_element(css)
        el.clear()
        el.send_keys(text)
        logger.info(" Input text %s to %s element." % (text, css))

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        logger.info("Gets the value %s of an element attribute %s" % (attribute, css))
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        el = self.get_element(css)
        logger.info("Get element text information.. %s" % css)
        return el.text
    @property
    def page_source(self):
        logger.info("get page_source")
        return self.driver.page_source

    def quit_driver(self):
        self.driver.quit()