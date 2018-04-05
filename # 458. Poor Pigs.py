class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

# https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution
# https://leetcode.com/problems/poor-pigs/discuss/94273/Solution-with-detailed-explanation
# those two article explains this bizzare problem in different but clear ways