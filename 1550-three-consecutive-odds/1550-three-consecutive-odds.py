class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter=0
        for i in range(len(arr)):
            if arr[i]%2==1:
                counter+=1
                if counter==3:
                    return True
            else:
                counter=0
        return False