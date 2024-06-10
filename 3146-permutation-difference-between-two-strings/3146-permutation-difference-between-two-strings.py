class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic_t={}
        len_t=len(t)
        for i in range(len_t):
            dic_t[t[i]]=i
        permutation=0
        for i in range(len_t):
            permutation+= abs(i-dic_t[s[i]])
        
        return permutation 
