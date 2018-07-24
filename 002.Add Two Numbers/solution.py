# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2 
        node3 = ListNode(0)
        sum = 0
        node_pre = node3 
        while (node1 or node2):
            val1 = node1.val if node1!=None else 0 
            val2 = node2.val if node2!=None else 0 
            digitsum = val1+val2+sum 
            if digitsum>=10:
                digitsum-=10; sum=1
            else:
                sum = 0
            
            node_new = ListNode(digitsum)
            node_pre.next = node_new 
            node_pre = node_new
            
            
            if node1!=None and node1.next!=None:
                node1 = node1.next 
            else:
                node1 = None 
            if node2!=None and node2.next!=None:
                node2 = node2.next
            else:
                node2= None
        
        if sum>0:
            node_new = ListNode(sum)
            node_pre.next = node_new
            
        return node3.next

if __name__=="__main__":

    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(9)
    l2 = ListNode(1)
    l2.next = ListNode(4)
    l2.next.next = ListNode(7)
    
    node = Solution().addTwoNumbers(l1,l2)
    while node:
        print(node.val)
        node = node.next


