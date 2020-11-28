#coding=utf-8
import  pytest,os,json,allure
from ddkt_api.Public.framework import *

@allure.feature("登录模块")
class Test_Api_Login(object):
    """登录模块接口"""

    @classmethod
    def setup_class(cls):
        cls.head = {"ddversion": ddversion, "ddclient": ddclient}

    @classmethod
    def teardown_class(cls):
        pass

    @allure.story("正确密码正常登录")
    @allure.severity('blocker')
    def test_password_login(self):
        """正确的密码可以正常登录"""
        data = readExcel(filename, "login", 1)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "login", 1)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text
        ddtoken = res.json()["data"]["ddtoken"]
        writExcel(filename, 'token', line=1, row=0, data=ddtoken)  ##将token写入到excel文件中

    @allure.story("错误的密码不能登录")
    @allure.severity('blocker')
    def test_error_password_login(self):
        """错误的密码无法登录"""
        data=readExcel(filename, "login", 2)  ##从excel表格里读取接口的数据
        req_data=encryption(filename, "login", 2)  ##获取需要传输的参数
        res=apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.json().get('msg')

    @allure.story("不输入密码无法登录")
    @allure.severity('blocker')
    def test_not_inpot_password_login(self):
        """不输入密码无法登录"""
        data=readExcel(filename, "login", 3)  ##从excel表格里读取接口的数据
        req_data=encryption(filename, "login", 3)  ##获取需要传输的参数
        res=apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.json().get('msg')

if __name__ == '__main__':
    pytest.main()
    print("chengli")



