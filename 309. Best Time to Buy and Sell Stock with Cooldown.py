from typing import List
class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        """
                :type prices: List[int]
                :rtype: int
                """
        n = len(prices)
        if n < 2:
            return 0
        buy, profit = [float('-inf')] * n, [0] * n
        buy[0], buy[1] = max(buy[0], -prices[0]), max(-prices[0], -prices[1])
        profit[1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            buy[i] = max(buy[i - 1], profit[i - 2] - prices[i])
            profit[i] = max(profit[i - 1], prices[i] + buy[i - 1])
        return profit[-1]

if __name__ == '__main__':
    s = Solution()
    input = [8,6,4,3,3,2,3,5,8,3,8,2,6]
    print(s.maxProfit(input))


