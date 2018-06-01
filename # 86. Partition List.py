# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p1 = ListNode(0)
        p2 = ListNode(0)
        a, b = p1, p2
        p = head
        
        while(p != None):
            if p.val < x:
                a.next = p
                a = a.next
            else:
                b.next = p
                b = b.next
            p = p.next
        a.next = p2.next
        b.next = None
        return p1.next