from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        if not strs[0]:
            return ''
        shortest_word = strs[0]
        while shortest_word:
            failed = False
            for s in strs:
                if not s.startswith(shortest_word):
                    shortest_word = shortest_word[:-1]
                    failed = True
                    break
            if not failed: return shortest_word
        return ''


solution = Solution()
print(solution.longestCommonPrefix(['abcs','ab','bbc']))