import os
import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ddkt_object.drivier.Client import AndroidClient
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(AndroidClient):
    driver:webdriver
    def __init__(self):
        """启动driver，实例化一个对象"""
        self.driver = AndroidClient().restart_app()

    def find(self, kv) -> webdriver:
        """查找元素"""
        self.wait(kv)
        return self.driver.find_element(*kv)

    def finds(self, kv) -> webdriver:
        """查找一组元素"""
        self.wait(kv)
        return self.driver.find_elements(*kv)

    def click(self, kv):
        """点击元素"""
        self.find(kv).click()

    def sendKey(self, kv, value):
        """输入框输入信息"""
        self.find(kv).send_keys(value)

    def wait(self,kv):
        """等待元素加载完成，且可见"""
        try:
            WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(kv))
            WebDriverWait(self.driver, 2, 0.1).until(EC.visibility_of_element_located(kv))
        except:
            # print("等待元素出现失败")
            pass

    def quit(self):
        """退出应用程序"""
        self.driver.quit()

    def getText(self, KV) -> str:
        """获取元素的文本"""
        return self.find(KV).text

    def getWinSize(self) -> tuple:
        """ 获取屏幕分辨率"""
        size=self.driver.get_window_size()
        return size["width"],size["height"]

    def upSwipeFindElement(self, kv) -> webdriver:
        """向上滑动查找元素"""
        x, y = self.getWinSize()
        flag=0
        for i in range(10):
            try:
                WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(kv))
                ele=WebDriverWait(self.driver, 1, 0.1).until(EC.visibility_of_element_located(kv))
                flag=1
                return ele
            except:
                self.driver.swipe(x / 2, y / 30 * 25, x / 2, y / 30 * 15, 500)
        if flag==1:
            print("向上滑动10次，没有找到该元素")

    def getToast(self, toast_text) -> str:
        """获取toast"""
        message ='//*[contains(@text,"%s")]'%(toast_text)
        toast_element = WebDriverWait(self.driver,5, 0.1).until(EC.presence_of_element_located((By.XPATH, message)))
        get_text=toast_element.text
        print(get_text)
        return get_text

    def getElementAttribute(self,KV,label):
        """获取元素属性"""
        self.wait(KV)
        element=self.find(KV)
        return element.get_attribute(label)

    def back(self):
        self.driver.back()

    def getScreenshotAsFile(self,filename):
        self.driver.get_screenshot_as_file(filename)

    @staticmethod
    def getImage(function):
        def get_ErrImage(self,*args, **kwargs):
            try:
                function(self,*args, **kwargs)
            except Exception as msg:
                file_name = os.getcwd() + "\\report\\" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.png'
                self.driver.getScreenshotAsFile(file_name)
                allure.attach.file(file_name, "失败截图", attachment_type=allure.attachment_type.JPG)
                raise msg
        return get_ErrImage

