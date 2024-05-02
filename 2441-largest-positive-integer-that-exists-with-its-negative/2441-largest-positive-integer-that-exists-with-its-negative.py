class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        length=len(nums)
        dic=defaultdict(int)
        c=1
        a=-1
        for i in range(length):
            num=nums[i]
            if num<0:
                dic[num]=c
                c+=1
            elif num>0:
                negative_num=num-num*2
                if dic[negative_num]!=0:
                    a=num
        return a