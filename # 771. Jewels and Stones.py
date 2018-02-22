# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel = []
        jewel_in_stone = 0
        for j in J:
            jewel.append(j)
        for s in S:
            if s in jewel:
                jewel_in_stone += 1
        return jewel_in_stone