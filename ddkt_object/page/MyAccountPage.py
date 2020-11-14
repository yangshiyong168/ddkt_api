import os,time
from time import sleep
from selenium.webdriver.common.by import By
from ddkt_object.page.ClassDetailedPage import ClassDetailedPage
from ddkt_object.page.HomePage import *
from ddkt_object.page.MyPage import *
from ddkt_object.page.MainPage import MainPage
from ddkt_object.page.BasePage import BasePage

class MyAccountPage(BasePage):

    ##我的账户页面
    _SurplusClass = (By.ID, "my_account_left_course_tv")  ##剩余课时
    _CourseTime = (By.ID, "my_account_deadline_tv")  ##课程有限期
    _Scholarship = (By.ID, "my_account_scholarship_tv")  ##奖学金数量
    _SurplusDingDongBi = (By.ID, "my_account_dd_coin_tv")  ##剩余叮咚币数量
    _BuyHistory = (By.ID, "my_account_course_buy_record_tv")  ##购买记录
    _ClassPackage = (By.ID, "my_account_course_package_rv")  ##课包

    ##叮咚币页面
    _DingDong_SurplusDingDongBi = (By.ID, "my_dd_coin_left_tv")  ##剩余叮咚币
    _RechargeRecord_Button = (By.ID, "my_dd_coin_pay_record_tv")  ##充值记录按钮
    _RechargeAmount = (By.XPATH,"//*[@text='¥1398']") ## 充值数量按钮
    _SureRecharge_Button = (By.ID,"my_dd_coin_pay_btn") ##确认充值按钮

    ##购买记录页面
    _View_Course = (By.ID, "item_payment_record_detail_tv")  ##查看课程按钮

    def gotoMyAccount(self):
        """进入我的账户页面"""
        self.click(HomePage._my)
        courseMy = self.getText(MyPage._course)  ##获取个人中心课时数
        self.click(MyPage._course)  ##点击进入我的账号页面
        self.openChildrenLock()  ##儿童锁解锁
        return courseMy

    def classHour(self) -> tuple:
        """获取课时数，校验正确性"""
        Course_MyAccount = self.getText(self._SurplusClass) ##获取我的账户里面剩余课时数量
        CourseTime_MyAccount = self.getText(self._CourseTime)  ##获取我的账户里面课时有限期
        self.click(self._SurplusClass) ##点击进入课时明细页面
        Course_ClassDetailed=self.getText(ClassDetailedPage._SurplusClass)  ##获取课时明细里面的剩余课时数
        CourseTime_ClassDetailed = self.getText(ClassDetailedPage._CourseTime)  ##获取课时明细里面课时有限期
        return Course_MyAccount,CourseTime_MyAccount,Course_ClassDetailed,CourseTime_ClassDetailed

    def gotoCourseExplaind(self):
        """进入课时卡说明页面，且截图"""
        self.click(ClassDetailedPage._CardExplain_Button)  ##点击进入课时卡说明
        file_name = os.getcwd() + "\\report\\" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.png'
        os.system(r"adb shell screencap -p sdcard/screen.png")
        os.system(r"adb pull sdcard/screen.png " + file_name)
        self.back() ##点击返回键
        time.sleep(1)
        self.back() ##点击返回键

    def gotoPuyRecord(self):
        """进入购买记录页面，且点击查看课程"""
        #todo 购买流程
        pass

    def gotoCourseBag(self):
        """进入我的课包里面的第一个课包"""
        #todo 进入课包流程
        pass