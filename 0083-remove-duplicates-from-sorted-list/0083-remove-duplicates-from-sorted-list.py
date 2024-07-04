# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        value=head.val
        head=head.next
        dummy=ListNode(value)
        newHead=dummy
        lastValue=value
        while head:
            value=head.val
            if value!=lastValue:
                lastValue=value
                newHead.next=ListNode(value)
                newHead=newHead.next
            head=head.next
        return dummy
