
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[a],nums[i]=nums[i],nums[a]
                a+=1
        return(nums)
        #================================
        #Method-2
        #=================================
			# for i in nums:
			# if i==0:
			# 	nums.remove(i)
			# 	nums.append(0)
			# return(nums)