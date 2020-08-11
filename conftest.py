import time,os
import pytest,allure

# def pytest_sessionstart(session):
#     session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():

    outcome = yield
    rep = outcome.get_result()

    def adb_screen_shot():
        file_name = os.getcwd() + "\\report\\" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.png'
        os.system(r"adb shell screencap -p sdcard/screen.png")
        os.system(r"adb pull sdcard/screen.png " + file_name)
        return file_name

    if rep.when == 'call':
        if rep.passed:
            return
        if rep.failed:
            pic_path = adb_screen_shot()
            allure.attach.file(pic_path, "失败截图", attachment_type=allure.attachment_type.JPG)
