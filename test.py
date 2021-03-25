import mysql.connector

# conn = mysql.connector.connect(user='root',passwd='BlockPulse2020',db='test',auth_plugin='mysql_native_password')
# cursor = conn.cursor()

'''创建数据库连接'''
mydb = mysql.connector.connect(
    host = 'localhost',                              # 数据库主机地址
    user = 'root',                                   # 数据库用户名
    passwd = '铭文密码',                       # 数据库密码
    auth_plugin = 'mysql_native_password'            # 密码插件改变
)
print(mydb)

'''创建数据库'''

# mycursor = mydb.cursor()

### 创建数据库
# mycursor.execute('CREATE DATABASE runoob_bd')

### 输出所有数据库列表
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

### 可以直接连接数据库，如果数据库不存在，则会输出错误信息
# mydb = mysql.connector.connect(
#     host = 'localhost',                              # 数据库主机地址
#     user = 'root',                                   # 数据库用户名
#     passwd = '',                       # 数据库密码
#     auth_plugin = 'mysql_native_password',            # 密码插件改变
#     database = 'runoob_bd'
# )

'''创建数据表'''
### 创建数据表使用 "CREATE TABLE" 语句，创建数据表前，需要确保数据库已存在，以下创建一个名为 sites 的数据表：
# mydb = mysql.connector.connect(
#     host = 'localhost',                              # 数据库主机地址
#     user = 'root',                                   # 数据库用户名
#     passwd = '',                       # 数据库密码
#     auth_plugin = 'mysql_native_password',            # 密码插件改变
#     database = 'runoob_bd'
# )
# mycursor = mydb.cursor()
### 建立一个TABLE
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

### 显示TABLE内容
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

'''主键设置'''

# 创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY" 语句来创建一个主键，主键起始值为 1，逐步递增。
# 如果我们的表已经创建，我们需要使用 ALTER TABLE 来给表添加主键：
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 如果你还未创建 sites 表，可以直接使用以下代码创建。
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

'''插入数据'''
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
#
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")

'''批量插入'''
### 批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")

### 如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码：
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 条记录已插入, ID:", mycursor.lastrowid)

'''查询数据'''
### 获取所有数据
# mycursor.execute("SELECT * FROM sites")
#
# myresult = mycursor.fetchall()     # fetchall() 获取所有记录
#
# for x in myresult:
#     print(x)

### 也可以读取指定的字段数据：
# mycursor.execute("SELECT name, url FROM sites")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

