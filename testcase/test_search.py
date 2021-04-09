import sys
sys.path.append('..')
# 增加sys.path.append('..')是为了解决使用pytest执行用例时报错：调用page
from page.app import App

class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_search()

    # def test_test01(self):
    #     assert "收录店铺" in self.search.test01()

    def test_search(self):
        assert "美食-米线" in self.search.search("米线")

    def test_search_list(self):
        assert "招牌菜" in self.search.search_word_list("米线")

    def test_search_hotword(self):
        assert "搜美食" in self.search.search_hotword()

    def test_search_history(self):
        assert "搜美食" in self.search.search_word_history()

    def test_search_history_delete(self):
        assert "搜索记录" in self.search.search_history_word_delete()

    def test_search_shop_without(self):
        assert "上传店铺" in self.search.search_shop_without("llll")

    def test_search_cancel(self):
        assert "收录店铺" in self.search.search_cancel()

    def test_result_address(self):
        assert "搜位置" in self.search.search_result_address("米线")

    def test_result_cancel(self):
        assert "收录店铺" in self.search.search_result_cancel("米线城西")

    def test_result_address_shopdetail(self):
        assert "招牌菜" in self.search.search_result_address_shopdetail("金水路")

    def test_result_add_shopdetail(self):
        assert "上传店铺信息" in self.search.search_result_add_shopdetail("米mimi")
