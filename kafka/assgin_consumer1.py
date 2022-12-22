from kafka import KafkaConsumer,TopicPartition
import time
import uuid

display_interval = 5

consumer1 = KafkaConsumer(bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
consumer1.assign([TopicPartition('assign_topicc', 0)])
print('Consuming messagse from topic assign_topic. Press Ctrl-C to interrupt.')
display_iteration = 0
message_count = 0
partitions = set()
start_time = time.time()
while (True):
    message = next(consumer1)
    identifier = str(message.value,encoding="utf-8")
    message_count += 1
    partitions.add(message.partition)
    now = time.time()
    print('No.%i  %i messages consumed  partitions %r' % (
            display_iteration,
            message_count,

            sorted(partitions)))
    display_iteration += 1
    message_count = 0
    partitions = set()

