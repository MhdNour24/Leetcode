class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for karakter,count in dic.items():
            if count==1:
                return s.index(karakter)
        return -1