
from utils.mysql import *
try:
    # db_connection  连接数据库
    db_connection=database()
    #创建游标
    cursor=db_connection.cursor()
    print(cursor)
    #书写sql语句
    #sql="select id,ssc from ssc where id='1' "
    sql='select id from python_ui.ssc  order by id DESC'


    #执行sql
    cursor.execute(sql)

    # fetchone() ：返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
    # fetchall() ：返回所有个元组，即返回多个记录(rows),如果没有结果 则返回 ()
    # fetchmany(x)：获取前n行数据，row_2 = cursor.fetchmany(3)  获取前三行数据，元组包含元组
    '''采用时间倒叙，orderby 时间 desc +fetchone(), 就可以获得最新数据'''
    result= cursor.fetchmany(3)

    #提交sql  更新数据（insert，update，delete）的操作都需要 commit
    db_connection.commit()

    #判断类型
    print(type(result))
    print(result[0][0])
finally:
    #关闭游标
    cursor.close()
    #关闭数据库
    db_connection.close()