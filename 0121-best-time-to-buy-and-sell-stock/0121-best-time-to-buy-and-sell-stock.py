class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = 0
        high = 1

        max_profit = 0

        while high < len(prices):
            if prices[high] > prices[low]:
                profit = prices[high]-prices[low]
                max_profit = max(max_profit,profit)

            else:
                low = high#found a cheaper price so buy on this day.
                #say we found a higher price in future, profit will be higher with this buy price as it is smaller, than the previous day's buying price
            
            high += 1

        return max_profit   

# Time Complexity: O(N)
# Space Complexity: O(1)