class Solution:
    def candy(self, ratings: List[int]) -> int:
        #using the slop method
#        Instead of giving candies to each child,
# we look at the ratings like a mountain shape and calculate how many candies that shape needs.
#         if two ratings are same just give 1 candy because the constraint just says neighbors with higher rating needs extra candy.
            sum = 1 #first one gets one candy
            i = 1
            n = len(ratings)

            while i < n:
                if ratings[i-1] == ratings[i]:
                    sum+= 1 #just add one
                    i+=1
                    continue

                #increasing slope
                peak = 1 #assigned 1 to first index after that slope starts
                while (i<n and ratings[i] > ratings[i-1]):
                    peak += 1
                    i+=1
                    sum += peak

                #decreasing slope
                down = 1 # else peak will cause overcounting
                while (i<n and ratings[i] < ratings[i-1]):
                    sum += down
                    down += 1
                    i += 1

                if (down > peak):
                    sum += down - peak

            return sum

# TC: O(N)
# SC: O(1)
        
# eg: 0 2 4 7 6 5 4 3 2 1 1 1
#     1 2 3 4,1 2 3 4 5 6 
#     after 6 down will be at 7 but we wont add that to the slope. so finally if down > peak, we add diff to the sum 
# check strivers explanation