# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head

        a=[]

        while head!=None:
            a.append(head.val)
            head=head.next

        a.sort()
        head=l

        for i in a:
            head.val=i
            head=head.next

        head=l
        return head
       
        