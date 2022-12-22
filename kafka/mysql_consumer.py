from kafka import KafkaConsumer
import json
import pymysql.cursors

consumer = KafkaConsumer('mysql_topic',bootstrap_servers=['localhost:9092'],group_id=None,auto_offset_reset='earliest')
for msg in consumer:
	msg1=str(msg.value,encoding="utf-8")
	data=json.loads(msg1)
	print(data)
