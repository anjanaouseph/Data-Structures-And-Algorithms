class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # At each step, make the locally optimal choice
        # hoping it leads to a globally optimal solution
        # Prev q, we can only buy and sell 1 stock
        # Here we can buy and sell multiple stocks.
        # After selling, you are free to buy again but only from future days, not from past
        # so we buy at every dip (trough) and sell at the next peak. This is greedy because we take every local profit opportunity, and due to the additive nature of profits, these local gains combine to give the global maximum profit.
        #local maximum profits leads to global maximum profit.
        #Profit will be same or never less if we take all local profits instead of waiting for a global peak.
        #Splitting a big profit into smaller ones doesn’t change the total.

        #cant buy and sell on same day, then profit = 0!
        
        profit = 0

        for i in range(len(prices)):

            if i != 0 and prices[i] > prices[i-1]:#add the valleys
                profit += prices[i]-prices[i-1]
            
        return profit

# TC: O(N)
# SC: O(1)