from se_basic.web_flow_test_case import WebFlowTestCase


class BusLogin(WebFlowTestCase):
    def setUp(self):
        pass

    def test_login_success(self):
        """login testcase"""
        self.open("https://demo.bigappleexpress.com")
        self.maximize_window()

        # 点击登录
        self.script("HeaderManager.login()")

        # 选择国家号
        self.click(".arrow")
        self.keep()
        self.click(".flag-dropdown li[data-country-code=cn]")

        # 输入手机号
        self.send_keys("input[sid='phoneInput'] ", "17863803770")
        self.keep()

        # 输入密码
        self.send_keys("input[sid='passwordInput']", "666666")

        # 点击sign up
        self.click("div[sid='signInBtn']")

        # 判断是否登录成功
        self.keep(2)
        self.assertNotEqual(self.get_text("em[sid=userNameView]"), "", "登录失败")
