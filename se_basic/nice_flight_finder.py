"""
    用于检索近期的低价机票
"""
import datetime

from selenium.common.exceptions import NoSuchElementException

from se_basic.web_flow_test_case import WebFlowTestCase


class NiceFlightFinder(WebFlowTestCase):

    def setUp(self):
        # 定位器
        self._loc_nav_flight_nav = "#nav_flight"  # 飞机票菜单定位器
        self._loc_depart_city = "#DepartCity1TextBox"  # 出发城市定位器
        self._loc_arrival_city = "#ArriveCity1TextBox"  # 到达城市定位器
        self._loc_depart_date = "#DepartDate1TextBox"  # 出发日期定位器
        self._loc_search_button = "#search_btn"  # 搜索按钮定位器
        self._loc_lowest_price = ".lowest_price .base_price02"  # 一天最低价格定位器
        self._loc_blank = ".ico-flight"  # 定义一处空白,用于收起弹出菜单

    # 页面动作
    def _enter_flight_search_page(self):  # 进入搜索页
        self.click(self._loc_nav_flight_nav)
        self.keep()

    def _input_start_city(self, city):  # 输入出发城市
        self.send_keys(self._loc_depart_city, city)
        self.keep()
        self.click_blank_area()

    def _input_dest_city(self, city):  # 输入到达城市
        self.send_keys(self._loc_arrival_city, city)
        self.keep()
        self.click_blank_area()

    def _input_depart_date(self, date):  # 输入出发日期
        self.send_keys(self._loc_depart_date, date)
        self.keep()
        self.click_blank_area()

    def _execute_search(self):  # 点击搜索按钮
        self.click(self._loc_search_button)

    def _get_lowest_price(self):  # 获取最低的直达票价格
        try:
            txt_lowest_price = self.get_text(self._loc_lowest_price)
            lowest_price = txt_lowest_price.lstrip("¥")
            return lowest_price
        except NoSuchElementException:
            return 0

    # 辅助函数
    def _get_start_dates(self):  # 获取后N天的日期
        _start_dates = []
        for day in range(0, self.days):
            start_date = datetime.date.today() + datetime.timedelta(days=day)
            format_start_date = start_date.strftime("%Y-%m-%d")
            _start_dates.append(format_start_date)
        return _start_dates

    def _check_nice_price(self, lowest_prices):  # 检查最低价是否满足需要
        assert len(lowest_prices) > 0, "机票价格列表长度为 %s" % len(lowest_prices)
        # 取出价格最低的一天
        all_day_lowest_price = min(lowest_prices, key=lambda item: item["price"])["price"]
        self.assertTrue(0 < all_day_lowest_price < self.nice_price, "没有合适的机票,还是等等吧,毕竟穷")

    def print_daily_lowest_price(self, daily_lowest_price, date):
        if daily_lowest_price != 0:
            print("%s 到 %s %s 的直达机票最低价为 %s" % (self.departure_city, self.arrival_city, date, daily_lowest_price))
        else:
            print("没有找到 %s 到 %s %s 的直达机票" % (self.departure_city, self.arrival_city, date))

    # 测试用例
    def find_lowest_prices_flow(self):

        # 打开页面
        self.open("http://www.ctrip.com/", 30, 30, loc_blank=self._loc_blank, is_active_window=True)

        # 获得拟查询的的所有出发日期
        start_dates = self._get_start_dates()

        # 保存每日低价集合
        lowest_prices = []

        for date in start_dates:
            # 进入机票搜索页面
            self._enter_flight_search_page()

            # 输入 出发城市
            self._input_start_city(self.departure_city)

            # 输入 到达城市
            self._input_dest_city(self.arrival_city)

            # 输入 出发时间
            self._input_depart_date(date)

            # 执行 搜索
            self._execute_search()

            # 获取 当日最低价
            daily_lowest_price = self._get_lowest_price()

            # 获取直达航线的最低价,保存到字典中
            lowest_prices.append({"date": date, "price": int(daily_lowest_price)})

            # 打印当日最低价
            self.print_daily_lowest_price(daily_lowest_price, date)

        # 检查有没有符合预期的价格
        self._check_nice_price(lowest_prices)

        # 关闭浏览器
        self.close()

    def test_find_jinan_to_haikou(self):
        self.days = 7
        self.departure_city = "济南"
        self.arrival_city = "海口"
        self.nice_price = 300
        self.find_lowest_prices_flow()

    def test_find_jinan_to_shanghai(self):
        self.days = 7
        self.departure_city = "济南"
        self.arrival_city = "上海"
        self.nice_price = 300
        self.find_lowest_prices_flow()

    def test_find_jinan_to_guangzhou(self):
        self.days = 7
        self.departure_city = "济南"
        self.arrival_city = "广州"
        self.nice_price = 300
        self.find_lowest_prices_flow()
