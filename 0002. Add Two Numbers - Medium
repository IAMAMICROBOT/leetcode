# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=[]
        a2=[]
        n1=0
        n2=0
        while l1:
            a1.append(l1.val)
            l1=l1.next
        while l2:
            a2.append(l2.val)
            l2=l2.next
        n1 = int(''.join(map(str, reversed(a1))))
        n2 = int(''.join(map(str, reversed(a2))))
        n3=n1+n2
        l3 = ListNode(0)
        curr = l3
        for digit in str(n3)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return l3.next
