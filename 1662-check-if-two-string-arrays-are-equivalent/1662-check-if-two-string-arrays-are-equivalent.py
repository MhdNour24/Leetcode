class Solution:
    def __init__(self):
        self.word1=None
        self.word2=None
    def merging(self,liste):
        length=len(liste)
        word=""
        for word_ind in range(length):
            word+=liste[word_ind]
        return word
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        self.word1=self.merging(word1)
        self.word2=self.merging(word2)
        if self.word1==self.word2:
            return True
        return False