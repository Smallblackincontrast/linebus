from se_basic.web_flow_test_case import WebFlowTestCase


class EldLogin(WebFlowTestCase):
    def setUp(self):
        self.url = 'http://eld-demo.riverroad.cn/account/login'
        self._loc_user_name = "#username"
        self._loc_password = "#password"
        self._loc_btn_login = "#loginBtn"

    def test_customer_login_success(self):
        self.open(self.url)
        self.send_keys(self._loc_user_name, "ubtadmin")
        self.send_keys(self._loc_password, "123456")
        self.click("#loginBtn")
        self.keep(2)
        self.assertEqual(self.get_current_url(), "http://eld-demo.riverroad.cn/driver-availability/list", "登录成功未通过")

    def test_customer_login_fail(self):
        self.open(self.url)
        self.send_keys(self._loc_user_name, "wrong_user")
        self.send_keys(self._loc_password, "123456")
        self.click(self._loc_btn_login)
        self.keep(2)
        self.assertEqual(self.get_current_url(), "http://eld-demo.riverroad.cn/account/do-login", "登录失败未通过")
