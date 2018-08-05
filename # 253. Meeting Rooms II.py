# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x : x.start) 
        heap = [] #minimum end time
        room = 0
        
        for i in intervals:
            if heap and heap[0] <= i.start: #non-conflict
                heapq.heappop(heap)
                room -= 1
            heapq.heappush(heap, i.end)
            room += 1
        return room