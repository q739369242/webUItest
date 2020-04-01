
def set_mysql_config(env):
    if env == "dev":
        db_config = {
            'host': '192.168.1.35',
            'user': 'admin',
            'passwd': '123456',
            'db': 'python_ui',
            "port": 3306,
            'charset': 'utf8'
        }
    if env == "pro":
        db_config = {
            'host': '192.168.1.35',
            'user': 'admin',
            'passwd': '123456',
            'db': 'python_ui',
            "port": 3306,
            'charset': 'utf8'
        }
    return db_config
