from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] +=1
            return digits
        elif not len([x for x in digits if x != 9]):
            ans = [0 for x in digits]
            ans.insert(0, 1)
            return ans
        else:
            i = len(digits) - 1
            while digits[i] == 9:
                i-=1
            digits[i]+=1
            for j, x in enumerate(digits):
                if j > i:
                    digits[j] = 0
            return digits



solution = Solution()
print(solution.plusOne([1,2,9]))