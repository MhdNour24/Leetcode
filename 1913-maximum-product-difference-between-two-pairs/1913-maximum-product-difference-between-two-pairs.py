class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        length=len(nums)
        nums.sort()
        if length<4:
            return 0
        else:
            return (nums[-1]*nums[-2])-(nums[0]*nums[1])