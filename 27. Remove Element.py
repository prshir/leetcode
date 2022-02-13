from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        place_ind = len(nums)-1
        for i_ in range(len(nums),0,-1):
            i = i_-1
            print(i)
            if nums[i] == val:
                nums[place_ind], nums[i] = nums[i], nums[place_ind]
                place_ind -= 1
        print(nums)
        return place_ind+1 #len(nums)-nums.count(val)

solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))