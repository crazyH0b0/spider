import sys
import json
import pandas as pd
import os
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
 
KAFKA_HOST = "localhost" #服务器地址
KAFKA_PORT = 9092    #端口号
KAFKA_TOPIC = "iris"  #topic
print(os.getcwd()+'\\score.csv')
data=pd.read_csv(os.getcwd()+'\\score.csv', delim_whitespace=True)
key_value=data.to_json()

class Kafka_producer():
    def __init__(self, kafkahost, kafkaport, kafkatopic, key):
      self.kafkaHost = kafkahost
      self.kafkaPort = kafkaport
      self.kafkatopic = kafkatopic
      self.key = key
      self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
          kafka_host=self.kafkaHost,
          kafka_port=self.kafkaPort)
       )
    def sendjsondata(self, params):
         try:
            parmas_message = params
            producer = self.producer
            producer.send(self.kafkatopic, key=self.key, value=parmas_message.encode('utf-8'))
            producer.flush()
         except KafkaError as e:
             print(e)
 
 
class Kafka_consumer():
    def __init__(self, kafkahost, kafkaport, kafkatopic, groupid,key):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.key = key
        self.consumer = KafkaConsumer(self.kafkatopic, group_id=self.groupid,
           bootstrap_servers='{kafka_host}:{kafka_port}'.format(
           kafka_host=self.kafkaHost,
           kafka_port=self.kafkaPort)
         )
    def consume_data(self):
        try:
            for message in self.consumer:
                yield message
        except KeyboardInterrupt as e:
                print(e)
 
def sortedDictValues(adict):
    items = adict.items()
    items=sorted(items,reverse=False)
    return [value for key, value in items]
 
def main(xtype, group, key):
    if xtype == "p":
        # 生产模块
        producer = Kafka_producer(KAFKA_HOST, KAFKA_PORT, KAFKA_TOPIC, key)
        print("===========> producer:", producer)
        params =key_value        
        producer.sendjsondata(params)
    if xtype == 'c':
        # 消费模块
        consumer = Kafka_consumer(KAFKA_HOST, KAFKA_PORT, KAFKA_TOPIC, group,key)
        print("===========> consumer:", consumer)
        message = consumer.consume_data()
        for msg in message:
            msg=msg.value.decode('utf-8')
            python_data=json.loads(msg) ##字符串转换成字典
            key_list=list(python_data)
            test_data=pd.DataFrame()
            for index in key_list:                
                if index=='Name':
                    a1=python_data[index]                    
                    data1 = sortedDictValues(a1)                    
                    test_data[index]=data1
                else:
                    a2 = python_data[index]
                    data2 = sortedDictValues(a2)
                    test_data[index] = data2
            print(test_data)
 
if __name__ == '__main__':
    main(xtype='p',group='py_test',key=None)
    main(xtype='c',group='py_test',key=None)