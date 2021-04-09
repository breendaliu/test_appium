import sys

sys.path.append('..')
from page.app import App


class TestAddtional:
    def setup(self):
        self.infomation = App().start().main().goto_additional()

    def test_shop_photo(self):
        assert "OK" in self.infomation.shop_photo()

    def test_shop_price(self):
        assert "OK" in self.infomation.shop_price('10')

    def test_shop_price_null(self):
        assert "您在此店铺消费的人均价格" in self.infomation.shop_price_null("")

    def test_shop_describe(self):
        assert "OK" in self.infomation.shop_describe("描述描述描述描述")

    def test_shop_describe_null(self):
        assert "店铺描述" in self.infomation.shop_describe_null(" ")

    def test_shop_address(self):
        assert "上传人均价" in self.infomation.shop_address()

    def test_shop_address_detail(self):
        assert "OK" in self.infomation.shop_address_detail("详细地址详细详细详细")

    def test_shop_address_detail_null(self):
        assert "店铺位置" in self.infomation.shop_address_detail_null("")

    def test_shop_hours(self):
        assert "上传人均价" in self.infomation.shop_hours()

    def test_shop_phone(self):
        assert "OK" in self.infomation.shop_phone('18511111111')

    # 1
    def test_shop_phone_str(self):
        assert "OK" in self.infomation.shop_phone("saihdfashf")

    def test_shop_phone_null(self):
        assert "请输入商家的电话号码" in self.infomation.shop_phone_null("")

    # 2
    def test_shop_phone_chinese(self):
        assert "OK" in self.infomation.shop_phone("啊啊啊啊")

    def test_shop_menu(self):
        assert "OK" in self.infomation.shop_menu()

    def test_shop_zhaopaic(self):
        assert "OK" in self.infomation.shop_zhaopaic("caicaicai")

    # 招牌菜名字为空
    def test_shop_zhaopaic_name_null(self):
       assert "招牌菜信息" in self.infomation.shop_zhaopaic_name_null("")

    # 招牌菜名字为空
    def test_shop_zhaopaic_photo_null(self):
       assert "招牌菜信息" in self.infomation.shop_zhaopaic_photo_null("caicai")