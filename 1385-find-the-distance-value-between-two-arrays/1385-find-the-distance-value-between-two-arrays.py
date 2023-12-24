class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value=0
        for i in arr1:
            k=True
            for j in arr2:
                if abs(i-j)<=d:
                    k=False
                    break
            if k:
                distance_value+=1
        return distance_value
