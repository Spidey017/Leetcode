# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head == None:
            return head

        l = head

        a = []
        while head != None:
            a.append(head.val)
            head = head.next

        i = left - 1
        j = right - 1

        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        head=l

        i=0
        while head!=None:
            head.val=a[i]
            head=head.next
            i=i+1

        head=l
        return head