class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #she can eat from 1 till len(piles) bananas

        left = 1
        right = max(piles)

        def eatingSpeed(mid):
            count = 0
            for i in range(len(piles)):
                count += ceil(piles[i]/mid)

            return count

        while left <= right:
            mid = left + (right-left)//2

            if eatingSpeed(mid) <= h:
                right = mid-1
            else:
                left = mid+1

        return left    