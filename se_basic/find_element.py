"""
    推荐使用 find_element_by_css_selector
"""

from selenium import webdriver

# 驱动设置
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

# 打开百度
baidu_url = 'http://www.baidu.com'
driver.get(baidu_url)

# 通过ID找到搜索框
txt_search_text = driver.find_element_by_id('kw')
txt_search_text.send_keys("find_element_by_id")

# 通过name找到搜索框
txt_search_text = driver.find_element_by_name('wd')
txt_search_text.send_keys(" find_element_by_name")

# 通过class找到搜索框
txt_search_text = driver.find_element_by_class_name('s_ipt')
txt_search_text.send_keys(" find_element_by_class_name")

# 通过tagname找到搜索框
meta = driver.find_element_by_tag_name('meta')
print(meta.get_attribute("content"))

# 通过连接地址找到元素
link_index_page = driver.find_element_by_link_text("百度首页")
link_index_page.click()

# 通过xpath找到元素
# http://www.ruanyifeng.com/blog/2009/07/xpath_path_expressions.html
txt_search_text = driver.find_element_by_xpath('//*[@id="kw"]')
txt_search_text.send_keys(" find_element_by_xpath")

# 通过css选择器找到元素 (推荐使用)
# http://www.ruanyifeng.com/blog/2009/03/css_selectors.html
txt_search_text = driver.find_element_by_css_selector('input[autocomplete=off]')
txt_search_text.send_keys(" find_element_by_css_selector")

# driver.find_element(By.CSS_SELECTOR,"input[autocomplete=off]")

driver.quit()
