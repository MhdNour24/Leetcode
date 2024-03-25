class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates_nums=[]
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
            if dic[i]>1 and i not in duplicates_nums:
                duplicates_nums.append(i)
        return duplicates_nums