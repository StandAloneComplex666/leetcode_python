#203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
            
        node = head
        pre = dummy
        while node:
            if node.val == val:
                pre.next = node.next
            else:
                pre = node
            node = node.next
        return dummy.next