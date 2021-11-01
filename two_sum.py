from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            need_value = target - nums[i]
            if need_value in (nums[:i]+nums[i+1:]):
                nums[i] = 'foo'
                return [i, nums.index(need_value)]

solution = Solution()
print(Solution.twoSum(solution,[2,7,11,15],9))