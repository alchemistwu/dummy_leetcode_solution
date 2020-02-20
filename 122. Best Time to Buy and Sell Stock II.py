"""
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy_state = - prices[0]
        sell_state = 0
        for i in range(1, len(prices)):
            sell_state = max(sell_state, buy_state + prices[i])
            buy_state = max(buy_state, sell_state - prices[i])
        return sell_state

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))