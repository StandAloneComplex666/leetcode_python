
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# 贪心算法的代表情况之一，贪心算法的成立性见书中证明
# 若要求最少的删除，则要保证当前情况下选择最早结束的interval ，则局部可以保证容纳最多数量的interval
# 由于贪心性质，则总体可以保证容纳数量最多的interval
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x:x.end)
        #for i in range(len(intervals)):
        #    print(intervals[i].start, ' ', intervals[i].end)
        current, res = -float('inf'), 0
        for i in intervals:
            if current > i.start :
                res += 1
            else:
                current = i.end
        return res