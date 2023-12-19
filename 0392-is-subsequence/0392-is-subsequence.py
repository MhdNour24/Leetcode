class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_word=0
        c=0
        len_s=len(s)
        if len_s==0:
            return True
        for i in t:
            if i==s[c]:
                len_word+=1
                c+=1
                if len_s==c:
                    return True
        return False
