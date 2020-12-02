from selenium.webdriver.common.by import By

from ddkt_object.page.MainPage import MainPage


class ClassDetailedPage(MainPage):
    ##课时明细页面
    _SurplusClass = (By.ID, "my_course_time_detail_item_header_total_tv")  ##课时明细的剩余课时
    _CourseTime = (By.ID, "my_course_time_detail_item_header_validity_tv")  ##课时明细的有限期
    _CardExplain_Button = (By.ID, "my_course_time_detail_item_header_help_tv")  ##课时卡说明按钮