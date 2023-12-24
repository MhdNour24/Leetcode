class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[]
        for i in range(0,length,2):
            pair_of_elements=[nums[i],nums[i+1]]
            freq=pair_of_elements[0]
            val=pair_of_elements[1]
            new_list=[val]*freq
            result+=new_list
        return result