class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_t=len(t)
        if len_s != len_t:
            return False
        dic_s={}
        dic_t={}
        for i in range(len_s):
            if s[i] not in dic_s and t[i] not in dic_t:
                dic_s[s[i]]=i
                dic_t[t[i]]=i
            elif  s[i] in dic_s and t[i]  in dic_t:
                if dic_s[s[i]]!=dic_t[t[i]]:
                    return False
                else:
                    dic_s[s[i]]=i
                    dic_t[t[i]]=i
            else:
                return False
        return True