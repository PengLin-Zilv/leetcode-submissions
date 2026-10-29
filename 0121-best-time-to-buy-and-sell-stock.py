class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        # stock max profit: buy low sell high, so we track the lowest
        # assume we sell at each day to prev lowest

        for price in prices:
            lowest = min(price, lowest)
            profit = price - lowest
            max_profit = max(max_profit, profit)
        return max_profit