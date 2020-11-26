from ddkt_object.page.LoginPage import LoginPage
import pytest
from time import sleep

class Test_Login(object):
    """登录模块"""
    @classmethod
    def setup_class(cls):
        cls.driver = LoginPage()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_verify_login(self):
        """验证码正常登录"""
        self.driver.loginVerifyCode(phonenum="14011111331", code='6315')
        assert "我的" in self.driver.getHomeTabText()

    def test_error_verify_login(self):
        """错误的验证码登录"""
        self.driver.loginVerifyCode(phonenum="14011111331", code='1111')
        assert self.driver.getToast('验证码输入错误') is not None
        self.driver.back()

    def test_error_password_login(self):
        """错误密码登录"""
        self.driver.loginPassword(phonenum="14011111331", password='000000')
        assert self.driver.getToast('密码错误') is not None
        self.driver.quitPasswordLogin()

    def test_password_login(self):
        """密码登录"""
        self.driver.loginPassword(phonenum="14011111331", password='123456')
        assert "我的" in self.driver.getHomeTabText()

if __name__ == '__main__':
    pytest.main()
