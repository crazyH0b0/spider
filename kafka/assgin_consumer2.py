from kafka import KafkaConsumer,TopicPartition
import time
import uuid

display_interval = 5

consumer2 = KafkaConsumer(bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
consumer2.assign([TopicPartition('assign_topicc', 1)])
print('Consuming messagse from topic assign_topic. Press Ctrl-C to interrupt.')
display_iteration = 0
message_count = 0
partitions = set()
start_time = time.time()
while (True):
    message = next(consumer2)
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

# 步骤
# 首先通过KafkaConsumer()方法创建一个消费者，然后通过assign()方法指定分区，然后通过while循环来获取消息，然后通过str()方法将消息转换为字符串，然后通过add()方法将分区添加到集合中，然后通过now()方法获取当前时间，然后通过print()方法打印出来。