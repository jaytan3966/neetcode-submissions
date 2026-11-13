class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

        self.key_to_node = {}
        self.node_to_key = {}

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        if self.head.next == self.tail:
            self.head.next = node
            self.tail.prev = node

            node.prev = self.head
            node.next = self.tail
        else:
            tail_prev = self.tail.prev
            tail_prev.next = node
            node.prev = tail_prev
            node.next = self.tail
            self.tail.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]

        self.remove(node)
        self.insert(node)

        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        else:
            node = ListNode(value)
            self.key_to_node[key] = node
            self.node_to_key[node] = key

            self.insert(node)
            
            if self.capacity == 0:
                removed_node = self.head.next
                self.remove(removed_node)

                removed_key = self.node_to_key[removed_node]

                del self.key_to_node[removed_key]
                del self.node_to_key[removed_node]
            else:
                self.capacity-=1
            
            
