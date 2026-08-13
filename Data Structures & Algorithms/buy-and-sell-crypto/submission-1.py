class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -999
        
        l, r = 0,1

        while r <= (len(prices)-1):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                max_profit = max(profit,max_profit)
            else:
                l = r
            r += 1

        return max_profit if max_profit > 0 else 0  