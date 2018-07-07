class Solution(object):
    def gcd(self, a, b):
        if a > b:
            a, b = b, a
        for i in xrange(a, 1, -1):
            if b % i == 0 and a % i == 0:
                return i
        return 1

    def add_fractions(self, frac1, frac2):
        sign = 1   
        numerator = frac1[0]*frac2[1] + frac2[0]*frac1[1]
        if numerator < 0:
            sign = -1
            numerator *= -1

        denominator = frac1[1] * frac2[1]
        gcd_res = self.gcd(numerator, denominator)

        fraction = [0] * 2
        fraction[0] = numerator / gcd_res
        fraction[1] = denominator / gcd_res

        if fraction[0] == 0:
            fraction[1] = 1

        fraction[0] *= sign
        return fraction

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        expression = expression + '+'

        if expression[0] != '-':
            expression = '+' + expression

        sign, total = 1, 0
        numer, denom = 0, 0
        frac1, frac2 = [], []

        for i, c in enumerate(expression):
            if c == '-' or c == '+':
                sign = -1 if c == '-' else 1
                if i == 0:
                    continue
                denom = total
                total = 0
                frac2.append(denom)
                if len(frac1) == 0:
                    frac1 = frac2
                else:
                    frac1 = self.add_fractions(frac1, frac2)
                frac2 = []
            elif c.isdigit():
                total = total * 10 + int(c)
            elif c == '/':
                numer = sign*total
                total = 0
                frac2.append(numer)

        res = str(frac1[0]) + '/' + str(frac1[1])

        return res