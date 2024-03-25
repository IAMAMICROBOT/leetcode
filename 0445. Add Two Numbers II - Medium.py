# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nex
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1 is not None:
            s1+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            s2+=str(l2.val)
            l2=l2.next
        s3=str(int(s1)+int(s2))
        res=ListNode()
        curr=res
        for i in s3:
            curr.next=ListNode(int(i))
            curr=curr.next
        return res.next
