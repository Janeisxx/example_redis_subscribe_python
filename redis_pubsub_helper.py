
'''
发布订阅的实现:
逻辑:订阅频道后,频道发消息就可以收到
    未订阅频道,频道发消息收不到

    1.创建包含发布和订阅方法的类
    2.实例化订阅对象,"等待"接收频道消息,运行
    3.实例化发布对象,发布消息,运行
    4.第3步后,第2步收到发布消息
根据逻辑:2,3运行顺序不能反
'''

from redis import Redis

class RedisPubSubHelper():
    def __init__(self):
        self.__redis = Redis(host='localhost',
                             port=6379)
        # 订阅和发布设置为同一个频道
        self.pub_channel = 'channel3'
        self.sub_channel = 'channel3'

    # 定义发布方法
    def pub(self,msg):
        # 直接用redis实例来publish
        self.__redis.publish(self.pub_channel,msg)
        return True
    # 定义订阅方法
    def sub(self):
        # 实现订阅要创建一个redis的"订阅对象实例"
        sub_obj = self.__redis.pubsub()
        sub_obj.subscribe(self.sub_channel)
        sub_obj.parse_response()
        return sub_obj

    '''
             def pubsub(self, **kwargs):
         """
         Return a Publish/Subscribe object. With this object, you can
         subscribe to channels and listen for messages that get published to
         them.
         """
    '''











