# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ans=[]

        while head!=None:
            ans.append(head.val)
            head=head.next

        ans.pop(-n)

        head=None
        root=None

        for i in ans:
            temp=ListNode(i)

            if head==None:
                head=temp
                root=temp
            else:
                root.next=temp
                root=root.next

        return head


        