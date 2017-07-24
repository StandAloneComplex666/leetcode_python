#19. Remove Nth Node From End of List
# fastest version so far create a list to save the nodes and return by index
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp_list = []
        prev_node = head
        while prev_node:
            tmp_list.append(prev_node)
            prev_node = prev_node.next

        list_length = len(tmp_list)

        if list_length == n:
            return tmp_list[1] if len(tmp_list) > 1 else []
        elif list_length > n:
            tmp_list[list_length - n - 1].next = tmp_list[list_length - n].next
                
        return head

# my version 
# create two pointers :the first one start and when it has traversed n nodes , the second one start
# when the first one came to the end , the second one is pointing the target,finally delete it. 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0); dummy.next=head
        p1=p2=dummy
        for i in range(n): p1=p1.next
        while p1.next:
            p1=p1.next; p2=p2.next
        p2.next=p2.next.next
        return dummy.next