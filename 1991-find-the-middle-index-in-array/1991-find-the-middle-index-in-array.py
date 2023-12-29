class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        top=0
        for i in range(len(nums)):
            if top==(sum_nums-nums[i]-top):
                return i
            else:
                top+=nums[i]
        return -1