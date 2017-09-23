#23. Merge k Sorted Lists
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        cur = dummy
        heap = [(l.val, l) for l in lists if l]
        heapq.heapify(heap)
        while heap:
            x = heapq.heappop(heap)[1]
            cur.next = x
            x = x.next
            if x:
                heapq.heappush(heap, (x.val, x))
            cur = cur.next
            cur.next = None
            
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        cur = dummy
        q = PriorityQueue()
        for i in lists:
            if i: q.put((i.val, i))
        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:q.put((cur.next.val,cur.next))
        return dummy.next