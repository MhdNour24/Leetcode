# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_liste=[]
        even_liste=[]
        size=0
        a=1
        while head!=None:
            value=head.val
            head=head.next
            size+=1
            if a%2==0:
                even_liste.append(value)
            else:
                odd_liste.append(value)
            a+=1
        new_head=None
        while size:
            if odd_liste:
                num=odd_liste.pop(0)
                if new_head==None:
                    new_head=ListNode(num)
                else:
                    tmp=new_head
                    while tmp.next!=None:
                        tmp=tmp.next
                    tmp.next=ListNode(num)

            else:
                num=even_liste.pop(0)
                if new_head==None:
                    new_head=ListNode(num)
                else:
                    tmp=new_head
                    while tmp.next!=None:
                        tmp=tmp.next
                    tmp.next=ListNode(num)
            size-=1
        return new_head