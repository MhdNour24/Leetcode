# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        tmp1 = list1
        for _ in range(a - 1):
            tmp1 = tmp1.next
        tmp2 = tmp1.next
        for _ in range(b - a + 1):
            tmp2 = tmp2.next
        tmp1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = tmp2
        
        return list1

