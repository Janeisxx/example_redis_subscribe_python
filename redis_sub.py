
from redis_pubsub_helper import  RedisPubSubHelper
#    订阅部分
obj = RedisPubSubHelper()
redis_pub = obj.sub()


#死循环 ,要一直等待接收消息,
while True:
    print('已订阅channel3频道,等待接收消息')
    msg = redis_pub.parse_response()
    print("从channel3频道接收到消息内容为:%s"%msg)
