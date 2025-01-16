class Solution:

    def __init__(self, w: List[int]):
        #use init function to create the prefix sum

        self.prefix = []

        self.total = 0

        for i in w:
            self.total += i
            self.prefix.append(self.total)
        

    def pickIndex(self) -> int:
        #use this to generate the random function from 0 to total-1
        #apply binary search
        target = random.uniform(0, self.total) #random no generator from [0,tota)
        left = 0
        right = len(self.prefix)

        while left < right:
            mid = (left + right)//2

            if target < self.prefix[mid]:
                right = mid
            else:
                left = mid+1

        return left


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()