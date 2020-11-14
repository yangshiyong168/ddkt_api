from selenium.webdriver.common.by import By


class HomePage(object):

    _first_page = (By.XPATH, "//*[@text='首页']")  ##主页面首页按钮
    _find = (By.XPATH, "//*[@text='发现']")  ##主页面发现按钮
    _appointment_courses = (By.XPATH, "//*[@text='约课']")  ##主页面约课按钮
    _my = (By.XPATH, "//*[@text='我的']")  ##主页面我的按钮
