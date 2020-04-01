from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json
import unittest

path = 'd:/liang/chromedriver/78.0.3904.70/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.implicitly_wait(10)

class jingdong(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_jingdong(self):
        # 要有一个循环来控制登录状态，判断登录是否成功
        loop_status = True
        while loop_status:
            #save_cookies_to_file()
            # 检验cookies是否生效
            login_status = check_cookies()
            if login_status == True:
                loop_status = False
            else:
                login()
                # 跳转到商品信息页面
        to_goods_page()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        driver.quit()

# 登录功能
def login():

    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("13076636096")
    driver.find_element_by_id("nloginpwd").send_keys("08668699liang")
    driver.find_element_by_id("loginsubmit").click()

    # 要保存cookies到文件中
    save_cookies_to_file()


# 把cookies保存到文件中
def save_cookies_to_file():
    # 获取存储cookies的文件夹
    file_path = get_cookies_dir()
    # 获取cookies
    cookies = driver.get_cookies()
    # 存储cookies到文件中
    with open(file_path + "jd.cookies", "w") as f:
        json.dump(cookies, f)


def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    #判断路径有没有file_path这个目录
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


def check_cookies():
    # 设置一个登录状态，初始值是未登录
    login_status = False

    # 将cookies信息保存到driver中
    driver = save_cookies_to_driver()

    # 进行跳转链接的检测
    driver.get("https://order.jd.com/center/list.action")
    current_url = driver.current_url
    if current_url == "https://order.jd.com/center/list.action":
        login_status = True
        return login_status
    else:
        return login_status


# 保存cookies信息到driver中,
# 注意读取文件的内容为空或者直接连文件都没有时，会报错
def save_cookies_to_driver():
    cookies_file = get_cookies_file()
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 这里必须清除掉旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
        # expiry不是整数报错
        expiry = cookie.get("expiry")
        if isinstance(expiry, float):
            cookie["expiry"] = int(expiry)
        driver.add_cookie(cookie)
    return driver


def get_cookies_file():
    return get_cookies_dir() + "jd.cookies"


def to_goods_page():
    # 首先把页面放在首页上
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_css_selector(".cate_menu_lk[href*='//diannao.jd.com/']")
    # 鼠标悬停在电脑上
    ActionChains(driver).move_to_element(computer_element).perform()
    # 点击笔记本
    time.sleep(2)
    driver.find_element_by_css_selector(".cate_detail_con_lk[href*= \"//list.jd.com/list.html?cat=670,671,672\"]").click()
    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_url
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)
    # 点击thinkpad
    driver.find_element_by_css_selector("#brand-11518 a[href*=\"_品牌_ThinkPad \"]").click()
    # 点击7000以上
    driver.find_element_by_css_selector(".J_valueList a[href*=\"7000以上\"] ").click()
    # 点击评论数
    driver.find_element_by_xpath("//*[@id=\"J_filter\"]/div[1]/div[1]/a[3]").click()
    # 点击第一款电脑
    driver.find_element_by_xpath("//*[@id=\"plist\"]/ul/li[1]/div/div[1]/a/img").click()
    # 切换句柄
    notebook_handler = driver.current_window_handle
    # 这里必须重新获取一下所有的句柄，因为这里已经有3个窗口了
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notebook_handler:
            driver.switch_to.window(handle)
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    # 解析所有的标签
    info_elements = driver.find_elements_by_class_name("Ptable-item")

    # 有一个list存储最终的结果
    result_list = []
    # 标签一个一个解析
    for info_element in info_elements:
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    # 保存这些信息到文件中
    save_goods_info(result_list)


def get_info_element_dict(info_element):
    # 拿到第一列的信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机信息中的key值
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # 计算机信息中的value值
    computer_info_values = info_element.find_elements_by_xpath("dl//dd[not(@class='Ptable-tips')]")

    # 存储计算机信息的key和value
    key_and_value_dict = {}

    # 存储所有的计算机组成信息
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text

    parts_dict[computer_part.text] = key_and_value_dict

    return parts_dict


def save_goods_info(info_list):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/goods_infos/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open(file_path + "computer.infos", "a", encoding="utf-8") as f:
        f.write(str(info_list))
        print(str(info_list))


if __name__ == "__main__":
    unittest.main()



