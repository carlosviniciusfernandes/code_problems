# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#! works but times out !!!
class Solution1:
    def maxProfit(self, prices: list[int]) -> int:

        buy_idx = 0
        sell_idx = 0
        max_profit = 0

        for i, val in enumerate(prices):
            if val <= prices[buy_idx]:
                profit = max(prices[i:]) - val #! timesout here if the array is enornous
                max_profit = max(profit, max_profit)

        return max_profit


class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit


class Solution3:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res