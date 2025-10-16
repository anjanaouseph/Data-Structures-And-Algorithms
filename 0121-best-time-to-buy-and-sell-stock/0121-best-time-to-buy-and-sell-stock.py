class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = 0
        high = 1

        max_profit = 0

        while high < len(prices):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]

                max_profit = max(profit, max_profit)

            else:
                low = high #which means we found another day that is lower than low so buy on that  day instead of on the prev low day.

            high += 1

        return max_profit