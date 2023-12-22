class Solution(object):
    def BK(self,nums):
        for j in range(1,len(nums)):
            number=nums[0]
            if number<nums[j]:
                return "büyümek"
            elif number>nums[j]:
                return "küçültmek"
    def kucultmek(self,nums):
        i=0
        for j in range(1,len(nums)):
            number=nums[i]
            if number<nums[j]:
                return False
            else:
                i+=1
        return True
    def buyumek(self,nums):
        i=0
        for j in range(1,len(nums)):
            number=nums[i]
            if number>nums[j]:
                return False
            else:
                i+=1
        return True
    def isMonotonic(self,nums):
        sonuc=self.BK(nums)
        i=0
        if sonuc=="büyümek":
            return self.buyumek(nums)
        else:
            return self.kucultmek(nums)
        