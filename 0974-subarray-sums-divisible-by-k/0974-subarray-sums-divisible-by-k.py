class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashTable = {}
        counter = 0
        length = len(nums)
        prefixList = [0] * length
        prefixList[0] = nums[0]%k
        if prefixList[0]==0:
            counter+=1
        hashTable[prefixList[0]]=1

        for i in range(1, length):
            prefixList[i] = (nums[i] + prefixList[i - 1])%k
            a=prefixList[i]
            if a==0:
                counter+=1
            if a in hashTable:
                counter+=hashTable[a]
                hashTable[a]+=1
            else:
                hashTable[a]=1

        return counter
