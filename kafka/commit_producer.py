from kafka import KafkaProducer
import json # 引入模块
import os


data = open(os.getcwd()+'\\data.json')
# 转换为python对象
strJson = json.load(data)
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v:json.dumps(v).encode('utf-8'))
producer.send('json_topic', strJson)
producer.close()

