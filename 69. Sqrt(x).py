class Solution(object):

    def mySqrt(self, x):
        if x==0: return 0
        if x < 4: return 1
        top = x; bottom = 1
        while True:
            if top*top==x: return int(top)
            if bottom*bottom==x: return int(bottom)
            if top-bottom==1: return int(bottom)
            step = round((top-bottom)/2-.01)
            if (bottom+step)*(bottom+step) == x:
                return int(bottom+step)
            if (top-step)*(top-step) == x:
                return int(top-step)
            if (bottom+step)*(bottom+step) < x:
                bottom = bottom + step
            else:
                top = top - step

solution = Solution()
print(solution.mySqrt(16))