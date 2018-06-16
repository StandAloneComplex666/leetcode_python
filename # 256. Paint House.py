class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        dpRed, dpBlue, dpGreen = costs[0]
        for i in range(1, n):
            dpRed, dpBlue, dpGreen = min(dpBlue, dpGreen) + costs[i][0], min(dpRed, dpGreen) + costs[i][1], min(dpRed, dpBlue) + costs[i][2]
        return min(dpRed, dpBlue, dpGreen)