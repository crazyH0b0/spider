import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='webdb',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
# 设置sql语句
sql = "DELETE FROM student WHERE Sno = '%s'"
# 设置数据
data = ('10003',)
# 执行sql语句，并获取执行结果
result = cursor.execute(sql % data)
connect.commit()
# 输出执行结果
print(result)
# 关闭数据库连接
cursor.close()
connect.close()
