from typing import List
from datetime import datetime

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = max(nums)
        if m < 0: return m
        for num in nums:
            s += num
            if s < 0:
                s = 0
            if s > m:
                m = s
        return m
    
    def maxSubArray2(self, nums: List[int]) -> int:
        print(datetime.now())
        print(len(nums))
        if min(nums) >= 0:
            return sum(nums)
        if max(nums) <= 0:
            return max(nums)

        numsf = [num for num in nums if num!=0]
        s = 0
        nums_sign = []
        for i in range(len(numsf)):
            s+=numsf[i]
            if i==len(numsf)-1:
                nums_sign.append(s)
                break
            if numsf[i]*numsf[i+1] < 0:
                nums_sign.append(s)
                s = 0
        print(len(nums_sign))
        if nums_sign[0] < 0:
            nums_sign = nums_sign[1:]
        if nums_sign[-1] < 0:
            nums_sign = nums_sign[0:-1]
        print(nums_sign)
        s = sum(nums_sign)

        print(datetime.now())
        indices = [i for i,x in enumerate(nums_sign) if x>0]
        print(datetime.now())
        for i in range(len(indices)):
            local_sum = 0
            local_nums = nums_sign[indices[i]:]
            for j in range(len(local_nums)):
                local_sum += local_nums[j]
                if local_nums[j]>0:
                    if local_sum>s:
                        s=local_sum


        print(datetime.now())
        return s

    def maxSubArray_(self, nums: List[int]) -> int:
        mx = -1e6
        if min(nums) >= 0:
            return sum(nums)
        if max(nums) <= 0:
            return max(nums)
        mx = sum(nums)
        negative_indices = [i for i in range(len(nums)) if nums[i] < 0]
        # if 0 not in negative_indices:
        negative_indices.insert(0,-1)
        negative_indices.append(len(nums))
        possible_ranges = []
        for t in itertools.product(negative_indices, negative_indices):
            print(f'{t[0]} {t[1]}')
            if t[1]>t[0]:
                possible_ranges.append(t)
        possible_ranges.append((len(nums)-1,len(nums)))
        for possible_range in possible_ranges:
            temp_sum = sum(nums[possible_range[0]+1:possible_range[1]])
            if temp_sum > mx:
                mx = temp_sum
        return mx


solution = Solution()
# print(solution.maxSubArray([-2,1,-3,4,0,-1,2,1,-5,4,0])) # 6
# print(solution.maxSubArray([5,4,-1,7,8])) # 23
print(solution.maxSubArray([1,2,-1])) # 3
# print(solution.maxSubArray([-1,200,-1,2,-100,500,-2,100])) #
