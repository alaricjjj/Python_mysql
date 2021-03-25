import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',                              # 数据库主机地址
    user = 'root',                                   # 数据库用户名
    passwd = 'BlockPulse2020',                       # 数据库密码
    auth_plugin = 'mysql_native_password',            # 密码插件改变
    database = 'test'
)
mycursor = mydb.cursor()

