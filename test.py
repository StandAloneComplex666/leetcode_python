class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(ret, sorted(candidates), 0, target, [])
        return ret
        
    def dfs(self, ret, cand, idx, target, temp):
        
        for i in xrange(idx, len(cand)):
            if i > idx and cand[i] == cand[i-1]:
                continue
            if cand[i] == target:
                # print idx, i, cand[i], target
                ret.append(temp + [cand[i]])
                break 
            elif cand[i] > target:  # sorted, so any future candidates will also be too big
                break               # these two breaks save time but do not prevent duplicates in earlier idx, only this idx
            else:
                self.dfs(ret, cand, i+1, target-cand[i], temp+[cand[i]])  # idx+1 since we cannot use duplicates this time