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
sql = "UPDATE course SET Credit = %d " \
      "WHERE Cno = '%s'"
# 设置数据
data = (5, '00001')
# 执行sql语句，并获取执行结果

result = cursor.execute(sql % data)
# 提交事务
connect.commit()

# 查看执行结果
print(result)
# 关闭数据库连接
cursor.close()
connect.close()
