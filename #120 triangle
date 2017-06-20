class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        res=[triangle[0]]
        N = len(triangle)
        for i in range(1,len(triangle)):
            res.append([])
            for j in range(len(triangle[i])):
                if j-1>=0 and j< len(triangle[i-1]):
                    res[i].append(min(res[i-1][j-1],res[i-1][j])+triangle[i][j])
                elif j-1>=0:
                    res[i].append(res[i-1][j-1]+triangle[i][j])
                else:
                    res[i].append(res[i-1][j]+triangle[i][j])
                 
        minvalue = min(res[N-1])
        return minvalue
        
