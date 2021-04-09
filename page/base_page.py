import json
import logging
import time
import yaml
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page.handle_black import handle_black


class BasePage:
    _driver: WebDriver
    _max_err_num = 5
    _error_num = 0
    _params = {}
    _black_list = [
        (By.XPATH, '//*[@text="以后再说"]'),
        (By.ID, 'com.mstz.xf:id/agree'),
        (By.ID, "com.mstz.xf:id/title_back_img"),
        (By.XPATH, '//*[@text="始终允许"]'),
        (By.XPATH, "//*[@text='朕知道了']")
    ]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 保存png文件，path是路径
    def screenshot(self, path):
        self._driver.save_screenshot(path)

    @handle_black
    def find(self, by, locator):
        logging.info("find")
        logging.info(locator)
        if locator is None:
            result = self._driver.find_element(*by)
        else:
            result = self._driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        logging.info("finds")
        logging.info(locator)
        if locator is None:
            result = self._driver.find_elements(*by)

        else:
            result = self._driver.find_elements(by, locator)
        return result

    # 隐式等待方法封装
    def set_implicitly_wait(self, second):
        self._driver.implicitly_wait(second)

    # 下滑x1=x2,y1<y2， 左滑x1>x2, y1=y2, 右滑x1<x2,y1=y2，上滑x1=x2,y1>y2
    def swipe(self, x1, y1, x2, y2):
        size = self._driver.get_window_size()
        # print(size)
        time.sleep(3)
        for i in range(2):
            TouchAction(self._driver) \
                .long_press(x=size['width'] * x1, y=size['height'] * y1) \
                .move_to(x=size['width'] * x2, y=size['height'] * y2) \
                .release() \
                .perform()
        time.sleep(3)

    # 获取yaml文件中的数据，进行相应操作
    def steps(self, path, name):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                # if "len > 0" == action:
                #     eles = self.find(step["by"], step["locator"])
                #     return len(eles) > 0
                # 如果遇到点击搜索键的操作，调用press_keycode(66)方法
                if "press_keycode(66)" == action:
                    self._driver.press_keycode(66)
                # 如果遇到滑动屏幕的操作，调用swipe方法
                if "swipe" == action:
                    self.swipe(step["value1"], step["value2"], step["value3"], step["value4"])
                # 如果遇到等待，调用set_implicitly_wait方法
                if "set_implicitly_wait" == action:
                    self.set_implicitly_wait(step['value'])

