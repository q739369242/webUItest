#测试机屏幕分辨率,因为在无界面的操作中，不能最大化浏览器，所以要配置分辨率
x='1920'
y='1080'
#默认发现元素等待时间,值为数字类型
wait_time= 5
#谷歌chrome的驱动地址
chrome_path = '/webUItest/object/brower_drivers/chromedriver/78.0.3904.70/chromedriver.exe'
#谷歌chrome的驱动地址
Firefox_path=''
#谷歌chrome的驱动地址
ie_path=''
#mysql数据库地址h和端口号
mysql_host ='127.0.0.1'
mysql_port='3306'
#mysql数据库名
mysql_database='python_ui'
#mysql数据库账号
mysql_user ='root'
#mysql数据库密码
mysql_password ='root'
#mysql数据库编码
mysql_charset='utf8'
# 远程driver服务地址
REMOTE_DRIVER_DICT = {
    "linux": "http://192.168.1.35:4444/wd/hub",
    # "windows": "http://192.168.1.38:4444/wd/hub"
}


