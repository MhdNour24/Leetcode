class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            list.append(sum)
        return list