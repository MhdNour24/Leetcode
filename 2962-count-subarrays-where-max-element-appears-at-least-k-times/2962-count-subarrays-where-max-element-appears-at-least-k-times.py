class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num=max(nums)
        dic=defaultdict(int)
        dic_index=defaultdict(int)
        counter=0
        count_max_number=0
        for right, num in enumerate(nums):
            dic[num]+=1
            if num==max_num:
                dic_index[count_max_number]=right
                count_max_number+=1
            if dic[max_num]>=k:
                a=dic[max_num]-k
                counter+=dic_index[a]+1
        return counter
