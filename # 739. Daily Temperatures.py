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