class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        liste=[]
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    liste.append((i,j))
                j+=1
            i+=1
        return len(liste)