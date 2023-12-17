import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size=len(nums)
        times=size//3#math.floor(size/3)
        hash_list=defaultdict(int) 
        out_put=[]
        for num in nums:
            hash_list[num]+=1
        for key,majority in hash_list.items():
            if majority>times:
                out_put.append(key)
        return out_put