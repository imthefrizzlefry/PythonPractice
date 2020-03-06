# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c = 0) -> ListNode:
        val = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret

myList = ListNode(2)
myList.next = ListNode(4)
myList.next.next = ListNode(3)

myList2 = ListNode(5)
myList2.next = ListNode(6)
myList2.next.next = ListNode(4)
mySolution = Solution()
resultList = mySolution.addTwoNumbers(l1=myList, l2=myList2)

print(resultList)