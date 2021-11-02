from typing import List
class Solution:
    res = set()

    def add_possible_pars(self):
        if not Solution.res:
            Solution.res.add('()')
            return
        all_current_ans = Solution.res.copy()
        for current_ans in all_current_ans:
            for i in range(len(current_ans)+1):
                Solution.res.add(current_ans[:i]+'()'+current_ans[i:])

    def generateParenthesis(self, n: int) -> List[str]:
        Solution.res = set()
        for i in range(n):
            Solution.add_possible_pars(self)
        ans = [x for x in Solution.res if len(x) == n*2]
        return ans

solution = Solution()
print(solution.generateParenthesis(4))