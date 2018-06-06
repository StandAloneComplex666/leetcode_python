#the first time I tried and refered other's answer:
class Solution:

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results

# the second time, I tried dfs again:
# a wrong answer:
class Solution(object):
    def dfs(self, res, temp, nums, start):
        print temp
        res.append(temp)
        print res
        for i in range(start,len(nums)):
            temp.append(nums[i])
            self.dfs(res, temp, nums, i + 1)
            temp.pop()
        return res
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res= []
        start = 0
        temp = []
        self.dfs(res, temp, nums, start)
        return res

'''
the output will be:
temp is:  []
res is: [[]]
temp is:  [1]
res is: [[1], [1]]
temp is:  [1, 2]
res is: [[1, 2], [1, 2], [1, 2]]
temp is:  [1, 2, 3]
res is: [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
temp is:  [1, 3]
res is: [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]
temp is:  [2]
res is: [[2], [2], [2], [2], [2], [2]]
temp is:  [2, 3]
res is: [[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3]]
temp is:  [3]
res is: [[3], [3], [3], [3], [3], [3], [3], [3]]
'''

# the correct solution
class Solution(object):
    def dfs(self, res, temp, nums, start):
        #print "temp is: ", temp
        res.append(temp)
        #print "res is: ", res
        for i in range(start,len(nums)):
            self.dfs(res, temp + [nums[i]], nums, i + 1)
        #return res
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res= []
        start = 0
        temp = []
        self.dfs(res, temp, nums, start)
        return res

# the fastest one is like this:
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        out = [[]]
        
        for n in nums:
            out += [i+[n] for i in out]
        
        return out