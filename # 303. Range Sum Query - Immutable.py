# my first edition, which will lead to TLE
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numList  = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        for n in range(i,j+1):
            res += self.numList[n]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# second edition:use a list to pre store the accumlation from index 0 to index i
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numList  = nums
        self.accum = [0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            self.accum.append(temp)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = self.accum[j+1] - self.accum[i]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)