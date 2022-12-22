from kafka import KafkaProducer
import json
import pymysql.cursors

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v:json.dumps(v).encode('utf-8'))


connect=pymysql.Connect(
	host='localhost',
	port=3306,
	user='root',
	passwd='root',
	db='webdb',
	charset='utf8'
	)
cursor=connect.cursor()
sql="select sno,sname,ssex,sage from student;"
cursor.execute(sql)
data = cursor.fetchall()
connect.commit()
for msg in data:
	res={}
	res['sno']=msg[0]
	res['name']=msg[1]
	res['sex']=msg[2]
	res['age']=msg[3]
	producer.send('iris', res)

connect.close()
producer.close()
