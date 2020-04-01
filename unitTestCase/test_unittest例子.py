from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import unittest, time, re,os
import HTMLTestRunner #引入 HTMLTestRunner 包
def make_report():
    project_path= os.path.dirname(os.getcwd())
    file_path= project_path+"/report/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    fp =open(file_path+"123.html","wb")
    return fp

class Baidu(unittest.TestCase):
    #因为setup和teardown，和case是一起使用的，有多少case就会执行多少次，这样造成浏览器多次打开和关闭
    #使用修饰器可以解决，因为只会执行一次，这样就可以在浏览器一直操作了，setup和teardown都可以不用存在了
    @classmethod
    def setUpClass(cls):
        u"""百度搜索"""
        path="/liang/chromedriver/78.0.3904.70/chromedriver.exe"
        cls.driver = webdriver.Chrome(path)
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://www.baidu.com/"
        cls.verificationErrors = []
        cls.accept_next_alert = True
    #用于跳过仅后的case
    #@unittest.skip("Baidu")
    def test_baidu_search(self):
        # 下面用来写用例的标题，可以直接在html报告中显示出来
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        

    def test_jd_set(self):
        driver = self.driver
        #进入搜索设置页
        driver.get("http://jd.com")
        search_element =  driver.find_element_by_id("key")
        search_element.send_keys("电脑")
        time.sleep(3)
        search_element.send_keys(Keys.RETURN)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        #cls.assertEqual([], cls.verificationErrors)

if __name__ == "__main__":
    #运行全部用例
    #unittest.main()
    #实例一个容器，运行其中一个用例，
    suite=unittest.TestSuite()
    suite.addTest(Baidu("test_jd_set"))
    html_file=make_report()
    HTMLTestRunner.HTMLTestRunner(html_file).run(suite)