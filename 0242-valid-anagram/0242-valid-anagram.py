class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_t=len(t)
        if len_s!=len_t:
            return False
        dic_s=defaultdict(int)
        dic_t=defaultdict(int)
        for i in range(len_s):
            dic_s[s[i]]+=1
            dic_t[t[i]]+=1
        len_dic_s=len(dic_s)
        len_dic_t=len(dic_t)
        if len_dic_s!=len_dic_t:
            return False
        for i in dic_s:
            if dic_s[i]!=dic_t[i]:
                return False
        return True