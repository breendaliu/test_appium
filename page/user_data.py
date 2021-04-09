import allure
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class UserData(BasePage):
    # 修改头像
    def useredit(self):
        # self.find(By.ID, 'ivPhoto').click()
        # self.find(By.XPATH,
        #           "//*[@resource-id='com.mstz.xf:id/rv_photo_picker_content']/android.widget.RelativeLayout[2]").click()
        # self.find(By.ID, 'tv_photo_picker_preview_choose').click()
        # self.find(By.ID, 'tv_photo_picker_preview_submit').click()
        # self.find(By.ID, 'menu_crop').click()
        self.steps("../data/user_data.yaml", "useredit")
        toast = self.find(By.ID, 'com.mstz.xf:id/right_tv')
        return toast.text

    # 修改昵称
    def uesrname(self, username):
        # self.find(By.XPATH, "//*[@text='昵称']").click()
        # self.find(By.ID, "et_nickName").click()
        # self.find(By.ID, "et_nickName").send_keys(username)
        # self.find(By.XPATH, "//*[@text='确 定']").click()
        self._params['username'] = username
        self.steps("../data/user_data.yaml", "uesrname")
        toast = self.find(By.ID, 'com.mstz.xf:id/nickName')
        return toast.text

    # 修改性别，女
    def usersex_nv(self):
        # self.find(By.XPATH, "//*[@text='性别']").click()
        # self.find(By.ID, 'nv').click()
        # self.find(By.XPATH, "//*[@text='确 定']").click()
        self.steps("../data/user_data.yaml", "usersex_nv")
        toast = self.find(By.ID, 'com.mstz.xf:id/gender')
        return toast.text

    # 修改性别，男
    def usersex_nan(self):
        self.steps("../data/user_data.yaml", "usersex_nan")
        toast = self.find(By.ID, 'com.mstz.xf:id/gender')
        return toast.text

    # 选择城市，上拉页面，选择第12个
    def user_city_list(self):
        # self.find(By.XPATH, "//*[@text='城市']").click()
        # self.swipe(x1, y1, x2, y2)
        # self.find(By.XPATH, "//*[@class='android.widget.LinearLayout' and @index='12']").click()
        self.steps("../data/user_data.yaml", "user_city_list")
        toast = self.find(By.ID, 'com.mstz.xf:id/right_tv')
        return toast.text

    # 选择热门城市
    def user_city_hot(self):
        self.steps("../data/user_data.yaml", "user_city_hot")
        toast = self.find(By.ID, 'com.mstz.xf:id/right_tv')
        return toast.text

    # 城市，搜索
    def user_city_search(self, cityname):
        self._params["cityname"] = cityname
        self.steps('../data/user_data.yaml', "user_city_search")
        toast = self.find(By.ID, 'com.mstz.xf:id/right_tv')
        return toast.text

    # 点击GPS定位
    def user_city_gps(self):
        self.steps('../data/user_data.yaml', "user_city_gps")
        toast = self.find(By.ID, 'com.mstz.xf:id/right_tv')
        return toast.text

    # 选择历史记录城市
    def user_city_history(self):
        self.steps('../data/user_data.yaml', "user_city_history")
        toast = self.find(By.ID, 'com.mstz.xf:id/right_tv')
        return toast.text

    # 保存
    def user_update(self):
        # self.find(By.XPATH, "//*[@text='保存']").click()
        self.steps('../data/user_data.yaml', "user_update")
        toast = self.find(By.XPATH, "//*[@text='个人主页']")
        return toast.text
