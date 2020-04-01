import json
def save_cookies_to_driver(driver,url,get_cookies_file):
    '''
    
    :param driver: 传入一个浏览器驱动
    :param url: 测试地址，用于清除原有cookies
    :param get_cookies_file: cookies文件存放的地址，用于读取，然后写入driver
    :return: 
    '''
    cookies_file = get_cookies_file
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 这里必须清除掉旧的cookies
    driver.get(url)
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
        # expiry不是整数报错
        expiry = cookie.get("expiry")
        if isinstance(expiry, float):
            cookie["expiry"] = int(expiry)
        driver.add_cookie(cookie)
    return driver