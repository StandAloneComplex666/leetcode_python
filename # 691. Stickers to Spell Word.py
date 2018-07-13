class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        m = len(stickers)
        mp = [[0]*26 for y in range(m)] 
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1    
        dp = {}
        dp[""] = 0
        
        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1   
            ans = sys.maxint
            for i in xrange(n):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j]) 
                tmp = helper(dp, mp, s)
                if (tmp != -1): 
                    ans = min(ans, 1+tmp)    
            dp[target] = -1 if ans == sys.maxint else ans
            return dp[target]
                
        return helper(dp, mp, target)