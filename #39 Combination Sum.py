#39 Combination Sum
#my version:#92ms/80.36%
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


#other's version: he himself did several versions:
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSum2(candidates, target)
    
    # method 2
    def combinationSum2(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return 

            for item in candidates:
                if item > remain:
                    break
                if stack and item < stack[-1]:
                    continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result
    
    # method 1.3: variant of the method 1.2
    # avoid creating too many `path` to save time
    def combinationSum13(self, candidates, target):
        res = []
        comb = []
        candidates.sort()
        self.helper13(candidates, target, 0, comb, res)
        return res
    
    def helper13(self, nums, target, index, comb, res):
        if target == 0:
            res.append([x for x in comb])
            return
        for i in xrange(index, len(nums)):
            if nums[i] <= target:
                comb.append(nums[i])
                self.helper13(nums, target - nums[i], i, comb, res)
                comb.pop() 

    
    # method 1.2: variant of the method 1.1, avoid using slice to save space
    def combinationSum12(self, candidates, target):
        res = []
        candidates.sort()
        self.helper12(candidates, target, 0, [], res)
        return res
    
    def helper12(self, nums, target, index, path, res):
        if target > 0:
            for i in xrange(index, len(nums)):
                self.helper12(nums, target - nums[i], i, path + [nums[i]], res)
        elif target == 0:
            res.append(path)
            
    
    # method 1.1: variant of the method 1
    def combinationSum11(self, candidates, target):
        res = []
        candidates.sort()
        self.helper11(candidates, target, [], res)
        return res
    
    def helper11(self, nums, target, path, res):
        if target > 0:
            for i in xrange(len(nums)):
                self.helper11(nums[i:], target - nums[i], path + [nums[i]], res)
        elif target == 0:
            res.append(path)
            return
        else:
            return
        
    
    # method 1: backtracking, recursive, dfs
    # derived from the method 2 of the subset problem
    # `nums[i+1:]` changed to `nums[i:]` as an item can be repeatly used
    # O(2^n) time, O(n) space
    def combinationSum1(self, candidates, target):
        res = []
        candidates.sort()
        self.helper1(candidates, target, [], res)
        return res
    
    def helper1(self, nums, target, path, res):
        curr_sum = sum(path)
        # print "sum: " + str(curr_sum) +  ", " + str(path)
        if curr_sum < target:
            for i in xrange(len(nums)):
                self.helper1(nums[i:], target, path + [nums[i]], res)
        elif curr_sum == target:
            res.append(path)
            return
        else:
            return
    
    
    # method 2 of the subset problem: backtracking, recursive, dfs
    # O(2^n) time
    def subsets(self, nums):
        result = []
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, index, path, result):
        result.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], result)