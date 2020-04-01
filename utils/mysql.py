import pymysql
from config.basic_config import *

def database(dbtype='m'):
    '''
    :param dbname: 值为m，mysql，o，oracle，连接对应的数据库
    :return: 返回一个已经连接的数据库
    '''
    dbname=dbtype.lower()
    if dbname== 'mysql' or dbname=='m':
        db_connection = pymysql.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database,
            charset=mysql_charset
        )
    # elif dbname== 'o'or dbname=='oracle':
    #     db_connection = pymysql.connect(
    #         host=oracle_host,
    #         user=oracle_user,
    #         password=oracle_password,
    #         database=oracle_database,
    #         charset=oracle_charset
    #     )
    else:
        print("没有该数据库，请选择mysql,参数为 m ")

    return db_connection