
class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        ave = s/len(A)
        res = []
        for i in range(1, len(A)//2+1):
            s1=ave*i
            if s1-int(s1)<0.0000001:
                res.append([i,int(s1)])
                
        def dfs(i,cnt,t):
            if cnt==0 and t==0: return True
            if cnt==0 or t<0: return False
            if i==len(A): return False
            if dfs(i+1, cnt, t): return True
            if dfs(i+1, cnt-1, t-A[i]): return True
        
        for c, s in res:
            if dfs(0, c, s): return True   
        return False