class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(l+1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            
            profit = max(profit, prices[r] - prices[l])
        
        return profit