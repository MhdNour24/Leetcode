class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        i=0 
        j=0 
        n=len(s)
        count=0
        while j<n:
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                    count+=1 
                i+=1 
                j+=1
        return count