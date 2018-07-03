class Solution:
    def minCostII(self, costs):
        if costs == []:
            return 0
        
        idx = -1
        min1 = min2 = 0
        
        for i in range(len(costs)):
            newMin1 = float("inf")
            newMin2 = float("inf")
            
            for j in range(len(costs[i])):
                if j != idx:
                    costs[i][j] += min1
                else:
                    costs[i][j] += min2
                
                if costs[i][j] < newMin1:
                    newMin2 = newMin1
                    newMin1 = costs[i][j]
                    newIdx = j
                elif costs[i][j] < newMin2:
                    newMin2 = costs[i][j]
            
            min1 = newMin1
            min2 = newMin2
            idx = newIdx
            
        return min(costs[-1][j] for j in range(len(costs[-1])))