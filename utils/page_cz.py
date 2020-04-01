from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from config.basic_config import *


class pagecz(object):
    def __init__(self, driver):
        self._driver = driver

    def get_element(self,
                     Parameter_By, Parameter_Value,
                     timeout=None,
                     wait_type="visibility",
                     when_failed_close_browser=True):
        """
        :param Parameter_By: selenium 中的By对象   例如By.id
        :param Parameter_Value: selenium 元素定位信息 例如 id的值
        :param timeout: 默认值为None，但是为None时，将会取配置文件中的超时时间配置
        :param wait_type: 等待的类型，支持两种等待方式，一种是可见等待visibility，另外一种是存在等待presence
        :param when_failed_close_browser: 当元素定位失败时，浏览器是否关闭
        :return: 返回定位的元素
        """
        locator=(Parameter_By, Parameter_Value)
        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_element_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(locator))


    def get_elements(self,
                      Parameter_By,
                      Parameter_Value,
                     timeout=None,
                     wait_type="visibility",
                     when_failed_close_browser=True):
        """
        :param Parameter_By: selenium 中的By对象   例如By.id
        :param Parameter_Value: selenium 元素定位信息 例如 id的值
       
        :param timeout: 默认值为None，但是为None时，将会取配置文件中的超时时间配置
        :param wait_type: 等待的类型，支持两种等待方式，一种是可见等待visibility，另外一种是存在等待presence
        :param when_failed_close_browser: 当元素定位失败时，浏览器是否关闭
        :return: 返回定位的元素们
        """
        locator = (Parameter_By, Parameter_Value)

        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_all_elements_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_all_elements_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(locator))



    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=wait_time)

        else:
            return WebDriverWait(driver=self._driver, timeout=wait_time)
