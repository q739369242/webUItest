from selenium import webdriver

from config.basic_config import *

class browserdriver:
    @staticmethod
    def brower_driver(d='chrome',x=x,y=y):
        '''
        
        :param s: 浏览器启动，值为chrome，Firefox和ie，或第一个字母也可以例如 c，f，i，大小写都可以已做处理
        :param x: 值为屏幕X轴大小，默认值为配置文件config中所配置的值
        :param y: 值为屏幕Y轴大小，默认值为配置文件config中所配置的值
        :return: 返回一个有配置的driver
        '''
        b = d.lower()
        if b == 'chrome'or b=='c':
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
            print('driver=chrome')
        elif b == 'firefox'or b=='f':
            driver = webdriver.Firefox(Firefox_path)
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
            print('driver=Firefox')
        elif b == 'ie'or b=='i':
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
            print('driver=Ie')
        else:
            print('没有该浏览器驱动，打开chrome')
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
        return driver

    @staticmethod
    def brower_driver_no_gui(d='chrome',x=x,y=y):
        '''
        工具方法，无界面操作
        :param s: 浏览器启动，值为chrome，Firefox和ie，或第一个字母也可以例如 c，f，i，大小写都可以已做处理
        :param x: 值为屏幕X轴大小，默认值为配置文件config中所配置的值
        :param y: 值为屏幕Y轴大小，默认值为配置文件config中所配置的值
        :return: 返回一个有配置的driver
        '''
        b = d.lower()
        if b == 'chrome'or b=='c':
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument("--window-size="+ x+','+y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
            print('driver=chrome')
        elif b == 'firefox'or b=='f':
            driver = webdriver.Firefox(Firefox_path)
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
            print('driver=Firefox')
        elif b == 'ie'or b=='i':
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
            print('driver=Ie')
        else:
            print('没有该浏览器驱动，打开chrome')
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument("--window-size=" + x + ',' + y)
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=chrome_path)
        return driver