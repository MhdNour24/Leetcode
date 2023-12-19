class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, _ in ransom_count.items():
            if ransom_count[char]>magazine_count[char]:
                return False
        return True