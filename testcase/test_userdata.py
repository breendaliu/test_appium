import sys

sys.path.append('..')
from page.app import App


class TestUserData:
    def setup(self):
        self.userdata = App().start().main().goto_userdata()

    def test_user_image(self):
        assert "保存" in self.userdata.useredit()

    def test_user_name(self):
        assert "yyy" in self.userdata.uesrname('yyy')

    def test_usersex_nv(self):
        assert "女" in self.userdata.usersex_nv()

    def test_usersex_nan(self):
        assert "男" in self.userdata.usersex_nan()

    def test_usercity_list(self):
        assert "保存" in self.userdata.user_city_list()

    def test_usercity_hot(self):
        assert "保存" in self.userdata.user_city_hot()

    def test_usercity_search(self):
        assert "保存" in self.userdata.user_city_search("北")

    def test_usercity_gps(self):
        assert "保存" in self.userdata.user_city_gps()

    def test_usercity_history(self):
        assert "保存" in self.userdata.user_city_history()

    def test_userupdate(self):
        assert "个人主页" in self.userdata.user_update()
