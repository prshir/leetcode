from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        y = x[::-1]
        return y==x

solution = Solution()
print(Solution.isPalindrome(solution,1212))