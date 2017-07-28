#22.Generate Parentheses
#42ms / 83.22%
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return res
        self.dfs_parenthesis(n,n,'',res)
        return res
    
    def dfs_parenthesis(self , l, r, string, res):
        if l == 0 and r == 0:
            return res.append(string)
        if r < l:
            return
        if l > 0 :
            self.dfs_parenthesis( l-1, r, string + '(', res)
        if r > 0 :
            self.dfs_parenthesis( l, r-1, string + ')', res)