class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #We need to buy low and sell high
        l,r = 0,1
        max_profit = 0
        while r<len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r #we know l>=r thats why we came here, if we keep l at r then anyways the difference will be more, meaning more profit. We can optimize in this way.
#eg: Why buy on day 1 when I can buy on day 2 for a lesser price (intention is to maximise the profit)
#NOTE: We want out left pointer to always be at the minimum
            r += 1
        return max_profit
        