class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        dic=sorted(dic.items(), key=lambda item: item[1],reverse=True)
        counter=0
        last_value=dic[0][1]
        for value,count in dic:
            if count==last_value:
                counter+=count
            else:
                break
        return counter