class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            i=0
            for j in nums:
                if j<target:
                    i+=1
                else:
                    break
            return i