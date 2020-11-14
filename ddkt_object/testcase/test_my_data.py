from ddkt_object.page import MainPage
from ddkt_object.page.MyDataPage import MyDataPage
import pytest

class Test_My_Data(object):

    @classmethod
    def setup_class(cls):
        cls.driver=MyDataPage()
        return cls.driver

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # @MyDataPage.getImage
    def test_revise_name(self):
        name,nameNew = self.driver.reviseName()
        print(name,nameNew)
        assert name == nameNew

    @MyDataPage.getImage
    def test_revise_sex(self):
        sex,sexNew = self.driver.reviseSex()
        print(sex,sexNew)
        assert sex != sexNew

    @MyDataPage.getImage
    def test_revise_class(self):
        className,classNew = self.driver.reviseClass()
        print(className,classNew)
        assert className == classNew

if __name__ == '__main__':
    pytest.main()
