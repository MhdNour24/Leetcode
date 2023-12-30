class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        count=0
        dic={}
        for i in range(n):
            col=[grid[j][i] for j in range(n)]
            if str(col) in dic:
                dic[str(col)]+=1
            else:
                dic[str(col)]=1
        for i in range(n):
            row=grid[i]
            if str(row) in dic:
                count+=dic[str(row)]
        return count