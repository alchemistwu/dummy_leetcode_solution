"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        length = len(prices)
        buy_state = - prices[0]
        sell_state_1 = [0] * length
        sell_state_2 = prices[-1]
        buy_state_2 = [0] * length
        max_profit = 0
        for index_1 in range(1, len(prices)):
            sell_state_1[index_1] = max(sell_state_1[index_1 - 1], buy_state + prices[index_1])
            buy_state = max(buy_state,  - prices[index_1])

            index_2 = length - 1 - index_1

            sell_state_2 = max(sell_state_2, prices[index_2])
            buy_state_2[index_2] = max(buy_state_2[index_2 + 1], sell_state_2 - prices[index_2])

            if index_1 == length / 2:
                if length % 2 == 1:
                    max_profit = max(max_profit, sell_state_1[index_1] + buy_state_2[index_1])
                else:
                    max_profit = max(max_profit,
                                     max(
                                         sell_state_1[index_1] + buy_state_2[index_1],
                                         sell_state_1[length - index_1 - 1] + buy_state_2[length - index_1 - 1],
                                         ))
            elif index_1 > length / 2:
                max_profit = max(max_profit,
                                 max(
                                     sell_state_1[index_1] + buy_state_2[index_1],
                                     sell_state_1[length - index_1 - 1] + buy_state_2[length - index_1 - 1],
                                 ))

        return max_profit

if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))