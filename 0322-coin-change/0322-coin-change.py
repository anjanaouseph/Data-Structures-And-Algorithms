class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins) #rows
        n = amount #cols

        #create a 2D matrix of (m+1)*(n+1) dimension
        dp = [[0] * (n+1) for _ in range(m+1)] #we will have m+1 and n+1 rows and cols because we added a 0th column and 0th row above

        for j in range(1,n+1):
            dp[0][j] = float('inf') #dummy row except first cell rest all are infs

        #now lets fill the actual table
        for i in range(1,m+1):#skip first row which is the dummy row
            for j in range(n+1): #cant skip first column.
                if j < coins[i-1]: #amount < coin then not possible i-1 to map to index in original coins array because now we have a preceeding 0 in coins array due to dummy row [0 1 2 5] instead of [1 2 5]
                    dp[i][j] = dp[i-1][j] #copy the value from the prev row as it is
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j - coins[i-1]])
                    #taking the min of : case where we don't choose that coin and case where we choose the coin + 1. 

        return -1 if dp[m][n] == float('inf') else dp[m][n]     