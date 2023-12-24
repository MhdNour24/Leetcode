# Memory Usage: 13.9 MB, less than 75.94% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        for i in range(2,len(arr)):
            if arr[i-2]-arr[i-1]!= arr[i-1]-arr[i]:
                return False
        return True  