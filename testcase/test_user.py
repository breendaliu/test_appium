import sys
sys.path.append('..')
from page.app import App


class TestUser:
    def setup(self):
        self.user = App().start().main().goto_user()

    def test_user_message(self):
        assert "本店探长" in self.user.goto_usermessage()

    def test_user_collect(self):
        assert "本店探长" in self.user.goto_usercollect()

    def test_user_clock(self):
        assert "我打卡过的店铺都会显示在这里哦" in self.user.goto_clock()

    def test_shop_clue(self):
        assert "探店内容" in self.user.goto_shop_clue()
