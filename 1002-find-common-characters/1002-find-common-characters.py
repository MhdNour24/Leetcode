class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_word = min(words)
        words.remove(min_word)
        for char in min_word[:]: # shallow copy by slice
            for idx_w, word in enumerate(words):
                if char not in word and (idx_w == len(words) or char in min_word):
                    min_word = min_word.replace(char, "", 1)
                    break
                else:
                    words[idx_w] = words[idx_w].replace(char, "", 1)
        return min_word