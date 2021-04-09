import sys
sys.path.append('..')
from page.app import App


class TestUserShop:
    def setup(self):
        self.shop = App().start().main().goto_usershop()

    def test_user_shop_check(self):
        # 0.5, 0.8, 0.5, 0.2
        assert "店铺信息审核中" in self.shop.shop_check()

    def test_user_shop_not_pass(self):
        assert "审核失败原因：" in self.shop.shop_not_pass()

    def test_user_shop_pass(self):
        assert "本店探长" in self.shop.shop_pass()

    def test_shop_add(self):
        assert "确认上传" in self.shop.shop_add()
