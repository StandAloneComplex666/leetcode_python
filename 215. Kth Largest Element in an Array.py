# Method 2
import Queue
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = Queue.PriorityQueue()
        for num in nums:
            if minHeap.qsize() < k:
                minHeap.put(num)
            elif num > minHeap.queue[0]:
                minHeap.get()
                minHeap.put(num)

        return minHeap.queue[0]
