class Solution:
    def is_palindrome(self,word):
        length=len(word)
        c=-1
        for i in range(0,length//2):
            if word[i]!=word[c]:
                return False
            c-=1
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        length=len(words)
        for i in range(length):
            palindrome=self.is_palindrome(words[i])
            if palindrome:
                return words[i]
        return ""