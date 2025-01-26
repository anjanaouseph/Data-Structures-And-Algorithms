class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        #hashmap for O(1) get and put else it will be O(n)
        self.cache = {} #hashmap tp store key and values as Nodes

        #initialize dummy nodes for DLL
        self.left = self.right = Node(0,0)

        #connect next and prev pointers
        self.left.next = self.right
        self.right.prev = self.left

    #remove the node from the LL and add it to the right side
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    #insert node to the linkedlist, at the rightmost end as thats the MRU
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node
        

    def get(self, key: int) -> int:
        key_val = -1
        if key in self.cache:
            self.remove(self.cache[key])#delete the node from DLL
            self.insert(self.cache[key])#add to right side of the DLL its MRU
            key_val = self.cache[key].val       
        return key_val
        
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(node)
            self.cache[key] = node
        else:
            self.insert(node)
            self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)