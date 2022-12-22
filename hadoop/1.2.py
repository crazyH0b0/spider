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
sql = "SELECT student.Sno,Sname,Sdept,course.Cno,Cname,Grade " \
      "FROM student,course,sc " \
      "WHERE student.Sno = sc.Sno AND course.Cno = sc.Cno AND Grade > %d"
# 设置数据
data = (85, )
# 执行sql语句
cursor.execute(sql % data)
# 获取数据
print("共有%s条记录" % cursor.rowcount)
for row in cursor.fetchall():
    print("学号：%s\t姓名：%s\t系别：%s\t课程号：%s\t课程名：%s\t成绩：%d" % row)
# 关闭数据库连接
cursor.close()
connect.close()
