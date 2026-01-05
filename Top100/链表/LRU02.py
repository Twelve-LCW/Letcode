class Node:
    __slots__ = 'prev', 'next', 'key', 'value'
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dummy=Node()
        self.dummy.next=self.dummy
        self.dummy.prev=self.dummy
        self.key_to_node={}

    # 获取 key 对应的节点，同时把该节点移到链表头部
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:
            return None
        node=self.key_to_node[key]
        self.remove(node)
        self.put_front(node)
        return node
    
    def remove(self,x:Node) -> None:
        x.next.prev=x.prev
        x.prev.next=x.next
    
    def put_front(self,x:Node) ->None:
        x.prev=self.dummy
        x.next=self.dummy.next
        x.prev.next=x
        x.next.prev=x
    
    def get(self, key: int) -> int:
        node=self.get_node(key)
        return node.value if node else -1
    
    def put(self, key: int, value: int) -> None:
        node=self.get_node(key)
        if node:
            node.value=value
            return
        self.key_to_node[key]=node=Node(key,value)
        self.put_front(Node)
        if len(self.key_to_node)>self.capacity:
            back_node=self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)

        
