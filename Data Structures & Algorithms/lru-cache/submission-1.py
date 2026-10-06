class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove_node(node)
        self.insert_next_dummy_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove_node(node)
            self.insert_next_dummy_head(node)
        else:
            if len(self.map) == self.capacity:
                lru = self.dummy_tail.prev
                self.remove_node(lru)
                del self.map[lru.key]
            new_node = Node(key, value)
            self.insert_next_dummy_head(new_node)
            self.map[key] = new_node
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_next_dummy_head(self, node):
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

