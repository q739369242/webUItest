from object.brower_driver import browserdriver
from utils.page_cz import pagecz
d=browserdriver.brower_driver()
d=pagecz.get_element()
d.save_screenshot()