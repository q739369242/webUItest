
from utils.brower_driver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.page_cz import *

import os

try:

    driver=browserdriver.brower_driver()
    driver.get("https://www.jd.com")
    #find_element的元组参数

    #调用方法 类（驱动）+find_element函数（参数,该参数一定要带*）
    a=pagecz(driver).find_element(By.CSS_SELECTOR,".cate_menu_lk[href*='//diannao.jd.com/']")
    ActionChains(driver).move_to_element(a).perform()
finally:
    driver.save_screenshot(os.getcwd() + 'asd.png')
    driver.quit()