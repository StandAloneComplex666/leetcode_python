class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def mysort(obj):
            return obj.start
        intervals.sort(key=mysort)
        for i in xrange(len(intervals) -1):
            if not intervals[i].end <= intervals[i+1].start:
                return False
        return True

# my version:
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        
        def sortStart(interval):
            return interval.start

        sortedIntervals = sorted(intervals, key = lambda t:t.start)
        for i in range(0,len(sortedIntervals) - 1):
            if sortedIntervals[i].end > sortedIntervals[i+1].start:
                return False
        return True