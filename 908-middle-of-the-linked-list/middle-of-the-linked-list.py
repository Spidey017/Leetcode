# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l=head

        length=0

        while head!=None:
            
            length=length+1
            head=head.next

        length=length//2+1

        head=l

        count=0

        while head!=None:
            count=count+1
            if count==length:
                return head

            head=head.next


        


        