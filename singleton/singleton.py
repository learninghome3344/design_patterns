# -- coding:utf-8 --

# https://www.bilibili.com/video/BV1234y1m7Tr?spm_id_from=333.999.0.0

import configs
import threading


# 程序中任何地方使用Util类实例化出来的时候都是同一个对象！！！
class Util(object):

    _lock = threading.Lock()

    def __init__(self, host, port):
        self.host = host
        self.port = port

    # 重写__new__方法实现单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._lock:
                cls._instance = object.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    u1 = Util(configs.HOST, configs.PORT)
    u2 = Util(configs.HOST, configs.PORT)
    u3 = Util(configs.HOST, configs.PORT)

    print(id(u1), id(u2), id(u3))
    print(id(u1) == id(u2))
    print(id(u2) == id(u3))

