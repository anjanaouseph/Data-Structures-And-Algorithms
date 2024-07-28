class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        maxLeft = height[i]
        maxRight = height[j]
        res = 0
        while i<j:
            if maxLeft < maxRight:#move along the direction of lower pointer to maximize
            #the minimum boundary
                i+=1 #move to next pointer
                count = min(maxLeft,maxRight)-height[i] #use the formula to find units of water
                if count>0: #if positive >0 then add to the total units counter
                    res+=count
                maxLeft = max(maxLeft,height[i])
            else:
                j-=1
                count = min(maxLeft,maxRight)-height[j]
                if count>0:
                    res+=count
                maxRight = max(maxRight,height[j])
        return res

        #there is a method easier with o(n) time complexity and o(n) space complexity using hashmap. Try to do that.