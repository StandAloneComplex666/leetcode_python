class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign = 1
        stack =[]
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i += 1
                    #print(num)
                #print(num)
                res += num*sign
                i += 1
                #print(res)
                #print(i,'   ', len(s))
            elif s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                i += 1
            elif s[i] == ')':
                res = res*stack.pop() + stack.pop()
                i += 1
            elif s[i] == ' ':
                i += 1
        #print(res)
        return res