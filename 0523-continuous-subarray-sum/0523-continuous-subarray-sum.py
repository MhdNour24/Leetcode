class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        length=len(nums)
        prefixList=[0]*length
        prefixList[0]=nums[0]%k
        dic={}
        dic[prefixList[0]]=0
        for i in range(1,length):
            prefixList[i]=(nums[i]+prefixList[i-1])%k
            a=prefixList[i]
            if a==0:
                return True
            if a in dic:
                if i-dic[a]>1:
                    return True
            else:
                dic[a]=i
        return False
                