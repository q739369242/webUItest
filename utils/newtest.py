# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from object.DRIVER import set_Driver_implicitly_wait


def get_element_time(driver, Parameter_By, Parameter_Value, time=3):
    """
    使用selenium 的显示等待时间和EC对象组合定位元素。
    :param driver: 浏览器驱动对象
    :param Parameter_By: selenium 中的By对象
    :param Parameter_Value: selenium 元素定位信息
    :param time: 等待时间，如果时间过后还没找到则停止程序并抛出异常。
               time default = 2 秒
    :return:通过 Parameter_By, Parameter_Value信息定位的元素。
    use template
        get_element_time(driver, By.XPATH, "//input[@name=='userName']", 2)
    """
    return get_element(driver, Parameter_By, Parameter_Value, EC.presence_of_element_located, time)


def get_element_clickable(driver, Parameter_By, Parameter_Value, time=2):
    """
    使用selenium 的显示等待时间和EC对象组合定位元素。
    :param driver: 浏览器驱动对象
    :param Parameter_By: selenium 中的By对象
    :param Parameter_Value: selenium 元素定位信息
    :param time: 等待时间，如果时间过后还没找到则停止程序并抛出异常。
               time default = 2 秒
    :return:通过 Parameter_By, Parameter_Value 信息定位的元素,并且这个元素可以点击。
    use template
        get_element_clickable(driver, By.XPATH, "//input[@name=='userName']", 2)
    """
    return get_element(driver, Parameter_By, Parameter_Value, EC.element_to_be_clickable, time)


def get_element_Send_keysAble(driver, Parameter_By, Parameter_Value, compel=False, time=2):
    """
    使用selenium 的显示等待时间和EC对象组合定位元素。
    :param driver: 浏览器驱动对象
    :param Parameter_By: selenium 中的By对象
    :param Parameter_Value: selenium 元素定位信息
    :param compel: 是否强制发送
    :param time: 等待时间，如果时间过后还没找到则停止程序并抛出异常。
               time default = 2 秒
    :return:通过 Parameter_By, Parameter_Value 信息定位的元素,并且这个元素可以输入文字。
    use template
        get_element_clickable(driver, By.XPATH, "//input[@name=='userName']",False, 2)
        get_element_clickable(driver, By.XPATH, "//input[@name=='userName']",time=2)
    """
    ele = get_element(driver, Parameter_By, Parameter_Value, EC.presence_of_element_located, time)
    if ele.tag_name == 'textarea' or ele.tag_name == 'input' or compel:
        # TODO 完整判断是否可以输入文字
        return ele
    else:
        raise Exception("这个标签不是文本框，或者文本域，\n 如需要请compel == True\n\tuse template\n\t\t"
                        "get_element_clickable(driver, By.XPATH, \"//input[@name=='userName']\",True)")


def get_elements(driver, Parameter_By, Parameter_Value, time=2):
    """
    使用selenium 的显示等待时间和EC对象组合定位元素。
    :param driver: 浏览器驱动对象
    :param Parameter_By: selenium 中的By对象
    :param Parameter_Value: selenium 元素定位信息
    :param time: 等待时间，如果时间过后还没找到则停止程序并抛出异常。
               time default = 2 秒
    :return:通过 Parameter_By, Parameter_Value信息定位的多个元素。
    use template
        get_element_time(driver, By.XPATH, "//input[@name=='userName']",EC.element_to_be_clickable, 2)
    """
    driver.implicitly_wait(time)
    # elements = None
    try:
        elements = WebDriverWait(driver, time).until(
            EC.visibility_of_all_elements_located((Parameter_By, Parameter_Value)))
    except Exception:
        E_mag = dict(url=driver.current_url,
                     time=time,
                     by=Parameter_By,
                     val=Parameter_Value)
        raise Exception("在 %(url)s 页面 %(time)s秒 内没找到 %(by)s == %(val)s 的元素." % E_mag)
    finally:
        set_Driver_implicitly_wait(driver)
    return elements


def get_element(driver, Parameter_By, Parameter_Value, get_element_def, time=2 ):
    """
    使用selenium 的显示等待时间和EC对象组合定位元素。
    :param driver: 浏览器驱动对象
    :param Parameter_By: selenium 中的By对象
    :param Parameter_Value: selenium 元素定位信息
    :param get_element_def: EC 对象中的方法
    :param time: 等待时间，如果时间过后还没找到则停止程序并抛出异常。
               time default = 2 秒
    :return:通过 Parameter_By, Parameter_Value信息定位的元素。
    use template
        get_element_time(driver, By.XPATH, "//input[@name=='userName']",EC.element_to_be_clickable, 2)
    """
    driver.implicitly_wait(time)
    try:
        element = WebDriverWait(driver, time).until(get_element_def((Parameter_By, Parameter_Value)))
    except Exception:
        E_mag = dict(url=driver.current_url,
                     time=time,
                     by=Parameter_By,
                     val=Parameter_Value)
        raise Exception("在 %(url)s 页面 %(time)s秒 内没找到 %(by)s == %(val)s 的元素." % E_mag)
    finally:
        set_Driver_implicitly_wait(driver)
        # 页面滚动到元素位置
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element

