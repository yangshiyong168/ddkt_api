from selenium.webdriver.common.by import By

class MyPage(object):
    _quit_login = (By.ID, "settings_logout_tv")  ##退出登录按钮
    _sure_quit = (By.ID, "tv_btn_dialog_commit")  ##退出确认按钮
    _my_name = (By.ID, "tab_mine_user_nick_name_tv") ##我的页面里我的名字

    _my_picture = (By.ID, "tab_mine_user_icon_ivp")  ##个人中心里头像
    _my_task = (By.ID, "tab_mine_task_iv")  ##个人中心里领星星按钮
    _my_surplus_class = (By.ID, "my_account_left_course_tv")  ##个人中心剩余课时
    _course = (By.ID, "tab_mine_course_time_tv")  ##个人中心课时有限期

    _my_course_package = (By.ID, "tab_mine_course_package_tv")  ##个人中心课包数
    _my_star = (By.ID, "tab_mine_star_tv")  ##个人中心星星数
    _my_mine_medal = (By.ID, "tab_mine_medal_tv")  ##个人中心奖状数
    _my_top_ads = (By.ID, "tab_mine_top_ads_iv")  ##个人中心广告位
    _My_class_record = (By.XPATH, "//*[@text='上课记录']") ##个人中心上课记录
    _My_LearningReport = (By.XPATH,"//*[@text='学习报告']") ##个人中心学习报告
    _My_TeacherComments = (By.XPATH,"//*[@text,'老师点评']") ##个人中心老师点评
    _My_PictureReading = (By.XPATH,"//*[@text,'绘本跟读']") ##个人中心绘本跟读
    _My_DubbingShow = (By.XPATH,"//*[@text,'配音秀']") ##个人中心配音秀
    _My_LearningPlan = (By.XPATH,"//*[@text,'学习计划']") ##个人中心学习计划
    _My_ErrorBook = (By.XPATH, "//*[@text,'错题本']")  ##个人中心错题本


