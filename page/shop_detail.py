from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ShopDetail(BasePage):
    def shop_photo(self):
        self.steps("../data/shop_detail.yaml", "shop_photo")
        toast = self.find(By.XPATH, "//*[@text='本店探长']")
        return toast.text

    def shop_zhaopaic(self):
        self.steps("../data/shop_detail.yaml", "shop_zhaopaic")
        toast = self.find(By.XPATH, "//*[@text='本店探长']")
        return toast.text

    def shop_vote(self):
        self.steps("../data/shop_detail.yaml", "shop_vote")
        ele1 = self.find(By.XPATH, '//*[@resource-id="com.mstz.xf:id/aLevel"]')
        i = "已投票"
        if i in ele1.text:
            print('已投票')
        else:
            ele1.click()
        toast = self.find(By.XPATH, "//*[@text='本店探长']")
        return toast.text

    def shop_collect(self):
        self.steps("../data/shop_detail.yaml", "shop_collect")
        #self.find(By.ID, "com.mstz.xf:id/collection").click()
        toast = self.find(By.XPATH, "//*[@text='本店探长']")
        return toast.text
