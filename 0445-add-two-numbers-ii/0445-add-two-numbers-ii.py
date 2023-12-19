# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            if not head:
                return 0
            return 1+length(head.next)
        len1=length(l1)
        len2=length(l2)
        if len1<len2:
            pad=l1
            no_pad=l2
            smaller=len1
            larger=len2
        else:
            pad=l2
            no_pad=l1
            larger=len1
            smaller=len2
        while smaller<larger:
            node=ListNode(0)
            node.next=pad
            pad=node
            smaller+=1
        l1,l2=pad,no_pad
        def rec(h1,h2):
            if h1.next and h2.next:
                carry,node=rec(h1.next,h2.next)
            else:
                carry,node=0,None
            n_node=ListNode((carry+h1.val+h2.val)%10)
            n_c=(carry+h1.val+h2.val)//10
            n_node.next=node
            return n_c,n_node 
        carry,head=rec(l1,l2)
        if carry==1:
            n_h=ListNode(carry)
            n_h.next=head
            return n_h
        return head


        
        
        