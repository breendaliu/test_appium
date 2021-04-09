import sys
sys.path.append('..')
from page.app import App


class TestUserhome:
    def setup(self):
        self.user = App().start().main().goto_userhome()

    def test_userhome_data(self):
        assert "编辑资料" in self.user.userhome_data()

    def test_userhome_message(self):
        assert "消息" in self.user.uerhome_message()

    def test_userhome_set(self):
        assert "设置" in self.user.userhome_set()

    def test_userhome_shop(self):
        assert "我上传的店铺" in self.user.userhome_shop()

    def test_userhome_top(self):
        assert "推荐排行榜" in self.user.userhome_top()

    def test_userhome_shoppass(self):
        # 0.5, 0.8, 0.5, 0.2, 0.5, 0.3, 0.5, 0.7
        assert "本店探长" in self.user.userhome_shoppass()

    def test_userhome_comment(self):
        # 0.5, 0.8, 0.5, 0.2
        assert "本店探长" in self.user.userhome_comment()

    def test_userhome_collect(self):
        # 0.5, 0.8, 0.5, 0.2
        assert "本店探长" in self.user.userhome_collect()
