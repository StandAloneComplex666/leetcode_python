# my version:use two pointers first let the long list pointer go
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object): 
    
    def getSize(self ,head):
        n = 0
        while head:
            head = head.next
            n +=  1
        return n
    
   
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = self.getSize(headA)
        lb = self.getSize(headB)
        
        if la < lb:
            return self.getIntersectionNode(headB, headA)

        for i in range(la -lb):
            headA = headA.next
        
        while headA and headB:
            if id(headA) == id(headB):
                return headA
            
            headA = headA.next
            headB = headB.next
            
        return None

# another method used two pointers(fastest): both pointers go together and finally they meet or both hit the end == None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None