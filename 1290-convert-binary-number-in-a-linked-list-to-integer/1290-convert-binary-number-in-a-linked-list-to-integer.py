# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp=head
        s=""
        while tmp:
            num=tmp.val
            tmp=tmp.next
            s+=str(num)
        tens=0
        toplam=0
        while s:
            last_num=s[-1]
            toplam+=int(last_num)*(2**tens)
            tens+=1
            s=s[:-1]
        return toplam