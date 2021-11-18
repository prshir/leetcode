class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while True:
            if '  ' in s:
                s = s.replace('  ',' ')
            else:
                break
        words = s.split()
        return len(words[-1])

solution = Solution()
print(solution.lengthOfLastWord('hello world  '))