from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Content(BasePage):
    def content_all(self,content):
        self._params['content'] = content
        self.steps("../data/content.yaml", "content_all")
        toast=self.find(By.XPATH, "//*[@text='设置']")
        return toast.text
    def content_no_group(self,content):
        self._params["content"] = content
        self.steps("../data/content.yaml", "content_no_group")
        toast=self.find(By.XPATH, "//*[@resource-id,'right_tv' and @text='查看反馈']")
        return toast.text
