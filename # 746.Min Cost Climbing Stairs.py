# 746.Min Cost Climbing Stairs
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return -1
        l = len(cost)
        if l<2 or l>1000:
            return -1
        total_cost = [-1 for i in range(l+1)]
        for i in range(l+1):
            if i>=2:
                total_cost[i] = min((total_cost[i-1]+cost[i-1]),(total_cost[i-2])+cost[i-2])
            elif i == 1:
                total_cost[i] = 0
            elif i == 0:
                total_cost[i] = 0
        return total_cost[-1]