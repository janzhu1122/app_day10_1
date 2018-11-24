from selenium.webdriver.common.by import By

from Base.page import Page

from Base.get_driver import get_driver


# 实例化page类
page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

# 点击我
page_obj.get_home_page_obj().click_my_btn()
# 点击已有账户去登录
page_obj.get_sign_page_obj().click_exits_account()
# 登陆操作
page_obj.get_login_page_obj().login("1444444444", "159357li111")

# 每个返回页面对象方法 返回的页面实例化对象  页面继承Base
print(page_obj.get_home_page_obj().get_toast("不存在"))