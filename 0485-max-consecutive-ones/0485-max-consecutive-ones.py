class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        enb=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            if nums[i]==0:
                if count>enb:
                    enb=count
                count=0
        if count>enb:
            enb=count
    
        return enb