from typing import List

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        mn = prices[0]
        rev = 0
        for price in prices:
            if price < mn:
                mn = price
            elif price > mn:
                if price-mn>rev:
                    rev = price - mn
        return rev

solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))