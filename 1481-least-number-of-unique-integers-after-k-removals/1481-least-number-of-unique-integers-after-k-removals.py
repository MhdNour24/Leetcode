from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        dic=dict(sorted(dic.items(),key=lambda x:x[1]))
        while k!=0:
            first_number=next(iter(dic))
            dic[first_number]-=1
            if dic[first_number]==0:
                del dic[first_number]
            k-=1
        return len(dic)