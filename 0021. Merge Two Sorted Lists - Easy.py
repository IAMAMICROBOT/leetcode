# Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val<=list2.val:    
            list3=ListNode(list1.val)
            list1=list1.next
        else:
            list3=ListNode(list2.val)
            list2=list2.next
        temp=list3

        while list1 and list2:
            if list1.val<=list2.val:
                temp.next=ListNode(list1.val)
                list1=list1.next
            else:
                temp.next=ListNode(list2.val)
                list2=list2.next
            temp=temp.next
        if list1:
            temp.next=list1
        if list2:
            temp.next=list2

        return list3


            
        
