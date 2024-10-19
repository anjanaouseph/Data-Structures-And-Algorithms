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
                #dont update res when it takes more than h hours, because say mid is 3, it will take 10 hours, then res will be set as 3 even if its the incorrect ans (correct ans is 4 hrs.)
            else:
                #even if k=h, we should search for lower count value else you will get some lower no which may be the wrong answer like say 6 but (even though it takes only 7 hrs) still 4 is the optimal ans even though it takes 8 hrs 
                res = min(mid,res) 
                right = mid-1
#The variable res should be updated only when a feasible solution (k <= h) is found. You are doing this correctly in your description. However, in practice, if k == h, you might still want to try finding a lower mid if possible.

        return res