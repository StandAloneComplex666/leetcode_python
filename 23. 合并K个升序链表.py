from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        for index, node in enumerate(lists): # index 用来记录这是第几个链表, node 是每个链表的头结点
                if node != None:  # 只要头结点不空
                    heappush(minHeap ,(node.val, index)) # 将当前头结点的value以及该头结点所在的链表index入堆
        linkedlistHead = ListNode(-1) # 创建用来存放结果的链表
        linkedlistTail = linkedlistHead          # 这个是尾结点        
        while minHeap:  
            val, index = heappop(minHeap) # 堆内链表value最小的出堆，找到他是第几个链表，好找他的下一个位置
            linkedlistTail.next = lists[index]       # 加入到了结果集合中
            linkedlistTail = linkedlistTail.next                # 开始加下一个位置
            lists[index] = lists[index].next # 找到当前链表的下一个元素
            if lists[index] != None:      # 如果不空的话就让他入堆
                heappush(minHeap, (lists[index].val, index)) # 下一个元素入堆
        return linkedlistHead.next # 返回链表

