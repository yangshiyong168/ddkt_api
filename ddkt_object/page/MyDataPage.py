from selenium.webdriver.common.by import By
from ddkt_object.page.MainPage import MainPage
from ddkt_object.page.HomePage import HomePage
from ddkt_object.page.MyPage import MyPage

class MyDataPage(MainPage):
    _head_picture = (By.ID, "my_profile_head_portrait_ll")  ##头像按钮
    _english_name_button = (By.ID, "my_profile_english_name_ll")  ##英文名按钮
    _sex_button = (By.ID, "my_profile_gender_ll")  ##性别按钮
    _class_name_button = (By.ID, "my_profile_grade_ll")  ##年级按钮

    _name = (By.ID, "my_profile_english_name_tv")  ##英文名称
    _name_old = (By.XPATH, "//*[@text='Alex']") ##旧英文名称
    _name_new = (By.XPATH, "//*[@text='Aaron']") ##新英文名称
    _submit = (By.ID, "tvbtn_forward")  ##提交按钮

    _sex_current = (By.ID, "my_profile_gender_tv")  ##当前性别
    _nan_nv = (By.ID, "item_dialog_common_list_data_tv")  ##男&女
    _sex_cancel = (By.ID, "dialog_common_list_cancel_tv")  ##取消

    _class_name_now = (By.ID, "my_profile_grade_tv")  ##当前年级名称
    _kinder_garten = (By.XPATH, "//*[contains(@text,'中班')]")
    _primary_school = (By.XPATH, "//*[contains(@text,'二年级')]")
    _english_level = (By.ID, "tv_item")  ##英语水平


    def gotoMyData(self):
        self.click(HomePage._my)
        self.click(MyPage._my_name)
        return self


    def reviseName(self) -> tuple:
        self.gotoMyData() ##进入我的资料页面
        name = self.getText(self._name) ##获取当前页面
        self.click(self._name)
        if name == "Aaron":
            self.upSwipeFindElement(self._name_old).click() ##滑动查找英文名
        else:
            self.upSwipeFindElement(self._name_new).click()  ##滑动查找英文名
        self.click(self._submit)
        newName = self.getText(self._name)  ##获取修改后的英文名
        return name, newName

    def reviseSex(self) -> tuple:
        sex = self.getText(self._sex_current)
        self.click(self._sex_button)
        if sex == "男":
            self.finds(self._nan_nv)[1].click()
        else:
            self.finds(self._nan_nv)[0].click()
        sexNew = self.getText(self._sex_current)
        return sex, sexNew

    def reviseClass(self):
        """修改年级"""
        _Class=self.getText(self._class_name_now) ##获取当前的年级
        self.click(self._class_name_button)  ##点击年级按钮
        if _Class=="中班":
            self.click(self._primary_school)
        else:
            self.click(self._kinder_garten)
        self.click(self._english_level)  ##确认
        _ClassNew = self.getText(self._class_name_now)  ##获取修改后的年级
        return _Class,_ClassNew
