class ListNode:
    def __init__(self, key, val): #DLL
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]

        self.remove(node)
        self.add(node)#add to MRU end of list
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        #a) if existing node
        if key in self.hashMap:
            old_node = self.hashMap[key]
            old_node.val = value
            self.remove(old_node)
            self.add(old_node)
            
        else:
            #we are inserting a existing node
            
            new_node = ListNode(key,value)
            new_node.key = key
            new_node.val = value
            self.add(new_node) #add to MRU
            self.hashMap[key] = new_node #update hashMap
            if len(self.hashMap) > self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.hashMap[lru_node.key]

    def remove(self, node: Node):
        
        next_node = node.next
        prev_node = node.prev

        next_node.prev = prev_node
        prev_node.next = next_node

        node.next = None
        node.prev = None
        #will be removed by garbage collector
        #Breaking references helps GC reclaim memory sooner


    def add(self, node: Node):

        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value);