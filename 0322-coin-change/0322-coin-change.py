class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #optimizing using 1D array
        #basically we are just overwritting each row
        m = len(coins) #rows
        n = amount #cols

        #create a 1D array of (n+1) dimension
        dp = [0] * (n+1)

        for j in range(1,n+1):
            dp[j] = float('inf') 

        #now lets fill the actual table
        for i in range(1,m+1):#skip first row which is the dummy row
            for j in range(n+1): #cant skip first column.
                if j < coins[i-1]: #amount < coin then not possible i-1 to map to index in original coins array because now we have a preceeding 0 in coins array due to dummy row [0 1 2 5] instead of [1 2 5]
                    dp[j] = dp[j] #copy the value from the prev row as it is
                else:
                    dp[j] = min(dp[j], 1+dp[j - coins[i-1]]) #if condition above ensures dp[j - coins[i-1] is not out of bounds. as we are checking if j < coins[i-1] case.
                    #taking the min of : case where we don't choose that coin and case where we choose the coin + 1. 

        return -1 if dp[n] == float('inf') else dp[n]     