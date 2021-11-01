class Solution:
    order = 'MDCLXVI'
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    def max_leftside_rem(self, s):
        max_num = 'I'
        for letter in Solution.order:
            if letter in s:
                max_num = letter
                break
        max_num_index = s.index(max_num)
        max_num_count = 1
        while True:
            if len(s) == 1:
                break
            if max_num_index+max_num_count < len(s) and s[max_num_index+max_num_count] == max_num:
                max_num_count+=1
            else:
                break
        # max_num_string = max_num * max_num_count
        left_side = Solution.vals[s[:max_num_index]] if max_num_index > 0 else 0
        middle = Solution.vals[max_num]*max_num_count
        Solution.res += middle-left_side
        bias = len(s[:max_num_index])
        s = s.replace(s[:max_num_index],'',1)
        s = s.replace(s[max_num_index-bias:max_num_index+max_num_count-bias],'',1)
        return s

    def romanToInt(self, s: str) -> int:
        Solution.res=0
        while True:
            s = Solution.max_leftside_rem(self, s)
            if not s: break
        return Solution.res

solution = Solution()
# print(Solution.romanToInt(solution,'CMXIX'))
# print(Solution.romanToInt(solution,'XXX'))
print(Solution.romanToInt(solution,"IV"))