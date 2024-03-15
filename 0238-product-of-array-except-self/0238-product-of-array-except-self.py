from numpy import array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[1]*length
        result=array(result)
        for i in range(length):
            k=result[i]
            result=result*nums[i]
            result[i]=k
        return list(result)