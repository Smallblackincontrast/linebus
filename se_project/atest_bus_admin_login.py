from selenium.webdriver.common.keys import Keys

from se_basic.web_flow_test_case import WebFlowTestCase


class TestBusAdminLogin(WebFlowTestCase):
    def setUp(self):
        self.url = "http://line-dev.riverroad.cn/#/login"
        self.loc_user_name = "input[name=username]"
        self.loc_user_password = "input[name=password]"
        self.loc_error_message = ".el-message--error"

    def _login_flow(self, user_name, password):
        self.open(self.url)
        self.send_keys(self.loc_user_name, user_name)  # 输入用户名
        self.send_keys(self.loc_user_password, password)  # 输入密码
        self.send_keys(self.loc_user_password, Keys.ENTER, False, True)  # 按回车登录

    def test_login_success(self):
        self._login_flow("riverRoadAdmin", "123456")
        self.keep(3)
        self.assertEqual(self.get_current_url(), "http://line-dev.riverroad.cn/#/ticket/ticketList", "验证登录成功的用例不通过")

    def test_login_faild(self):
        self._login_flow("admin", "111111")
        self.keep()
        self.assertTrue(self.get_display(self.loc_error_message))
