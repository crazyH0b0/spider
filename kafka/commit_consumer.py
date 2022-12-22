from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata
import json

class Consumer():
    def __init__(self):
        self.server = 'localhost:9092'
        self.topic = 'json_topic'
        self.consumer = None
        self.tp = None
        self.consumer_timeout_ms = 5000 
        self.group_id = 'test1' 

    def get_connect(self):
        self.consumer = KafkaConsumer('json_topicc',group_id=self.group_id,auto_offset_reset='earliest',bootstrap_servers=self.server,enable_auto_commit=False,consumer_timeout_ms=self.consumer_timeout_ms)

    def beginConsumer(self): 
        now_offset = 0 
        while True:
            for message in self.consumer:
                now_offset = message.offset
                data = message.value.decode('utf-8')
                data = json.loads(data)
                print(data)
                self.consumer.commit()
        consumer.close()

c = Consumer()
c.get_connect()
c.beginConsumer()

