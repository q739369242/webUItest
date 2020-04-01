from utils.brower_driver import *
from utils.page_cz import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
try:
    driver= browserdriver.brower_driver()
    driver.get("https://www.baidu.com")
    baidusshezhi=(By.CSS_SELECTOR,'.pf[href=\'http://www.baidu.com/gaoji/preferences.html\']')
    shezhi=pagecz(driver).find_element(*baidusshezhi)
    ActionChains(driver).move_to_element(shezhi).perform()
    sousuoshezhi=(By.CSS_SELECTOR,'.setpref')
    sousuo=pagecz(driver).find_element(*sousuoshezhi)
    ActionChains(driver).move_to_element(sousuo).perform()
    sousuo.click()
    tiaoshu=(By.NAME,'NR')
    sousuotiaoshu=pagecz(driver).find_element(*tiaoshu)
    Select(sousuotiaoshu).select_by_index(1)
    '''
    <select name="NR" id="nr">
    <option value="10" selected="">每页显示10条</option>
    <option value="50">每页显示50条</option>
    <option value="20">每页显示20条</option>
    </select>
    
    option型下拉选择框:
    #导入工具类，
    from selenium.webdriver.support.ui import Select
    #进行元素定位
    tiaoshu=(By.NAME,'NR')
    sousuotiaoshu=pagecz(driver).find_element(*tiaoshu)
    #再选择选项
    Select(sousuotiaoshu).select_by_index(index，例如0，0为第一个选项)    　　  # 以index属性值来查找匹配的元素并选择；
    Select(sousuotiaoshu).select_by_value(value ,例如'50')  # 以value属性值来查找该option并选择；
    Select(sousuotiaoshu).select_by_visible_text(text 例如'每页显示50条')  # 以text文本值来查找匹配的元素并选择；
    '''
finally:
    time.sleep(5)
    driver.quit()