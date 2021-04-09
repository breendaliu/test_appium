import sys

sys.path.append('..')
import pytest
import yaml
from page.app import App


class TestAddshop:
    def setup(self):
        self.shop = App().start().main().goto_addshop()

    def load_yaml(self):
        with open("./test_add.yaml", encoding="utf-8") as f:
            result = yaml.safe_load(f)
        return result

    @pytest.mark.parametrize("shopname, addressdescribe, reason", load_yaml(1))
    def test_add_shop(self, shopname, addressdescribe, reason):
        assert "查看我推荐的美食店铺" in self.shop.add_shop(shopname, addressdescribe, reason)

    def test_add_shop_noname(self):
        assert "上传店铺" in self.shop.add_shop_noname("详细地址啊啊啊啊", '推荐理由啊啊啊')

    @pytest.mark.parametrize("shopname, addressdescribe, reason", load_yaml(1))
    def test_add_shop_noadress(self, shopname, addressdescribe, reason):
        # self.shop.add_shop_noaddress(shopname, addressdescribe, reason)
        assert "上传店铺" in self.shop.add_shop_noaddress(shopname, addressdescribe, reason)

    @pytest.mark.parametrize("shopname, addressdescribe, reason", load_yaml(1))
    def test_add_shop_list(self, shopname, addressdescribe, reason):
        assert "查看我推荐的美食店铺" in self.shop.add_shop_listname(shopname, addressdescribe, reason)

    def test_add_shop_address_maps(self):
        # , 0.7, 0.3, 0.6, 0.6
        assert "上传店铺" in self.shop.add_shop_address_maps('呃呃呃')

    def test_add_shop_address_mapslist(self):
        # 0.5, 0.7, 0.5, 0.3
        assert "上传店铺" in self.shop.add_shop_address_maps_list()

    def test_add_shop_no_addressdescribe(self):
        assert "查看我推荐的美食店铺" in self.shop.add_shop_no_addressdescribe("eeeee", "hhhhhh")

    def test_add_shop_no_reason(self):
        assert "上传店铺" in self.shop.add_shop_no_reason("cccc", "dddddddd")

    def test_add_shop_into_detail(self):
        assert "本店探长" in self.shop.add_shop_into_detail("cccc", "dddddddd")

    def test_add_shop_search_address(self):
        assert "上传店铺" in self.shop.add_shop_seach_address("中原万达")

    def test_add_shop_return(self):
        assert "收录店铺" in self.shop.add_shop_return("111")


