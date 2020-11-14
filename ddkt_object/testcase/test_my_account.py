from ddkt_object.page.MyAccountPage import MyAccountPage
import pytest

class Test_My_Account(object):

    @classmethod
    def setup_class(cls):
        cls.driver = MyAccountPage()
    @classmethod
    def teardown_class(cls):
        pass

    def test_course_hours(self):
        """课时数以及一致性验证"""
        course_my=self.driver.gotoMyAccount()
        tuple = self.driver.classHour()
        print(course_my,tuple[0],tuple[2])
        print(tuple[1],tuple[3])
        assert str(course_my) in tuple[2]
        assert str(tuple[0]) in tuple[2]
        assert tuple[1] == tuple[3]

    def test_goto_course_detailed(self):
        """课时明细页面跳转"""
        self.driver.gotoCourseExplaind()


if __name__ == '__main__':
    pytest.main()