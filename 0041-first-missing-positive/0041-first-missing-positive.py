class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        count = 1
        for i in nums:
            if(i<count):
                continue
            elif(count!=i):
                
                return count
            else:
                count+=1
            
        return count