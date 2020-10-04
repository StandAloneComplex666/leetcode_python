from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        s = deque(s)
        num = 0
        sign = "+"
        res = []
        for i in range(n):
            char = s.popleft()
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num = self.calculate(s)
            if (not char.isdigit() and char != " ") or not s:
                if sign == "+":
                    res.append(num)
                if sign == "-":
                    res.append(-num)
                if sign == "*":
                    res.append(res.pop() * num)
                if sign == "/":
                    res.append(int(res.pop() / num))
                num = 0
                sign = char
            if char == ")":
                break
        return sum(res)

