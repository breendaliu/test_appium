import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class UserHome(BasePage):
    # 进入编辑资料页
    def userhome_data(self):
        # self.find(By.ID, 'photo').click()
        self.steps("../data/user_home.yaml", "userhome_data")
        toast = self.find(By.XPATH, '//*[@text="编辑资料"]')
        return toast.text

    # 进入消息页
    def uerhome_message(self):
        # self.find(By.ID, 'rightLayout').click()
        self.steps("../data/user_home.yaml", "uerhome_message")
        toast = self.find(By.XPATH, '//*[@text="消息"]')
        return toast.text

    # 进入设置页
    def userhome_set(self):
        # self.find(By.ID, 'right_img').click()
        self.steps("../data/user_home.yaml", "userhome_set")
        toast = self.find(By.XPATH, '//*[@text="设置"]')
        return toast.text

    # 进入店铺推荐页
    def userhome_shop(self):
        # self.find(By.XPATH, "//*[@text='店铺推荐' and @class='android.widget.TextView']").click()
        self.steps("../data/user_home.yaml", "userhome_shop")
        toast = self.find(By.XPATH, '//*[@text="我上传的店铺" and @class="android.widget.TextView"]')
        return toast.text

    # 进入平台排名页
    def userhome_top(self):
        # self.find(By.XPATH, "//*[@text='平台排名' and @class='android.widget.TextView']").click()
        self.steps("../data/user_home.yaml", "userhome_top")
        toast = self.find(By.XPATH, '//*[@text="推荐排行榜" and contains(@resource-id, tv_title_title)]')
        return toast.text

    # 上拉页面,等待5秒，下拉页面，点击推荐标签下的店铺
    def userhome_shoppass(self):
        # ,x1,y1,x2,y2,a,b,c,d
        # self.swipe(x1,y1,x2,y2)
        # time.sleep(5)
        # self.swipe(a, b, c, d)
        # self.find(By.XPATH, "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.widget.RelativeLayout[1]").click()
        self.steps("../data/user_home.yaml", "userhome_shoppass")
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text

    # 切换到评价，上拉页面，点击展开、收起、店铺,x1,y1,x2,y2
    def userhome_comment(self):
        # self.find(By.XPATH, '//*[@text="评价"]').click()
        # self.swipe(x1,y1,x2,y2)
        # self.find(By.XPATH,
        #           "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.widget.LinearLayout[2]/*[@resource-id='com.mstz.xf:id/shopLayout']").click()
        self.steps("../data/user_home.yaml", 'userhome_comment')
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text

    # 切换到收藏，点击店铺信息,x1,y1,x2,y2
    def userhome_collect(self):
        # self.find(By.XPATH, "//*[@text='收藏']").click()
        # self.swipe(x1,y1,x2,y2)
        # self.find(By.XPATH,
        #           "//*[@resource-id='com.mstz.xf:id/recyclerView']/android.view.ViewGroup[2]").click()
        self.steps("../data/user_home.yaml", 'userhome_collect')
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text
