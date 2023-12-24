class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        output=[]
        length_nums=len(nums)
        for i in range(length_nums):
            count=sorted_nums.index(nums[i])
            output.append(count)
        return output