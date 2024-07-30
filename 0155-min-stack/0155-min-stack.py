class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] #to keep track of min values
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minimum)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop() #if we are popping an element from main stack say 1
        #it needs to be popped from minstack as well to keep both in sync, else it
        #will return what was popped out from main stack which is wrong!
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()