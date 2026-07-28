class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = 0
        s = 1

        while s < len(prices):
            if prices[s] < prices[b]:
                b = s
            elif prices[s] > prices[b]:
                profit = max(profit, prices[s] - prices[b])
                
            s += 1

        return profit

        