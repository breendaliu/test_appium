from selenium.webdriver.common.by import By
from page.add import AddShop
from page.additional_shop import Additional
from page.base_page import BasePage
# 功能按钮
from page.content import Content
from page.set import Set
from page.search import Search
from page.shop_detail import ShopDetail
from page.user import User
from page.user_data import UserData
from page.user_home import UserHome
from page.user_shop import UserShop


class Main(BasePage):
    # 从首页，进入上传店铺页面
    def goto_addshop(self):
        self.steps("../data/main.yaml", "goto_addshop")
        return AddShop(self._driver)

    # 从首页，进入搜索页面
    def goto_search(self):
        self.steps('../data/main.yaml', "goto_search")
        return Search(self._driver)

    # 从首页，进入我的页面
    def goto_user(self):
        self.steps("../data/main.yaml", "goto_user")
        return User(self._driver)

    # 进入补充店铺信息页。搜索米线，进入第一条数据中的店铺详情页面，点击补充店铺信息按钮
    def goto_additional(self):
        self.goto_search()
        self.steps("../data/main.yaml", "goto_shop_addtional")
        return Additional(self._driver)

    def goto_shop_detail(self):
        self.goto_search()
        self.steps("../data/main.yaml", "goto_shop_detail")
        return ShopDetail(self._driver)

    # 从我的页面，编辑个人资料
    def goto_userdata(self):
        self.goto_user()
        self.steps("../data/main.yaml", "goto_userdata")
        return UserData(self._driver)

    # 从我的页面，进入个人主页
    def goto_userhome(self):
        self.goto_user()
        self.steps("../data/main.yaml", "goto_userhome")
        return UserHome(self._driver)

    # 从我的页面，进入我的推荐页面
    def goto_usershop(self):
        self.goto_user()
        self.steps("../data/main.yaml", "goto_usershop")
        return UserShop(self._driver)

    # 从个人主页，进入设置页面
    def goto_set(self):
        self.goto_userhome()
        self.steps("../data/main.yaml", "goto_set")
        return Set(self._driver)

    # 从设置页面，进入意见反馈页面
    def goto_content(self):
        self.goto_set()
        self.steps("../data/main.yaml", "goto_content")
        return Content(self._driver)
