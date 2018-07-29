# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        answer = None
        carry = 0
        while stack1 and stack2:
            add = stack1.pop() + stack2.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = answer
            answer = ListNode(add % 10)
            answer.next = temp
        l = stack1 if stack1 else stack2
        while l:
            add = l.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = answer
            answer = ListNode(add % 10)
            answer.next = temp
        if carry:
            temp = answer
            answer = ListNode(1)
            answer.next = temp
        return answer

# my version:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        s1 = []
        s2 = []
        
        node1, node2 = l1, l2
        
        while node1 != None or node2 != None:
            if node1 != None:
                s1.append(node1.val)
                node1 = node1.next
            if node2 != None:
                s2.append(node2.val)
                node2 = node2.next
                
        tempSum = 0
        resStack = []
        res = tempNode = ListNode(0)
        # print(s1)
        # print(s2)
        
        while len(s1)!= 0 or len(s2)!= 0:
            if len(s1)!= 0:
                tempSum += s1.pop()
            if len(s2)!= 0:
                tempSum += s2.pop()
            resStack.append(tempSum%10)
            tempSum =int(tempSum/10)
        print(resStack)  
        
        if  tempSum == 1:            
            tempNode.val = 1
            nextNode = ListNode(0)
            tempNode.next = nextNode
            tempNode = tempNode.next
            
        for i in range(len(resStack) - 1):
            tempNode.val = resStack.pop()
            nextNode = ListNode(0)
            tempNode.next = nextNode
            tempNode = tempNode.next
        tempNode.val = resStack.pop()
            
        return res