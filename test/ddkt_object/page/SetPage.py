from selenium.webdriver.common.by import By

class SetPage(object):
    _setting = (By.XPATH, "//*[contains(@text,'设置')]")
    _quit_login = (By.ID, "settings_logout_tv")  ##退出登录按钮
    _quit_sure = (By.ID, "tv_btn_dialog_commit")  ##退出确认按钮
