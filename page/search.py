from selenium.webdriver.common.by import By
from page.additional_shop import Additional
from page.base_page import BasePage


class Search(BasePage):

    # 搜索店铺
    def search(self, searchword):
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search")
        # self._driver.press_keycode(66)
        toast = self.find(By.ID, "tvName").text
        return toast

    # # 升级，以后再说
    # def test01(self):
    #     #self.steps("../page/search.yaml", "search_word_list")
    #     #self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
    #     time.sleep(3)
    #     self.find(By.XPATH, '//*[@text="以后再说"]').click()
    #     toast = self.find(By.ID, "tv11")
    #     return toast.text

    # 输入搜索内容，点击下拉列表中第一条数据，进入店铺详情
    def search_word_list(self, searchword):
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search_word_list")
        toast = self.find(By.ID, 'tvZhaoPai')
        return toast.text

    # 搜索第一个热搜词  todo 热搜词不存在时，脚本编辑错误
    def search_hotword(self):
        self.steps("../data/search.yaml", "search_hotword")
        toast = self.find(By.ID, "com.mstz.xf:id/kindsTv1")
        return toast.text

    # 搜索历史记录中第一条数据，todo 数据不存在时，不搜索
    def search_word_history(self):
        self.steps("../data/search.yaml", "search_word_history")
        toast = self.find(By.ID, "kindsTv1").text
        return toast

    # 删除历史记录中第一条数据
    def search_history_word_delete(self):
        self.steps("../data/search.yaml", "search_history_word_delete")
        toast = self.find(By.ID, "hisTv").text
        return toast

    # 搜索不存在的店铺，点击上传店铺按钮
    def search_shop_without(self, searchword):
        # self.find(By.ID, "et_key").click()
        # self.find(By.ID, "et_key").send_keys(searchword)
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search_shop_without")
        # self._driver.press_keycode(66)
        # self.find(By.ID, 'campaign').click()
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 搜索页面点击取消按钮
    def search_cancel(self):
        # self.find(By.ID, "tvCancel").click()
        self.steps("../data/search.yaml", "search_cancel")
        toast = self.find(By.ID, "tv11")
        return toast.text

    # 搜索结果页面，切换到搜索位置，选择列表中相关数据查询
    def search_result_address(self, searchword):
        # self.find(By.ID, "et_key").click()
        # self.find(By.ID, "et_key").send_keys(searchword)
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search_result_address")
        # self._driver.press_keycode(66)
        # self.find(By.ID, "kindsTv3").click()
        # self.find(By.XPATH,
        #           '//*[@resource-id="com.mstz.xf:id/searchRecyclerView"]/android.widget.LinearLayout[5]').click()
        toast = self.find(By.ID, 'kindsTv3')
        return toast.text

    # 搜索结果页面点击取消按钮，返回首页
    def search_result_cancel(self, searchword):
        # self.find(By.ID, "et_key").click()
        # self.find(By.ID, "et_key").send_keys(searchword)
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search_result_cancel")
        # self._driver.press_keycode(66)
        # self.find(By.ID, "tvCancel").click()
        toast = self.find(By.ID, "tv11")
        return toast.text

    # 位置搜索结果页，选中某一店铺，进入店铺详情页
    def search_result_address_shopdetail(self, searchword):
        # self.find(By.ID, "et_key").click()
        # self.find(By.ID, "et_key").send_keys(searchword)
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search_result_address_shopdetail")
        # self._driver.press_keycode(66)
        # self.find(By.ID, "kindsTv3").click()
        # self.find(By.XPATH,
        #           '//*[@resource-id="com.mstz.xf:id/searchRecyclerView"]/android.widget.LinearLayout[1]').click()
        # self.find(By.XPATH, '//*[@resource-id="com.mstz.xf:id/recyclerView"]/android.widget.RelativeLayout[2]').click()
        toast = self.find(By.ID, 'tvZhaoPai')
        return toast.text

    # 搜索结果页，选择某一店铺点击上传店铺信息按钮 todo 搜索结果页中上传店铺按钮不存在或下拉多次才显示的情况下，报错
    def search_result_add_shopdetail(self, searchword):
        # self.find(By.ID, "et_key").click()
        # self.find(By.ID, "et_key").send_keys(searchword)
        self._params["searchword"] = searchword
        self.steps("../data/search.yaml", "search_result_add_shopdetail")
        # self._driver.press_keycode(66)
        # self.find(By.ID, "kindsTv3").click()
        # self.find(By.ID, "com.mstz.xf:id/uploadTv").click()
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # # 输入搜索内容，点击下拉列表中第一条数据，进入店铺详情
    # def goto_shop_detail(self):
    #     # self.find(By.ID, "et_key").click()
    #     # self.find(By.ID, "et_key").send_keys("米线")
    #     # self.find(By.XPATH,
    #     #           "//*[@resource-id='com.mstz.xf:id/searchRecyclerView']/android.widget.LinearLayout[1]").click()
    #     self.steps("../data/search.yaml", "goto_shop_detail")
    #     # self.swipe(0.5, 0.7, 0.5, 0.3)
    #     # self.find(By.XPATH, "//*[@text='补充店铺信息']").click()
    #     return Additional(self._driver)
