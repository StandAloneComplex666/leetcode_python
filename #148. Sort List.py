# 148. Sort List
# fastest version 195ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def pl(head):
            p = head
            res = []
            while p:
                res.append(p.val)
                p = p.next
            print res
        def quickSort(head):
            if not head or not head.next: return head

            lh, rh, m= partition(head, head.val)
            #pl(lh)
            #pl(rh)
            
            left = quickSort(lh)
            right = quickSort(rh)
            
            p = nullHead = ListNode(0)
            p.next = left
            while p and p.next: p = p.next
            p.next = head
            m.next = right
            return nullHead.next

        def partition(head, pivot):
            l = ln = ListNode(0)
            r = rn = ListNode(0)
            m = mn = head
            p = head.next
            #pl(head)
            while p:
                if p.val == pivot:
                    m.next = p
                    m = m.next
                elif p.val < pivot:
                    l.next = p
                    l = l.next
                else:
                    r.next = p
                    r = r.next
                p = p.next
            l.next = r.next = m.next = None
            #pl(ln)
            #pl(rn)
            return ln.next, rn.next, m
        
        return quickSort(head)

#my version 395ms 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = cur = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return dummy.next