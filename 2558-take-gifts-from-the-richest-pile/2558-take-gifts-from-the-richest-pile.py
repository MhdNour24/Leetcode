class Solution:
    def find_max_element(self,gifts,length) :
        max_number=-float("inf")
        index=0
        for i in range(length):
            if gifts[i]>max_number:
                max_number=gifts[i]
                index=i
        return index
    def pickGifts(self, gifts: List[int], k: int) -> int:
        length=len(gifts)
        for i in range(k):
            index=self.find_max_element(gifts,length)
            gifts[index]=int(gifts[index]**(1/2))
        return sum(gifts)