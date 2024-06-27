class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length=len(nums)
        c=0
        for i in range(length):
            num=nums[i]
            if num%2==1:
                pass
            else:
                nums[c],nums[i]=num,nums[c]
                c+=1
        return nums