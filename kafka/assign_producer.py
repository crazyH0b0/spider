from kafka import KafkaProducer,TopicPartition
import time
import uuid


producer = KafkaProducer(bootstrap_servers='localhost:9092')
display_interval = 5

print('Producing messages to topic assign_topic. Press Ctrl-C to interrupt.')
display_iteration = 0
message_count = 0
start_time = time.time()
while True:
    identifier = str(uuid.uuid4())  
    producer.send('assign_topicc', identifier.encode('utf-8'))  
    message_count += 1
    now = time.time()
    if now - start_time > display_interval:
        print('No.%i iter %i messages produced at %.0f messages / second' % (
            display_iteration,
            message_count,
            message_count / (now - start_time)))
        display_iteration += 1
        message_count = 0
        start_time = time.time()
#步骤
#首先通过KafkaProducer()方法创建一个生产者，然后通过while循环生成uuid，设置编码格式为utf-8，然后通过send()方法将数据发送到kafka集群中的assign_topic主题