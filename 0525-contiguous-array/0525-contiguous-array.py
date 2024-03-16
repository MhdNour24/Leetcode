class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length=0
        len_nums=len(nums)
        dic={0:-1}
        sum_nums=0
        for i in range(len_nums):
            if nums[i]==1:
                sum_nums+=1
            else:
                sum_nums-=1

            if sum_nums not in dic:
                dic[sum_nums]=i
            else:
                max_length=max(max_length,i-dic[sum_nums])

        return max_length