class Solution:
    def next(self, nums: List[int]) -> int:
        i=0
        cnt=0
        res=[]
        while(i<len(nums)):
            if cnt%2==0:
                res.append(min(nums[i],nums[i+1]))
            else:
                res.append(max(nums[i],nums[i+1]))
            cnt+=1
            i+=2
        return res

    def minMaxGame(self, nums: List[int]) -> int:
        while(len(nums)>1):
            nums=Solution.next(self,nums)
        return nums[0]