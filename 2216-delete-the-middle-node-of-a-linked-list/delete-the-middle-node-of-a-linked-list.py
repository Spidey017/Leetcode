# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        a=[]

        while head!=None:
            a.append(head.val)
            head=head.next

       

        length=len(a)//2

        b=[]
        for i in range (0,len(a)):
            if i==length:
                continue 
            else:
                b.append(a[i])



        root=None

        for i in b:
            temp=ListNode(i)

            if root==None:
                root=temp
                head=temp

            else:
                root.next=temp
                root=root.next

            
        return head 

       


        

        

        
        