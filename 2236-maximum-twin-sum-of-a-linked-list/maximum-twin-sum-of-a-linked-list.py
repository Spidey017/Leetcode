# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans=[]
        while head!=None:
            ans.append(head.val)
            head=head.next

        
        i=0
        j=len(ans)-1
        max=0

        while i<j:
            if ans[i]+ans[j]>max:
                max=ans[i]+ans[j]
            i=i+1
            j=j-1

        return max