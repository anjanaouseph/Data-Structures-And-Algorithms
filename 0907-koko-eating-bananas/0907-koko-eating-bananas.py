class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)
        res = right #it will be atleast the maximum element in the piles array

        while left<=right:
            mid = (left+right)//2
            k = 0 #total hours taken to eat with mid no of bananas
            for i in piles:
                k+= math.ceil(i/mid) #find the hours

            if k > h: #takes lots of time so increase the speed (no of bananas)
                left = mid+1
            else:
                #even if k=h, we should search for lower count value.
                res = min(mid,res) #: The variable res should be updated only when a feasible solution (k <= h) is found. You are doing this correctly in your description. However, in practice, if k == h, you might still want to try finding a lower mid if possible.
                right = mid-1

        return res