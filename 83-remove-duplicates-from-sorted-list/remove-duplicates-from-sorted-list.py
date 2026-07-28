
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        a=[]

        while head!=None:
            a.append(head.val)
            head=head.next

        b=[]
        for i in a:
            if i not in b:
                b.append(i)

        head=None
        root=None

        for i in b:
            temp=ListNode(i)
            if head==None:
                head=temp
                root=temp

            else:
                root.next=temp
                root=root.next

        return head


           
        