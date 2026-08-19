class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 99999
        profit = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            cur_profit = prices[i] - lowest
            if profit < cur_profit:
                profit = cur_profit
        return profit