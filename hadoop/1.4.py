import pymysql.cursors
#将学号为10005的学生， OperatingSystems(00004)成绩为73分这一记录写入选课表中。
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
sql = "INSERT INTO sc(Sno,Cno,Grade) VALUES('%s','%s',%d)"
# 设置数据
data = ('10005', '00004', 73)
# 执行sql语句，并获取执行结果
result = cursor.execute(sql % data)
connect.commit()
# 输出执行结果
print(result)
# 关闭数据库连接
cursor.close()
connect.close()
