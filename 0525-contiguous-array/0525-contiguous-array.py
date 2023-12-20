class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        hash_table={0:-1}
        toplam=0
        enb=0
        for i in range(n):
            if nums[i]==1:
                toplam+=1
            else:
                toplam-=1
            try:
                k=i-hash_table[toplam]
                if k>enb:
                    enb=k
            except:
                hash_table[toplam]=i
        return enb