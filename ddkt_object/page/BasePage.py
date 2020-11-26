from selenium.webdriver.common.by import By

from ddkt_object.page.MainPage import MainPage


class BasePage(MainPage):

    ##儿童锁
    _NumOne = (By.ID, "tv_multiplier1")  ##第一个数字
    _NumTow = (By.ID, "tv_multiplier2")  ##第二个数字
    _InputAnswer = (By.ID, "tv_calu_resut")  ##答案输入框


    ##分享好友
    _Friends = (By.XPATH, "//*[@text='杨世勇']")  ##选择要分享的好友
    _Share = (By.XPATH, "//*[@text='分享']")  ##分享按钮
    _WeiXinBack = (By.XPATH, "//*[@text='返回叮咚课堂']")  ##返回叮咚课堂
    ##分享朋友圈
    _Publish = (By.XPATH, "//*[@text='发表']")  ##点击发表按钮

    def openChildrenLock(self):
        """开启儿童锁"""
        answer=int(self.getText(self._NumOne))*int(self.getText(self._NumTow))
        for i in range(1,7):
            _Answer = (By.ID, "tv_answer"+str(i))
            if int(self.getText(_Answer))==answer:
                self.click(_Answer)
                return

    def Share_WeiXin_Friend(self):
        """分享微信好友"""
        self.click(self._Friends)  ##点击好友
        self.click(self._Share)  ##点击分享
        self.click(self._WeiXinBack)  ##点击返回叮咚课堂

    def Share_WeiXin_Friendlink(self):
        """分享微信朋友圈"""
        self.click(self._Publish)  ##点击发表按钮






