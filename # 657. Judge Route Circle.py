# 657. Judge Route Circle
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        map_dir = {'R':0,'L':0,'U':0,'D':0}
        for c in moves:
            map_dir[c]+=1
        return (map_dir['R']==map_dir['L'])and(map_dir['U']==map_dir['D'])