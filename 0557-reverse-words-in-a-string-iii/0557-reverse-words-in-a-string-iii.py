class Solution:
    def reverseWords(self, s: str) -> str:
        list_words=s.split()
        new_s=""
        for word in list_words:
            reversed_word=word[::-1]
            new_s+=reversed_word+" "
        new_s=new_s.strip()
        return new_s