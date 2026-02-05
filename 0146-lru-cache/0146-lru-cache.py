class ListNode:
    def __init__(self, key, val): #DLL
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}

        self.capacity = capacity

        #create 2 dummy nodes

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head     

    def get(self, key: int) -> int:  #u need to remove it and add it to the end again
        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]

        self.remove(node)
        self.add(node)

        return node.val

        #what happens if we add first then remove the node?

    def put(self, key: int, value: int) -> None:

        if key in self.hashMap:
            old_node = self.hashMap[key]
            self.remove(old_node)

        new_node = ListNode(key, value)
        self.hashMap[key] = new_node
        self.add(new_node)

        if len(self.hashMap) > self.capacity:
            first_node = self.head.next
            self.remove(first_node)

            del self.hashMap[first_node.key] #delete it from hashMap also


    #define function to add Node to the end of the DLL (Most recently used node is this)
    def add(self, node):
        #remember tail is just dummy not an actual node 

        #adding a node to the end of the DLL
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def remove(self,node):
        #removing a node from the LL
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# you don’t need to manually delete the node from memory.
# You just need to remove all references to it. Python will handle the rest.