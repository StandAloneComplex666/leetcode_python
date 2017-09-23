#147. Insertion Sort List
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        while head:
            # check if it is needed to reset the cur pointer
            if cur and cur.val > head.val:
                cur = dummy
            # find the place to insert
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # insert and sort the next element
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next

class Solution:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         #为链表加一个头节点
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            #如果链表是升序的，那么curr指针一直往后移动
                pre = dummy                         #直到一个节点的值小于前面节点的值
                while pre.next.val < curr.next.val: #然后寻找插入的位置
                    pre = pre.next
                tmp = curr.next                     #上面的示意图就是以下这段代码
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next