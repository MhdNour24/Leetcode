class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table=defaultdict(int)
        counter=0
        for jewel in jewels:
            ord_jewel=ord(jewel)
            hash_table[ord_jewel]+=1
        
        for stone in stones:
            ord_stone=ord(stone)
            count=hash_table[ord_stone]
            if count!=0:
                counter+=1
        return counter