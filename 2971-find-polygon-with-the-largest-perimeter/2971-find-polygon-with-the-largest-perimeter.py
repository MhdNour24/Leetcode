class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        nums.sort()
        length=len(nums)
        if length<3:
            return -1
        for i in range(length-1,-1,-1):
            new_sum=sum_nums-nums[i]
            # if new_sum<=nums[i]:
            #     sum_nums=new_sum
            # else:
            #     return sum_nums
            if new_sum>nums[i]:
                return sum_nums
            else:
                sum_nums=new_sum
        return -1