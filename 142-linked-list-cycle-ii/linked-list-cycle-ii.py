# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = set()

        while head:
            if head in h:
                return head      # Return the node where cycle starts

            h.add(head)
            head = head.next

        return None

