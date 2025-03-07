class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
           self.map[key] = []
        self.map[key].append([value,timestamp])  

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key,[])#if doesnt exist initialize with []
        l , r = 0, len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp: #this way we get the closest value
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1 #ignore values greater than timestamp, we only need values closest to or equal to the timestamp.
        return res     


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)