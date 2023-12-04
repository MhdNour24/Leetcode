
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m, left,right, d, count = [0]*128, 0, 0, 0,0
        while right < len(s):
            if m[ord(s[right])] > 0: count = count + 1            
            m[ord(s[right])] += 1
            right=right+1
            while count > 0:
                if m[ord(s[left])] > 1: count-=1                
                m[ord(s[left])] -= 1
                left = left + 1      
            d = max(d, right - left)
        return d 