import mysql.connector

# conn = mysql.connector.connect(user='root',passwd='',db='test',auth_plugin='mysql_native_password')
# cursor = conn.cursor()

'''创建数据库连接'''
# mydb = mysql.connector.connect(
#     host = 'localhost',                              # 数据库主机地址
#     user = 'root',                                   # 数据库用户名
#     passwd = '',                       # 数据库密码
#     auth_plugin = 'mysql_native_password'            # 密码插件改变
# )
# print(mydb)

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
mydb = mysql.connector.connect(
    host = 'localhost',                              # 数据库主机地址
    user = 'root',                                   # 数据库用户名
    passwd = '',                       # 数据库密码
    auth_plugin = 'mysql_native_password',            # 密码插件改变
    database = 'runoob_bd'
)
mycursor = mydb.cursor()
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

'''where 条件语句'''
### 如果我们要读取指定条件的数据，可以使用 where 语句：

sql = "SELECT * FROM sites WHERE name ='RUNOOB'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

### 也可以使用通配符 %：

# sql = "SELECT * FROM sites WHERE url LIKE '%google%'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

'''排序'''

# 查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。

# 按 name 字段字母的升序排序：
# sql = "SELECT * FROM sites ORDER BY name"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# 按 name 字段字母的降序排序：
# sql = "SELECT * FROM sites ORDER BY name DESC"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

### Limit
# 如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定
# mycursor.execute("SELECT * FROM sites LIMIT 3")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

### 也可以指定起始位置，使用的关键字是 OFFSET：
# mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

'''删除记录'''
# sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录删除")

# 注意：要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件：
# sql = "DELETE FROM sites WHERE name = %s"
# na = ("stackoverflow", )
#
# mycursor.execute(sql, na)
#
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录删除")

'''更新表数据'''
### 将 name 为 Zhihu 的字段数据改为 ZH：
# sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录被修改")

### 注意：UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
# sql = "UPDATE sites SET name = %s WHERE name = %s"
# val = ("Zhihu", "ZH")
#
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录被修改")

'''删除表'''

# sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
# mycursor.execute(sql)
