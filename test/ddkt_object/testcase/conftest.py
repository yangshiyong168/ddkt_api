import time,os,sys
import pytest,allure
sys.path.append("C:\\automation")



# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
#
# def pytest_runtest_makereport():
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == 'call' and rep.failed:
#         file_name = os.getcwd() + "\\report\\" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.png'
#         # os.system(r"adb shell screencap -p sdcard/screen.png")
#         # os.system(r"adb pull sdcard/screen.png " + file_name)
#         allure.attach.file(file_name, "失败截图", attachment_type=allure.attachment_type.JPG)
