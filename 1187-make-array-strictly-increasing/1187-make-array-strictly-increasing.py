class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        cache ={}
        arr2.sort()
        def dfs(i,prev) :
            if i == len(arr1):
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            temp = 1e9
            if i == 0 or prev < arr1[i]:
                temp = dfs(i+1,arr1[i])
            idx = bisect_right(arr2,prev)
            if idx == len(arr2):
                return temp
            temp = min(1+dfs(i+1,arr2[idx]),temp)
            cache[(i,prev)] = temp
            return temp
        res = dfs(0,-1)
        if res == 1e9:
            return -1
        else:
            return res