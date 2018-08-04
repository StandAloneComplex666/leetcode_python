# original one : brute force  (TLE)
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        nextHigher = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    nextHigher[i] = j-i
                    break
        return nextHigher

# updated one: use stack and passes:
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                tempTuple = stack.pop()
                res[tempTuple[0]] = i - tempTuple[0]
            stack.append((i,temp))
        return res