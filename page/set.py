import pytest
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Set(BasePage):
    def clear(self):
        self.find(By.ID, "rl_clearCache").click()
        toast=self.find(By.XPATH, "//*[@text='设置']")
        return toast.text

    def xieyi(self):
        self.find(By.ID, 'rl_xieYi').click()
        self.find(By.ID, 'title_back_img').click()
        toast=self.find(By.XPATH, "//*[@text='设置']")
        return toast.text
    def yinsi(self):
        self.find(By.ID, 'rl_yinsi').click()
        self.find(By.ID, 'title_back_img').click()
        toast=self.find(By.XPATH, "//*[@text='设置']")
        return toast.text
    def weixin(self):
        self.find(By.ID, 'rl_bindWeiXin').click()
        toast=self.find(By.XPATH, "//*[@text='设置']")
        return toast.text

    def quite(self):
        self.find(By.XPATH, "//*[@text='退出登录']").click()
        self.find(By.XPATH, "//*[@text='再看看']").click()
        self.find(By.XPATH, "//*[@text='退出登录']").click()
        self.find(By.XPATH, "//*[@text='狠心离开']").click()
        toast=self.find(By.XPATH, "//*[@text='收录店铺']")
        return toast.text

