class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         left = 1 #min it can eat 1 banana per hour
         right = max(piles) #max it can eat highest value in pile

         #conditional binary search
         while left<right:
            mid = (left+right)//2

            if self.canEat(piles, mid, h):
                #lets try to find a value lesser
                right = mid
            else: #increase the no of bananas per hour
                left = mid+1

         return left

    def canEat(self,piles, mid, h):
        count = 0
        #here find how man hours it takes to finish the whole pile using mid hours
        for i in range(len(piles)):
            count += math.ceil(piles[i]/mid)

        if count<=h:
            return True
        return False




        