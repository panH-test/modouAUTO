from appium import webdriver
#思路：包装了最常用的启动参数
from mobileUtil.write_user_command import WriteUserCommand
import time

class BaseDriver:
    def android_driver(self,i):
        '''
        port, devicename，udid是要动态的读取userconfig.yml里面的数据
        然后填充对应的参数
        :return:
        '''
        #读取userconfug.yml
        write_file = WriteUserCommand()
        devicename = write_file.get_value('user_info_'+str(i),'devicename')
        port = write_file.get_value('user_info_'+str(i),'port')
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        # 必须
        desired_caps['automationName'] = 'Uiautomator1'
        # desired_caps['app'] = r'C:\Users\86133\Downloads\pre4.0.6_12_22_18_39_release.apk'
        # desired_caps['app'] = 'C:\\apk\\modou.apk'
        desired_caps['app'] = r'C:\Users\86133\.PyCharmCE2017.2\modou\data\intest4.1.4_03_15_14_50_release.apk'

        desired_caps['udid'] = devicename
        desired_caps['deviceName'] = devicename
        desired_caps['noSign'] = True
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # desired_caps['autograntExcutable'] = True
        remote = "http://localhost:"+str(port)+"/wd/hub"
        driver = webdriver.Remote(remote, desired_caps)
        time.sleep(10)
        return driver


if __name__ == "__main__":
    driver = BaseDriver().android_driver(0)
    print(driver)
