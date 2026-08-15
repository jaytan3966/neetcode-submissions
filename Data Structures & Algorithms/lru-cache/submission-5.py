class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.h = {}
        self.cap = capacity

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        if prev and nxt:
            prev.next = nxt
            nxt.prev = prev
        elif prev:
            prev.next = None
            self.tail = prev
        elif nxt:
            nxt.prev = None
            self.head = nxt
        else:
            self.head = None
            self.tail = None
        return node

    def add(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def get(self, key: int) -> int:
        val = -1
        if key in self.h:
            node = self.h[key]
            val = node.val
            self.add(self.remove(node))
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            node = self.h[key]
            node.val = value
            self.add(self.remove(node))
        else:
            if self.cap == 0:
                del self.h[self.head.key]
                self.remove(self.head)
                
            node = ListNode(key, value)
            self.h[key] = node
            self.add(node)
            self.cap-=1
            

class ListNode():
    def __init__(self, k=0, v=0, prev=None, nxt=None):
        self.key = k
        self.val = v
        self.prev = prev
        self.next = nxt