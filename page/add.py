from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AddShop(BasePage):
    # 上传店铺，选择当前位置
    def add_shop(self, shopname, addressdescribe, reason):
        # 店铺名称
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # # 点击确定按钮
        # self.find(By.ID, 'cancel').click()
        # # 点击获取当前位置按钮
        # self.find(By.ID, 'currentLocation').click()
        # # 输入详细位置
        # self.find(By.ID, 'etAddressDescribe').send_keys(addressdescribe)
        # # 输入推荐理由
        # self.find(By.ID, 'etReason').send_keys(reason)
        # # 点击确认上传按钮
        # self.find(By.ID, 'upload').click()
        # 点击查看我上传的店铺按钮
        self._params["shopname"] = shopname
        self._params['addressdescribe'] = addressdescribe
        self._params['reason'] = reason
        self.steps("../data/add.yaml", "add_shop")
        toast = self.find(By.ID, 'checkMyShop')
        return toast.text

    # 上传店铺，不输入店铺名称
    def add_shop_noname(self, addressdescribe, reason):
        # self.find(By.ID, 'currentLocation').click()
        # self.find(By.ID, 'etAddressDescribe').send_keys(addressdescribe)
        # self.find(By.ID, 'etReason').send_keys(reason)
        # self.find(By.ID, 'upload').click()
        self._params['addressdescribe'] = addressdescribe
        self._params['reason'] = reason
        self.steps("../data/add.yaml", "add_shop_noname")
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 上传店铺，不选择地址
    def add_shop_noaddress(self, shopname, addressdescribe, reason):
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # self.find(By.ID, 'cancel').click()
        # self.find(By.ID, 'etAddressDescribe').send_keys(addressdescribe)
        # self.find(By.ID, 'etReason').send_keys(reason)
        # self.find(By.ID, 'upload').click()
        self._params["shopname"] = shopname
        self._params['addressdescribe'] = addressdescribe
        self._params['reason'] = reason
        self.steps("../data/add.yaml", "add_shop_noaddress")
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 上传店铺，选择下拉列表中数据
    def add_shop_listname(self, shopname, addressdescribe, reason):
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # self.find(By.XPATH, '//*[@resource-id="com.mstz.xf:id/recyclerView"]/android.view.ViewGroup[3]').click()
        # self.find(By.ID, 'etAddressDescribe').send_keys(addressdescribe)
        # self.find(By.ID, 'etReason').send_keys(reason)
        # self.find(By.ID, 'upload').click()
        self._params["shopname"] = shopname
        self._params['addressdescribe'] = addressdescribe
        self._params['reason'] = reason
        self.steps("../data/add.yaml", "add_shop_listname")
        toast = self.find(By.ID, 'checkMyShop')
        return toast.text

    # 上传店铺，滑动高德地图，选择店铺位置, x1, y1, x2, y2
    def add_shop_address_maps(self, shopname):
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # self.find(By.ID, 'cancel').click()
        # self.find(By.ID, 'select').click()
        # self.swipe(x1, y1, x2, y2)
        # self.find(By.ID, 'confirm').click()
        self._params["shopname"] = shopname
        self.steps("../data/add.yaml", "add_shop_address_maps")
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 上传店铺，滑动地图列表，选择店铺位置, x1, y1, x2, y2
    def add_shop_address_maps_list(self):
        # self.find(By.ID, 'select').click()
        # self.swipe(x1, y1, x2, y2)
        # self.find(By.XPATH, '//*[@resource-id="com.mstz.xf:id/recyclerView"]/android.widget.LinearLayout[5]').click()
        # self.find(By.ID, 'confirm').click()
        self.steps("../data/add.yaml", "add_shop_address_maps_list")
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 上传店铺，不输入详细地址,上传成功后返回首页
    def add_shop_no_addressdescribe(self, shopname, reason):
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # self.find(By.ID, 'cancel').click()
        # self.find(By.ID, 'currentLocation').click()
        # self.find(By.ID, 'etReason').send_keys(reason)
        # self.find(By.ID, 'upload').click()
        # self.find(By.ID, 'com.mstz.xf:id/ll_title_back').click()
        self._params["shopname"] = shopname
        self._params["reason"] = reason
        self.steps("../data/add.yaml", "add_shop_no_addressdescribe")
        toast = self.find(By.ID, 'checkMyShop')
        return toast.text

    # 上传店铺，搜索位置
    def add_shop_seach_address(self, address):
        # self.find(By.ID, 'select').click()
        # self.find(By.XPATH, "//*[@text='搜索地点']").send_keys(address)
        # self.find(By.XPATH, '//*[@resource-id="com.mstz.xf:id/recyclerView"]/android.widget.LinearLayout[3]').click()
        # self.find(By.ID, 'confirm').click()
        self._params["address"] = address
        self.steps("../data/add.yaml", "add_shop_seach_address")
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 上传店铺，不输入推荐理由
    def add_shop_no_reason(self, shopname, addressdescribe):
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # self.find(By.ID, 'cancel').click()
        # self.find(By.ID, 'currentLocation').click()
        # self.find(By.ID, 'etAddressDescribe').send_keys(addressdescribe)
        # self.find(By.ID, 'upload').click()
        self._params["shopname"] = shopname
        self._params['addressdescribe'] = addressdescribe
        self.steps("../data/add.yaml", "add_shop_no_reason")
        toast = self.find(By.ID, 'tv_title_title')
        return toast.text

    # 上传店铺，成功后进入店铺详情页
    def add_shop_into_detail(self, shopname, reason):
        # self.find(By.ID, 'etShopName').send_keys(shopname)
        # self.find(By.ID, 'cancel').click()
        # self.find(By.ID, 'currentLocation').click()
        # self.find(By.ID, 'etReason').send_keys(reason)
        # self.find(By.ID, 'upload').click()
        # self.find(By.ID, 'checkMyShop').click()
        self._params["shopname"] = shopname
        self._params['reason'] = reason
        self.steps("../data/add.yaml", "add_shop_into_detail")
        toast = self.find(By.XPATH, '//*[@text="本店探长" and contains(@resource-id, "tze")]')
        return toast.text

    # 进入搜索位置页面，输入地址后取消输入信息->点击左上角取消，返回上传店铺页，返回首页
    def add_shop_return(self, address):
        # self.find(By.ID, 'select').click()
        # self.find(By.XPATH, "//*[@text='搜索地点']").send_keys(address)
        # self.find(By.XPATH, "//*[@text='取消' and contains(@resource-id, 'cancel')]").click()
        # self.find(By.XPATH, "//*[@class='android.widget.RelativeLayout']//*[@text='取消']").click()
        # self.find(By.ID, "ll_title_back").click()
        self._params["address"] = address
        self.steps("../data/add.yaml", "add_shop_return")
        toast = self.find(By.ID, "tv11")
        return toast.text
