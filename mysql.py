"""
mysql.py
pymysql 数据库操作流程演示
"""
import  pymysql

#连接数据库
db=pymysql.connect(host='localhost',#连接的主机地址
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
#生成游标对象(操作数据库  执行sql语句)
cur=db.cursor()

#执行各种对数据库的读写操作






#关闭游标和数据库连接
cur.close()
db.close()