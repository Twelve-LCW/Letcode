from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict() #dict+双向链表
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key,last=False)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        self.cache[key]=value
        self.cache.move_to_end(key,last=False)
        if len(self.cache)>self.capacity:
            self.cache.popitem()#去掉最后一本