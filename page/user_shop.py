from selenium.webdriver.common.by import By

from page.base_page import BasePage


class UserShop(BasePage):

    # 切换到审核中店铺，上拉列表，选择一店铺进入店铺详情,x1,y1,x2,y2
    def shop_check(self):
        # self.find(By.XPATH, "//*[@text='审核中' and @class='android.widget.TextView']").click()
        # self.swipe(x1,y1,x2,y2)
        # self.find(By.XPATH,
        #           "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.widget.RelativeLayout[3]//*[@resource-id='com.mstz.xf:id/image']").click()
        self.steps("../data/user_shop.yaml", "shop_check")
        toast = self.find(By.XPATH, "//*[@text='店铺信息审核中']")
        return toast.text

    # 切换到审核失败店铺，上拉列表，选择一店铺进入店铺详情
    def shop_not_pass(self):
        # self.find(By.XPATH, "//*[@text='审核失败' and @class='android.widget.TextView']").click()
        # self.find(By.XPATH,
        #           "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.widget.RelativeLayout[1]//*[@resource-id='com.mstz.xf:id/image']").click()
        self.steps("../data/user_shop.yaml", "shop_not_pass")
        toast = self.find(By.ID, 'com.mstz.xf:id/tv')
        return toast.text

    # 进入审核通过店铺，上拉列表，选择一店铺进入店铺详情
    def shop_pass(self):
        # self.find(By.XPATH, "//*[@text='审核中' and @class='android.widget.TextView']").click()
        # self.find(By.XPATH, "//*[@text='审核失败' and @class='android.widget.TextView']").click()
        # self.find(By.XPATH, "//*[@content-desc='审核通过']").click()
        # self.find(By.XPATH,
        #           "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.widget.RelativeLayout[1]//*[@resource-id='com.mstz.xf:id/image']").click()
        self.steps("../data/user_shop.yaml", "shop_pass")
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text

    # 进入上传店铺页面
    def shop_add(self):
        # self.find(By.ID, 'com.mstz.xf:id/right_img').click()
        self.steps("../data/user_shop.yaml", "shop_add")
        toast = self.find(By.ID, 'com.mstz.xf:id/upload')
        return toast.text
