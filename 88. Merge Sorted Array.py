class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1.pop()
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        print(nums1)

solution = Solution()
# solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
solution.merge([1], 1, [], 0)