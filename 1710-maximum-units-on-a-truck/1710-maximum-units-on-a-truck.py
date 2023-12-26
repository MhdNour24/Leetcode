class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        l=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        toplam=0
        truckSize=truckSize
        #[[5, 10], [3, 9], [4, 7], [2, 5]]
        while truckSize!=0 and l:
            if l[0][0]<=truckSize:
                toplam+=l[0][0]*l[0][1]
                truckSize-=l[0][0]
                del l[0]
            else:
                toplam+=truckSize*l[0][1]
                truckSize=0
        return toplam

