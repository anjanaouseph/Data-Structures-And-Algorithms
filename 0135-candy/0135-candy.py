class Solution:
    def candy(self, ratings: List[int]) -> int:
        #brute force Each iteration scans the entire array and may update up to n positions. Since we can have up to n iterations in the worst case, the total time complexity becomes O(n²).
        #In the brute force approach, each pass propagates constraints by at most one step, so we need at most O(n) passes. Since each pass takes O(n), the total time complexity is O(n²).
        #and a single pass approach fails when there is mountain like symmetry. 
        #eg: 1 2 3 4 3 2 1, if i use my logic of if curr > left then do left candies + 1 else 1+1,
        # then it breaks.
        # 1 2 3 4 3 2 1
        # 1 2 3 4 2 3 1.  2,3 is wrong here there is a breach
        # so single pass will breach the constraints so we need to use a double pass approach as we can't for sure say how many candies will the right element get as thats not yet fixed, only left candies will be fixed in a single forward pass.
        #So use one pass for left candies and second pass for right candies and take max.
        # A single pass is not sufficient because when assigning candies from left to right, we only satisfy the left neighbor constraint. We don’t yet know how many candies the right neighbor will need, so we might violate the right-side condition.
        candies = [1]*len(ratings) #each child shud get atleast one candy
        sum = 0
        n = len(ratings)

        #left pass
        for i in range(1,n):
            if ratings[i] > ratings[i-1]: #left nei > curr rating
                candies[i] = candies[i-1]+1

        #right pass
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        for num in candies:
            sum += num

        return sum        

# TC: O(N)
# SC: O(N)