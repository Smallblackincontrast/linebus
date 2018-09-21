#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: RuanZhe

from se_basic.web_flow_test_case import WebFlowTestCase


class TestGuntherWebLogin(WebFlowTestCase):

	def setUp(self):
		self.url = "http://test.bigappleexpress.com/"
		# login按钮
		self._loc_login_button = ".user>div:nth-child(5)"
		# 国家号
		self._loc_country_code = ".arrow"
		self._loc_country_code_select = ".flag-dropdown li[data-country-code=cn]"
		# 手机号输入框
		self._loc_phone_number = "input[sid='phoneInput']"
		# 邮箱输入框
		self._loc_email_number = "input[sid='email']"
		# 密码框
		self._loc_password = "input[sid='passwordInput']"
		# SignIn按钮
		self._loc_sign_in = "div[sid='signInBtn']"
		# 个人中心按钮
		self._loc_my_account = ".user>div:nth-child(3)"
		# 登录失败提示
		self._loc_login_failed_message = "p[sid='message']"
		# email登录方式切换
		self._loc_change_to_email = "div[sid='emailRadio']>div[sid='radio']"

	def _click_login(self):
		self.click(self._loc_login_button)

	def _login_by_telephone(self):
		self.click(self._loc_country_code)
		self.click(self._loc_country_code_select)

	def _login_by_email(self):
		self.click(self._loc_change_to_email)

	def _send_telephone_number(self, username):
		self.send_keys(self._loc_phone_number, username)

	def _send_email_number(self, username):
		self.send_keys(self._loc_email_number, username)

	def _send_password(self, password):
		self.send_keys(self._loc_password, password)

	def _click_sign(self):
		self.click(self._loc_sign_in)

	def login_flow(self, username, password, is_telphone: bool = True):
		self.open(self.url, is_auto_close=True)
		self.maximize_window()
		self._click_login()
		if is_telphone:
			self._login_by_telephone()
			self._send_telephone_number(username)
		else:
			self._login_by_email()
			self._send_email_number(username)
		self._send_password(password)
		self._click_sign()

	# 已注册手机号登录
	def test_telphone_login_success(self):
		self._login_flow("17863803770", "666666")
		self.keep()
		self.assertEqual(self.get_text(self._loc_my_account), "MY ACCOUNT", msg="登陆成功！")

	# 未注册手机号登录
	def test_telphone_login_failed(self):
		self._login_flow("17888888888", "666666")
		self.keep()
		self.assertEqual(self.get_text(self._loc_login_failed_message), "User account not existed", msg="登录失败")

	# 已注册邮箱登录
	def test_email_login_success(self):
		self._login_flow("ruanzhe@riverroad.cn", "666666", is_telphone=False)
		self.keep()
		self.assertEqual(self.get_text(self._loc_my_account), "MY ACCOUNT", msg="登陆成功！")

	# 未注册邮箱登录
	def test_email_login_failed(self):
		self._login_flow("123123@riverroad.cn", "666666", is_telphone=False)
		self.keep()
		self.assertEqual(self.get_text(self._loc_login_failed_message), "User account not existed", msg="登录失败")
