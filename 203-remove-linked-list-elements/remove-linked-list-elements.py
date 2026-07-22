# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        a=[]

        while head!=None:
            if head.val!=val:
                a.append(head.val)
            head=head.next


        root=None

        for i in a:
            temp=ListNode(i)

            if root==None:
                root=temp
                head=temp

            else:
                root.next=temp
                root=root.next
        return head


        
                
        