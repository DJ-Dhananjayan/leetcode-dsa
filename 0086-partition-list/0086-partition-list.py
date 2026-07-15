# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lhead=ltail=ListNode(0)
        bhead=btail=ListNode(0)
        while head:
            if head.val<x:
                ltail.next=head
                ltail=ltail.next
            else :
                btail.next=head
                btail=btail.next
            head=head.next
        btail.next=None
        ltail.next=bhead.next
        return lhead.next