class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        category = set(candies)
        if len(category) > int(0.5*len(candies)):
            return int(0.5*len(candies))
        else:
            return len(category)

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(category), int(len(candies)*0.5))