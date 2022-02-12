class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        l = len(nums)
        for i in range(0, l, 2):
            if i+1 == l:
                return nums[i]
            if nums[i]!=nums[i+1]:
                return nums[i]


solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))