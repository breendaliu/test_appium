from page.app import App


class TestContent:
    def setup(self):
        self.content=App().start().main().goto_content()
    def test_content_all(self):
        assert "设置" in self.content.content_all('意见反馈意见反馈意见反馈')
    def test_content_no_group(self):
        assert "查看反馈" in self.content.content_no_group("测试测试测试测试测试测试")