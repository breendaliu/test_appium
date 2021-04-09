from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestMstzContent:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test02"
        # caps["automationName"] = "uiautomator2"
        caps["appPackage"] = "com.mstz.xf"
        caps["appActivity"] = ".ui.SplashActivity"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)
        self.driver.find_element(MobileBy.ID, 'com.mstz.xf:id/photo').click()

    def test_content(self):
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/center").click()
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/right_img").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='意见反馈']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='其他问题']").click()
        # self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/submit").click()
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/etContent").send_keys("测试一下的啊啊啊啊阿")
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/tv_expand_remain_mask").click()
        photo = (MobileBy.XPATH, "//*[@class='android.widget.RelativeLayout' and @index='2']")
        self.driver.find_element(*photo).click()
        self.driver.find_element(MobileBy.ID, 'com.mstz.xf:id/hvp_photo_picker_preview_content').click()
        photo1=(MobileBy.XPATH, "//*[@text='选择' and contains(@resource-id,'com.mstz.xf:id/tv_photo_picker_preview_choose')]")
        self.driver.find_element(*photo1).click()
        photo2=(MobileBy.XPATH, "//*[@resource-id='com.mstz.xf:id/tv_photo_picker_preview_submit' and contains(@text,'确定')]")
        self.driver.find_element(*photo2).click()
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/submit").click()

    def test_right(self):
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/center").click()
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/right_img").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='意见反馈']").click()
        self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/right_tv").click()
        right=self.driver.find_element(MobileBy.ID, "com.mstz.xf:id/tv_title_title")
        assert "我的反馈" in right.text


