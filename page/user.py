from selenium.webdriver.common.by import By
from page.base_page import BasePage


class User(BasePage):
    # 进入消息页面
    def goto_usermessage(self):
        # self.find(By.XPATH, "//*[@text='消息']").click()
        # self.swipe(x1,y1,x2,y2)
        # self.find(By.XPATH, "//*[contains(@resource-id,'recyclerView')]/android.widget.RelativeLayout[4]//*[@text='系统消息：']").click()
        # self._params["x1"] = x1
        # self._params["y1"] = y1
        # self._params["x2"] = x2
        # self._params["y2"] = y2
        self.steps("../data/user.yaml", "goto_usermessage")
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text

    # 进入收藏页面
    def goto_usercollect(self):
        # self.find(By.XPATH, "//*[@text='我的收藏']").click()
        # self.swipe(x1,y1,x2,y2)
        # self.find(By.XPATH, "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.view.ViewGroup[4]//*[@resource-id='com.mstz.xf:id/image']").click()
        self.steps("../data/user.yaml", "goto_usercollect")
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text

    # 进入我的打卡页面
    def goto_clock(self):
        # self.find(By.XPATH, "//*[@text='我的打卡']").click()
        self.steps("../data/user.yaml", "goto_clock")
        toast = self.find(By.XPATH, "//*[@resource-id='com.mstz.xf:id/layout']//*[@text='我打卡过的店铺都会显示在这里哦']")
        return toast.text

    # 进入我上传的店铺信息/线索页面
    def goto_shop_clue(self):
        # self.find(By.XPATH, "//*[@text='我上传的店铺信息']").click()
        # self.find(By.XPATH, "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.view.ViewGroup[1]").click()
        self.steps("../data/user.yaml", "goto_shop_clue")
        toast = self.find(By.XPATH, "//*[@text='探店内容']")
        return toast.text
