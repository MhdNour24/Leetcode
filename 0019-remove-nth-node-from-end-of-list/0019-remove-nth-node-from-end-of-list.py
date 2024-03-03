# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp=head
        length=0
        nums=[]
        while tmp!=None:
            length+=1
            value=tmp.val
            nums.append(value)
            tmp=tmp.next
        nums.pop(length-n)
        if len(nums)==0:
            k=ListNode()
            k=k.next
            return k
        new_head=ListNode(nums.pop(-1))
        
        while nums:
            new_node=ListNode(nums.pop(-1))
            new_node.next=new_head
            new_head=new_node
        return new_head