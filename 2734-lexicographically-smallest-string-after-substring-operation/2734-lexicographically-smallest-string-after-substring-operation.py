class Solution:


    def smallestString(self, s: str) -> str:
        count=0
        for i in s:
            if i=="a":
                count+=1
        if count==len(s):
            return s[:count-1]+"z"
        characters = list(s)
        for i in range(len(characters)):
            j = i
            while j < len(characters) and characters[j] == 'a':
                j += 1
            if j < len(characters) and characters[j] != 'a':
                k = j
                while k < len(characters) and characters[k] != 'a':
                    k += 1
                for l in range(j, k):
                    characters[l] = chr(ord(characters[l]) - 1)
                break
        return ''.join(characters)