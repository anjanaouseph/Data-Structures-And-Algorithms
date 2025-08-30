from collections import defaultdict

class TimeMap:

    def __init__(self):
        #using defaultdict
        self.store = defaultdict(list) #key : value, timesatmp, can use default dict as well
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])        

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        values = self.store[key] #if no key returns []
        left = 0
        right = len(values)-1

        while left <= right:
            mid = (left+right)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0] #this will be the closest value
                left = mid+1
            else:
                right = mid-1

        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)