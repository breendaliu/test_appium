import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.mstz.xf"
    _activity = ".ui.SplashActivity"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "test01"
            caps["automationName"] = "uiautomator2"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["newCommandTimeout"] = 6000
            # caps['skipServerInstallation'] = True
            # caps['skipDeviceInitialization'] = True
            # caps["dontStopAppOnReset"] = True
            # 忽略软键盘，直接输入内容
            # caps['unicodeKeyboard'] = True
            # caps['resetKeyboard'] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(20)
        else:
            print(self._driver)
            self._driver.start_activity(self._package, self._activity)

        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()
    #
    def stop(self):
        pass
        self._driver.quit()

    def main(self) -> Main:
        return Main(self._driver)
