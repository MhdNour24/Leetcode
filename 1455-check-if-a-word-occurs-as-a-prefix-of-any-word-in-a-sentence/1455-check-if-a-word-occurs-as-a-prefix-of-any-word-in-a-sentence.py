class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        list_words=sentence.split()
        len_of_word=len(searchWord)
        for i in range(len(list_words)):
            if len_of_word<=len(list_words[i]) and searchWord ==list_words[i][0:len_of_word] :
                return i+1
        return -1