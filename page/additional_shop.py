import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class Additional(BasePage):

    # 贡献照片/视频
    def shop_photo(self):
        self.steps("../data/additional_shop.yaml", "shop_photo")
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    # 上传人均价
    def shop_price(self, price):
        self._params["price"] = price
        self.steps("../data/additional_shop.yaml", "shop_price")
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    def shop_price_null(self, price):
        self._params["price"] = price
        self.steps("../data/additional_shop.yaml", "shop_price")
        toast = self.find(By.XPATH, "//*[@text='您在此店铺消费的人均价格']")
        return toast.text

    # 编辑店铺描述 todo
    def shop_describe(self, describe):
        self._params["describe"] = describe
        self.steps("../data/additional_shop.yaml", "shop_describe")
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    def shop_describe_null(self, describe):
        self._params["describe"] = describe
        self.steps("../data/additional_shop.yaml", "shop_describe")
        toast = self.find(By.XPATH, "//*[@text='店铺描述']")
        return toast.text
    # 查看路线
    def shop_address(self):
        self.steps("../data/additional_shop.yaml", "shop_address")
        toast = self.find(By.ID, "updatePrice")
        return toast.text

    # 完善位置信息
    def shop_address_detail(self, address):
        self._params["address"] = address
        self.steps("../data/additional_shop.yaml", "shop_address_detail")
        # self.find(By.XPATH, "//*[@text='完善位置信息']").click()
        # self.find(By.ID, "com.mstz.xf:id/etDescribe").send_keys(address)
        # self.find(By.XPATH, "//*[@text='确认提交' and contains(@resource-id, 'tvSubmit')]").click()
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    def shop_address_detail_null(self, address):
        self._params["address"] = address
        self.steps("../data/additional_shop.yaml", "shop_address_detail")
        toast = self.find(By.XPATH, "//*[@text='店铺位置']")
        return toast.text

    # 补充营业时间
    def shop_hours(self):
        self.find(By.XPATH, "//*[@text='编辑营业时间' and contains(@resource-id, 'etTime')]").click()
        # 上午开始时间调整（小时）
        time.sleep(3)
        for i in range(1):
            TouchAction(self._driver) \
                .long_press(x=260, y=890) \
                .move_to(x=260, y=726) \
                .release() \
                .perform()
        time.sleep(3)
        # 上午开始时间调整（分钟）
        for i in range(1):
            TouchAction(self._driver) \
                .long_press(x=500, y=917) \
                .move_to(x=500, y=800) \
                .release() \
                .perform()
        # 下午时间截至时间调整（小时）
        for i in range(1):
            TouchAction(self._driver) \
                .long_press(x=670, y=1300) \
                .move_to(x=670, y=1230) \
                .release() \
                .perform()
        self.find(By.XPATH, "//*[@text='确认提交' and contains(@resource-id, 'tvSubmit')]").click()
        self.find(By.XPATH, "//*[@text='OK']").click()
        toast = self.find(By.ID, "updatePrice")
        return toast.text

    # 编辑电话 todo
    def shop_phone(self, phone):
        # self.find(By.XPATH, "//*[@text='编辑电话' and contains(@resource-id, 'etPhone')]").click()
        # self.find(By.XPATH, "//*[@text='请输入商家的电话号码' and contains(@resource-id, 'etPhone')]").send_keys(phone)
        # self.find(By.XPATH, "//*[@text='确认提交' and contains(@resource-id, 'tvSubmit')]").click()
        self._params["phone"] = phone
        self.steps("../data/additional_shop.yaml", "shop_phone")
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    def shop_phone_null(self, phone):
        self._params["phone"] = phone
        self.steps("../data/additional_shop.yaml", "shop_phone")
        toast = self.find(By.XPATH, "//*[@text='请输入商家的电话号码']")
        return toast.text

    # 上传店铺菜单
    def shop_menu(self):
        # self.find(By.XPATH, "//*[@text='上传店铺菜单' and contains(@resource-id, 'addMenu')]").click()
        # self.find(By.XPATH,
        #                   "//*[@resource-id='com.mstz.xf:id/picture_recycler']/android.widget.RelativeLayout[9]//*[@resource-id='com.mstz.xf:id/btnCheck']").click()
        # self.find(By.XPATH, "//*[@text='已完成']").click()
        self.steps("../data/additional_shop.yaml", "shop_menu")
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    # 上传招牌菜
    def shop_zhaopaic(self, zhaopaic):
        # self.find(By.XPATH, "//*[@text='贡献招牌菜' and contains(@resource-id, 'layoutAddCai')]").click()
        # self.find(By.XPATH, "//*[@text='请输入菜品名称' and contains(@resource-id, 'etCaiName')]").send_keys(zhaopaic)
        # self.find(By.ID, "fiv").click()
        # self.find(By.XPATH,
        #                   "//*[@resource-id='com.mstz.xf:id/picture_recycler']/android.widget.RelativeLayout[9]//*[@resource-id='com.mstz.xf:id/btnCheck']").click()
        # self.find(By.XPATH, "//*[@text='已完成']").click()
        # self.find(By.XPATH, "//*[@text='提交完成' and contains(@resource-id, 'submit')]").click()
        self._params["zhaopaic"] = zhaopaic
        self.steps("../data/additional_shop.yaml", "shop_zhaopaic")
        toast = self.find(By.XPATH, "//*[@text='OK']")
        return toast.text

    def shop_zhaopaic_name_null(self, zhaopaic):
        self._params["zhaopaic"] = zhaopaic
        self.steps("../data/additional_shop.yaml", "shop_zhaopaic")
        toast = self.find(By.XPATH, "//*[@text='招牌菜信息']")
        return toast.text


    def shop_zhaopaic_photo_null(self, zhaopaic):
        self._params["zhaopaic"] = zhaopaic
        self.steps("../data/additional_shop.yaml", "shop_zhaopaic_photo_null")
        toast = self.find(By.XPATH, "//*[@text='招牌菜信息']")
        return toast.text