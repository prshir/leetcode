class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clear_s = ''.join(list(map(lambda x: x.lower() if x.isdigit() or x.isalpha() else '', s)))
        l = len(clear_s)
        max_ind = int(round(l/2))

        for i in range(max_ind):
            if clear_s[i] != clear_s[l-1-i]:
                return False
        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))