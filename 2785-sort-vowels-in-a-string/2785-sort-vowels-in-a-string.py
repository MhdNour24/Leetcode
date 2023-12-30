class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u"]
        new_vowels=[]
        new_s=""
        for i in s:
            if i.lower() in vowels:
                new_vowels.append(i)
        new_vowels.sort()
        for i in s:
            if i.lower() in vowels:
                vowel=new_vowels.pop(0)
                new_s+=vowel
            else:
                new_s+=i
        return new_s
        