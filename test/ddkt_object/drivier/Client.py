from appium import webdriver

class AndroidClient(object):

    def install_app(self):
        pass
    def restart_app(self) -> webdriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "8BN0218309005299"
        caps["platformVersion"] = 9
        caps["appPackage"] = "com.dd.dingdonglive"
        caps["noReset"] = True
        caps["appActivity"] = "com.dd.dingdonglive.activitys.SplashActivity"
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["chromedriverExecutableDir"] = "D:\\automation\\chromedriver\\74"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(6)
        return self.driver




