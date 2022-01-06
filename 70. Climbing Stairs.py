class Solution(object):
    def climbStairs(self, n):
        res = {x+1:x+1 for x in range(3)}
        if n<4:
            return res[n]
        ind = 4
        while len(res) < n:
            res[ind] = res[ind-1]+res[ind-2]
            ind+=1
        return res[n]



solution = Solution()
print(solution.climbStairs(5))