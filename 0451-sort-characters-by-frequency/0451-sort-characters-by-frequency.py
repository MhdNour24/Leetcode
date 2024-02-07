from collections import defaultdict 
class Solution:
    def frequencySort(self, s: str) -> str:
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1
        dic = sorted(dic.items(), key=lambda x: x[1],reverse=True)
        new_string=""
        for i in dic:
            char,count=i[0],i[1]
            new_string+=f"{char*count}"
        return new_string