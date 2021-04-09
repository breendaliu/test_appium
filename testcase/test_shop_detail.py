import sys
sys.path.append('..')
from page.app import App


class TestShopDetail:

    def setup(self):
        self.shopdetail=App().start().main().goto_shop_detail()

    def test_shop_photo(self):
        assert "本店探长" in self.shopdetail.shop_photo()

    def test_shop_zhaopaic(self):
        assert "本店探长" in self.shopdetail.shop_zhaopaic()

    def test_shop_vote(self):
        assert "本店探长" in self.shopdetail.shop_vote()

    def test_shop_collect(self):
        assert "本店探长" in self.shopdetail.shop_collect()