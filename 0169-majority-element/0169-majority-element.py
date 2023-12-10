class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        enb=0
        for i in dic.items():
            if i[1]>enb:
                k=i[0];enb=i[1]
        return k
            