"""
数据库操作
简介
数据库操作是每一门编程语言中都必不可少的操作。
使用程序操作数据库之前，需要在本地或服务器先安装数据库，比如 MySQL 数据库。
Python 中使用第三方模块 PyMySQL 操作数据库，使用前需要先进行安装。

安装 PyMySQL
pip install PyMySQL

操作流程
使用 PyMySQL 模块操作数据非常简单，步骤如下：
1.导入模块
2.连接数据库
3.创建游标对象
4.执行数据库操作
5.关闭游标对象
6.关闭数据库连接

# 导入模块
# import pymysql

连接关闭数据库
操作数据库之前，需要先进行数据库连接，和使用其它方式操作数据库方式相同。

PyMySQL 模块提供了四个连接数据库的函数名，其本质是多个变量的函数引用横等赋值，最终还是执行一个函数。
官方代码：
Connect = connect = Connection = connections.Connection

按代码的赋值顺序，推荐使用 Connect 方式连接，其它函数使用方式相同。

连接数据库函数格式及主要参数如下：
Connect(host, port, user, password, database, charset)
host：数据库主机的地址，默认为 localhost。
port：数据库的端口号，默认为 3306。
user：连接数据库所用的用户名。
password：连接数据库所用的密码。
database：要连接的数据库的名称。
charset：连接数据库时使用的字符集，默认为 utf8。
"""

# 目前本机已存在数据库 connect_test 及数据库中的数据表。
# import pymysql
#
# db_connect = pymysql.Connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='970413',
#     database='connect_test',
#     charset='utf8'
# )
# print(db_connect)
#
# db_connect.close()
# 数据库使用完毕后，需要调用 close() 方法将数据库连接对象关闭，让其断开数据库连接，避免资源泄漏。


# 获取和关闭游标对象
# 数据库连接对象创建成功后，还需要创建游标对象。
# 游标对象的作用是用来执行数据库操作，在执行完一次操作后，应调用 close() 方法将游标对象关闭。
# 在进行数据库操作时，每次数据库操作都应该建立一个游标对象，在操作完毕后将其关闭，不应使用一个游标对象进行多次操作。

# PyMySQL 模块使用 数据库连接对象.cursor() 方法获取游标对象。
# import pymysql
#
# db_connect = pymysql.Connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='970413',
#     database='connect_test',
#     charset='utf8'
# )
#
# cursor = db_connect.cursor()
# print(cursor)
# cursor.close()
# db_connect.close()

# 执行 SQL 操作
# PyMySQL 模块使用 execute() 方法执行 SQL 语句，实现数据库操作。
# 游标对象.execute(query, args=None)
# query：需要执行的 SQL 语句
# args：为 SQL 语句中的占位符提供参数，防止 SQL 注入的发生
# import pymysql
#
# db_connect = pymysql.Connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='970413',
#     database='connect_test',
#     charset='utf8'
# )

# 查询操作
# 查询单条记录
# 使用 execute 执行完毕 SQL 语句后， 可以使用 游标对象.fetchone() 方法获取一条查询结果。
# fetchone() 方法可重复使用，程序会继续向后读取查询结果。如果无查询结果可读取，则返回 None。
# cursor = db_connect.cursor()
# sql = '''select * from user'''
# cursor.execute(sql)
# for _ in range(4):
#     result = cursor.fetchone()
#     if result is not None:
#         print(result)
#     else:
#         print("No more results")
# cursor.close()
# db_connect.close()

# 查询多条记录
# 可以使用 游标对象.fetchall() 方法获取全部查询结果。
# cursor = db_connect.cursor()
# sql = '''select * from user'''
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# cursor.close()
# db_connect.close()

# 查询指定条数记录
# 可以使用 游标对象.fetchmany(size) 方法获取指定数量查询结果。
# cursor = db_connect.cursor()
# sql = '''select * from user'''
# cursor.execute(sql)
# result = cursor.fetchmany(2)
# print(result)
# cursor.close()
# db_connect.close()

#插入操作
# 执行插入操作同样使用 execute() 方法，插入数据时的 SQL 语句中的新数据，可以使用传参的方式填 入。
# 参数可以使用 元组 或 列表 形式传入。
# 在插入数据操作完成后，需要对所做的更改操作进行提交。
# 提交操作使用 数据库连接对象.commit() 方法。
# cursor = db_connect.cursor()
# sql = '''insert into user(name, age, gender, is_single) values (%s, %s, %s, %s)'''
# values = ('Will', 18, 'Female', 0)
# cursor.execute(sql, values)
# sql = '''select * from user'''
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# db_connect.commit()
# cursor.close()
# db_connect.close()

# 更新操作
# 更新操作同插入操作，只是 SQL 语句不同，操作完毕后，需要执行提交操作。
# cursor = db_connect.cursor()
# sql = '''update user set name=%s, age=%s, gender=%s, is_single=%s where id = 14'''
# values = ('方大同', 18, 'Male', 0)
# cursor.execute(sql, values)
# sql = '''select * from user'''
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# db_connect.commit()
# cursor.close()
# db_connect.close()

# 删除操作
# cursor = db_connect.cursor()
# sql = '''delete from user where age = %s'''
# value = '18'
# cursor.execute(sql, value)
# sql = '''select * from user'''
# cursor.execute(sql)
# result = cursor.fetchall()
# db_connect.commit()
# print(result)
# cursor.close()
# db_connect.close()


# 使用Python的pymysql库连接MySQL并创建users表的示例代码
import pymysql

# 数据库连接配置（需根据实际情况修改）
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'connect_test',
    'charset': 'utf8mb4'
}

# 创建表的SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    gender VARCHAR(10),
    is_single BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

try:
    # 建立数据库连接
    connection = pymysql.connect(**db_config)

    # 创建游标对象
    cursor = connection.cursor()

    # 执行创建表操作
    cursor.execute(create_table_sql)

    # 提交事务
    connection.commit()
    print("表创建成功！")

except pymysql.Error as e:
    print(f"数据库操作错误：{e}")
    # 发生错误时回滚
    connection.rollback()

finally:
    # 关闭连接
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()