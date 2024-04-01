class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s=s.split()
        last_word=list_s[-1]
        return  len(last_word)