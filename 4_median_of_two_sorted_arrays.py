from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_common = sorted(nums1+nums2)
        if not len(list_common)%2:
            ind=len(list_common)//2-1
            return (list_common[ind]+list_common[ind+1])/2
        return list_common[int(len(list_common)/2)]



solution = Solution()
print(solution.findMedianSortedArrays([1,3],[2]))