import sys

import pytest

sys.path.append('..')
from page.app import App


class TestSet:
    def setup(self):
        self.set = App().start().main().goto_set()

    def test_xieyi(self):
        assert "设置" in self.set.xieyi()

    def test_clear(self):
        assert "设置" in self.set.clear()

    def test_yinsi(self):
        assert "设置" in self.set.yinsi()

    def test_weixin(self):
        assert "设置" in self.set.weixin()

    @pytest.mark.run(order=5)
    def test_quite(self):
        assert "收录店铺" in self.set.quite()
