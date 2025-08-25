class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left<right:
            mid = left+(right-left)//2

            if self.min_integer(mid, h, piles):
                right = mid
            else:
                left = mid+1
        return left


    def min_integer(self,k, h, piles):
        count = 0
        for i in range(len(piles)):
            count += math.ceil(piles[i]/k)

        if count<=h:
            return True
        return False