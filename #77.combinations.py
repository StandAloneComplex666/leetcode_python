#77.combinations
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def dfs(start, valuelist):
            if self.count == k: ret.append(valuelist); return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1
        ret = []; self.count = 0
        dfs(1, [])
        return ret

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        
        Examples:
        n = 4 and k = 2 ==> [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
        n = 5 and k = 3 ==> [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
        """
        # Key idea:
        # Use recursion to implement n_C_k = n-1_C_k-1 + n-1_C_k
        results = []
        if k == n or k == 0:  # n_C_n or n_C_0
            results = [i+1 for i in range(k)]
            return [results]

        for res in self.combine(n-1, k-1):
            res.append(n)
            results.append(res)
        for res in self.combine(n-1, k):
            results.append(res)
        return results