class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length_s=len(s)
        length_t=len(t)
        j=0
        for i in range(length_s):
            if j>=length_t:
                break
            if s[i] == t[j]:
                j+=1
        return length_t-j