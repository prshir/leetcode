from typing import List

nums = [1,1,2]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        last_unqiue = nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] == last_unqiue:
                nums[i+1] = 1000
            else:
                last_unqiue = nums[i+1]
        nums.sort()
        nums = nums[:(len(nums)-nums.count(1000))]
        return len(nums)

solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)