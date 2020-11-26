#coding=utf-8
import pytest,os,json,allure,sys
from ddkt_api.Public.framework import *
sys.path.append("C:\\automation")
@allure.feature("约课/上课模块")
class Test_Courses(object):
    """约课/上课模块接口"""

    @classmethod
    def setup_class(cls):
        cls.head = {"ddversion": ddversion, "ddclient": ddclient}
        data = readExcel(filename, "token", 1)
        cls.head["ddtoken"] = data[0]

    @classmethod
    def teardown_class(cls):
        pass

    @allure.story("获取上课列表广告接口")
    @allure.severity('minor')
    def test_get_class_list_ad(self):
        """获取上课列表广告接口"""
        data = readExcel(filename, "yueke_attendClass", 1)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 1)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text

    @allure.story("获取上课列表卡片位数据")
    @allure.severity('blocker')
    def test_get_class_card_list(self):
        """获取上课列表卡片位数据"""
        data = readExcel(filename, "yueke_attendClass", 2)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 2)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text
        try:
            data=json.loads(res.json().get('data').get('data_list')[1].get('img_right_open_protocol').get('open_content')) ##获取数据且将字符串转成json格式

            course_id=data.get("data").get('course_id')
            lesson_id=data.get("data").get('lesson_id')
            category_id = data.get("data").get('category_id')

            fixExcel(filename, 'yueke_attendClass', line=5, row=5, data_1="course_id", data_2='course_id=' + str(course_id))  ##将course_id写入到excel文件中
            fixExcel(filename, 'yueke_attendClass', line=5, row=5, data_1="lesson_id", data_2='lesson_id=' + str(lesson_id))  ##将lesson_id写入到excel文件中
            fixExcel(filename, 'yueke_attendClass', line=5, row=5, data_1="category_id", data_2='category_id=' + str(category_id))  ##将lesson_id写入到excel文件中

            fixExcel(filename, 'yueke_attendClass', line=6, row=5, data_1="course_id", data_2='course_id=' + str(course_id))  ##将course_id写入到excel文件中
            fixExcel(filename, 'yueke_attendClass', line=6, row=5, data_1="lesson_id", data_2='lesson_id=' + str(lesson_id))  ##将lesson_id写入到excel文件中

            fixExcel(filename, 'yueke_attendClass', line=8, row=5, data_1="lession_id", data_2='lession_id=' + str(lesson_id))  ##将lesson_id写入到excel文件中
        except:
            print(res.json().get('data').get('data_list')[1].get('sub_desc'))
            print("该课程不能跳转到课时列表")

    @allure.story("获取上课列表广告接口")
    @allure.severity('minor')
    def test_class_api_01(self):
        """获取上课列表广告接口"""
        data = readExcel(filename, "yueke_attendClass", 3)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 3)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text

    @allure.story("获取上课列表广告接口")
    @allure.severity('minor')
    def test_class_api_02(self):
        """获取上课列表广告接口"""
        data = readExcel(filename, "yueke_attendClass", 4)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 4)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text

    @allure.story("上课/约课页面，课时卡片位跳转到课程列表")
    @allure.severity('blocker')
    def test_class_card_into_courses_list(self):
        """上课/约课页面，课时卡片位跳转到课程列表"""
        data = readExcel(filename, "yueke_attendClass", 5)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 5)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4] , req_data, self.head)  ##发送接口请求
        assert data[6] in res.text

    @allure.story("预约上课拉起时间页面数据")
    @allure.severity('blocker')
    def test_time_page_data(self):
        """预约上课拉起时间页面数据"""
        data = readExcel(filename, "yueke_attendClass", 6)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 6)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text

    @allure.story("获取当前可预约的时间")
    @allure.severity('blocker')
    def test_get_time_list(self):
        """获取当前可预约的时间"""
        data = readExcel(filename, "yueke_attendClass", 7)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 7)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text
        day=res.json().get('data').get('data_list')[0].get('bespeak_date')
        timetable_id=res.json().get('data').get('data_list')[0].get('day_timetable_afternoon')[5].get('timetable_id')

        fixExcel(filename, 'yueke_attendClass', line=8, row=5, data_1="day",
                 data_2='day='+str(day))  ##将course_id写入到excel文件中
        fixExcel(filename, 'yueke_attendClass', line=8, row=5, data_1="timetable_id",
                 data_2='timetable_id='+str(timetable_id))

    @allure.story("预约课程")
    @allure.severity('blocker')
    def test_Appointment_courses(self):
        """预约课程"""
        data = readExcel(filename, "yueke_attendClass", 8)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 8)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text
        bespeak_id=res.json().get('data').get('bespeak_id')
        fixExcel(filename, 'yueke_attendClass', line=9, row=5, data_1="bespeak_id",
                 data_2='bespeak_id='+str(bespeak_id))

    @allure.story("取消预约")
    @allure.severity('blocker')
    def test_cancel_order(self):
        """取消预约"""
        data = readExcel(filename, "yueke_attendClass", 9)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 9)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text

if __name__ == '__main__':
    pytest.main()