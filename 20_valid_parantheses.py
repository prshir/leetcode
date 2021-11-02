class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        if s.count('(')!=s.count(')') or s.count('[')!=s.count(']') or s.count('{')!=s.count('}'):
            return False
        while s:
            len_s = len(s)
            if '()' in s or '{}' in s or '[]' in s:
                s = s.replace('()','').replace('{}','').replace('[]','')
            if len(s) == len_s:
                return False
        return True

solution = Solution()
print(solution.isValid('()(())[]'))