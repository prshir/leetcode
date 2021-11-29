class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a); len_b = len(b)
        len_d = abs(len_a-len_b)
        add_list = '0'*len_d
        if len_d:
            if len_a < len_b:
                a = add_list + a
            else:
                b = add_list + b
        i = len(a)-1
        plus = 0; s = ''
        while i >= 0:
            res = int(a[i]) + int(b[i]) + plus
            if res == 0:
                plus = 0
                res = 0
            if res == 1:
                plus = 0
                res = 1
            if res == 2:
                plus = 1
                res = 0
            if res == 3:
                plus = 1
                res = 1
            s+=str(res)
            i-=1
        if plus==1:
            s+='1'
        return s[::-1]


solution = Solution()
print(solution.addBinary('1','11'))