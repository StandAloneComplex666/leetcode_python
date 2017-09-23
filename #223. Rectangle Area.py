#223. Rectangle Area
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        Length = min( max(0, C-E) , max(0, G-A), C-A, G-E )
        Height = min( max(0, H-B), max(0, D-F), H-F, D-B  )
        tot_area = abs( (A-C)*(B-D) ) + abs( (E-G)*(F-H) ) - Length*Height
        
        return tot_area