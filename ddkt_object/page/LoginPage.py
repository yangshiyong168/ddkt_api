from selenium.webdriver.common.by import By
from ddkt_object.page.MainPage import MainPage
from ddkt_object.page.HomePage import HomePage
from ddkt_object.page.SetPage import SetPage

class LoginPage(MainPage):

    _phone_number = (By.ID, "edt_phone")  ##手机号码输入框
    _next = (By.ID, "tvbtn_forward")  ##下一步
    _input_code = (By.CLASS_NAME, "android.widget.EditText")  ##输入验证码

    _login_password = (By.ID, "tvbtn_code_pwd_login")  ##密码登录按钮
    _login_verify_code = (By.ID, "tvbtn_code_pwd_login")  ##验证码登录按钮
    _password_input = (By.ID, "edt_pwd")  ##密码输入框
    _login_now=(By.ID, "tvbtn_forward") ##密码登录--立即登录按钮
    _forget_password = (By.ID, "tvbtn_forget_pw")  ##忘记密码

    _NewPasswordNext_1 = (By.ID, "edt_pwd")  ##新密码1
    _NewPasswordNext_2 = (By.ID, "edt_pwd_again")  ##新密码再次输入
    _Over = (By.ID, "tvbtn_forward")  ##新密码设置完成按钮

    _WeiXinlogin=(By.XPATH, "//*[contains(@text,'微信登录')]")  ##微信登录
    _WeiXinSurelogin = (By.XPATH, "//*[contains(@text,'确认登录')]")  ##点击确认登录


    def loginVerifyCode(self, phonenum, code):
        """验证码登录"""
        try:
            self.quitLogin()
        except:
            pass
        self.sendKey(self._phone_number, phonenum) ##输入手机号码
        self.click(self._next)  ##点击下一步
        self.sendKey(self._input_code, code) ##输入验证码

    def loginPassword(self, phonenum, password):
        """密码登录"""
        try:
            self.quitLogin()
        except:
            pass
        self.click(self._login_password)
        self.sendKey(self._phone_number, phonenum)
        self.sendKey(self._password_input, password)
        self.click(self._login_now)

    def quitLogin(self):
        """退出登录"""
        self.click(HomePage._my) ##点击我的按钮
        self.upSwipeFindElement(SetPage._setting).click()  ##滑动点击设置按钮
        self.upSwipeFindElement(SetPage._quit_login).click()##滑动点击退出登录按钮
        self.click(SetPage._quit_sure) ##点击确认按钮

    def getHomeTabText(self) -> str:
        """获取首页tab的文本"""
        return self.getText(HomePage._my)   ##获取首页推荐按钮文本
    def quitPasswordLogin(self):
        """退出密码登录页面"""
        self.click(self._login_password)






