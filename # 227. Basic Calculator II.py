class Solution(object):
    def calculate(self, s):
            """
            :type s: str
            :rtype: int
            """
            res = 0
            prev_op = '+'
            num = prev_term = 0
            for i in range(len(s) + 1):
                if i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif i == len(s) or s[i] in ['+', '-', '*', '/']:
                    if prev_op == '+':
                        res += num
                        prev_term = num
                    elif prev_op == '-':
                        res -= num
                        prev_term = -num
                    elif prev_op == '*':
                        res -= prev_term
                        prev_term *= num
                        res += prev_term
                    else:
                        res -= prev_term
                        prev_term = int(prev_term / float(num))
                        res += prev_term
                    num = 0
                    if i < len(s):
                        prev_op = s[i]
            return res