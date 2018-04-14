from redis_pubsub_helper import  RedisPubSubHelper


# 发布部分
obj_pub = RedisPubSubHelper()
obj_pub.pub("it's message from channel3")