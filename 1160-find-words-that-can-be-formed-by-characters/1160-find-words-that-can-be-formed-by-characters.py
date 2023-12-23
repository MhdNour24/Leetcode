class Solution:
    def __init__(self):
        self.chars_hash_table=defaultdict(int)
    def good_or_not(self,word):
        count=0
        hash_table=self.chars_hash_table.copy()
        for letter in word:
            if letter not in hash_table:
                return 0
            else:
                count+=1
                hash_table[letter]-=1
                if hash_table[letter]==0:
                    del hash_table[letter]
        return count
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter=0
        for char in chars:
            self.chars_hash_table[char]+=1
        for word in words:
            counter+=self.good_or_not(word)
        return counter
