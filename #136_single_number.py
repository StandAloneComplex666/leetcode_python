#38 ms \ 99.01%
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result = result ^ i
        return result 
