class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic_target=defaultdict(int)
        dic_arr=defaultdict(int)
        for i in range(len(target)):
            dic_target[target[i]]+=1
            dic_arr[arr[i]]+=1
        
        for value in dic_target:
            if dic_target[value]!=dic_arr[value]:
                return False
            del dic_arr[value]
        if len(dic_arr)>0:
            return False
        return True
        
        