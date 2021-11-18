from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        left = 0
        right = len(nums)-1
        while right-left > 1 and nums[left] != target and nums[right] != target:
            half = round((right-left)/2)
            if nums[left+half] < target:
                left = left+half
            else:
                right = left+half
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if right-left==1:
            return right

solution = Solution()
# print(solution.searchInsert([2,7,8,9,10],9))
print(solution.searchInsert([1,3,5,6],5))