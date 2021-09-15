import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize         #가장 큰 값

        for price in prices:
            min_price = min(min_price, price)       # 가장 작은값으로 변경
            profit = max(profit, price - min_price)
        return profit

    maxProfit(1, [7,1,5,3,6,4])