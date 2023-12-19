class Solution(object):
    def thirdMax(self, nums):
        A=list(set(nums))
        A.sort()
        A=A[::-1]
        if len(A)<3:
            return A[0]
        else:
            return A[2]