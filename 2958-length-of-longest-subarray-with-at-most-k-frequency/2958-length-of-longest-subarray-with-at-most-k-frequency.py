class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        length=len(nums)
        max_len_good=0
        dic=defaultdict(int)
        c=0
        l=0
        for num in nums:
            dic[num]+=1
            l+=1
            if dic[num]>k:
                max_len_good=max(max_len_good,l-1)
                while dic[num]>k:
                    dic[nums[c]]-=1
                    c+=1
                    l-=1
        max_len_good=max(max_len_good,l)
        return max_len_good
