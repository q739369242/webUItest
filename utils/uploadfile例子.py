from utils.brower_driver import *
from utils.page_cz import pagecz
from utils.mkdir_file import *
from utils.savecookies_todriver import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utils.uploadfille import *
import time


try:
    driver = browserdriver.brower_driver()
    driver.get('https://www.baidu.com')
    d=pagecz(driver)
    # denglu=(By.CSS_SELECTOR,'#u1 a[name="tj_login"]')
    # pagecz(driver).find_element(*denglu).click()
    # username=(By.ID,'TANGRAM__PSP_10__footerULoginBtn')
    # pagecz(driver).find_element(*username).click()
    # username=(By.ID,'TANGRAM__PSP_10__userName')
    # pagecz(driver).find_element(*username).send_keys('a3348336')
    # password=(By.ID,'TANGRAM__PSP_10__password')
    # pagecz(driver).find_element(*password).send_keys('08668699liang')
    # driver.find_element_by_css_selector('#TANGRAM__PSP_10__submit').click()
    #c=driver.get_cookies()
    # mk_dir_write_content(filename_filetype='baidu.cookies',writer_type='j',writer_content=c,open_mode='w',file_path='d://')
    save_cookies_to_driver(driver,url='https://www.baidu.com',get_cookies_file='d://baidu.cookies')
   #百度文库地址
    driver.get('https://wenku.baidu.com/new?fr=home')


    #获取上传文件标签
    f1 = driver.find_element_by_css_selector('#global-uploader-btn')
    # #仅用来检查，多余可删除
    #i1 = driver.find_element_by_xpath(u"//input[@name='articleTitlePic']")
    UpLoad_File(f1, "e:\\timg.jpg")#一定要是本地地址

finally:
    time.sleep(5)
    driver.quit()