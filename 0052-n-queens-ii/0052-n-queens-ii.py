
class Solution:
    
    def __init__(self):
        self.ans = 0
        
    def recurse(self,visited,ind):
           
        for i in range(self.n):
            
            if visited[ind][i] == False:
             
                if ind == self.n-1:
                    self.ans += 1
                    return
                
                new = [visited[h][:] for h in range(self.n)]
                for k in range(self.n):
                    new[ind][k] = True
                    new[k][i] = True
                    
                for r,c in {(1,1),(-1,-1),(1,-1),(-1,1)}:
                    ar,ac = ind + r,i + c
                    while 0 <= ar < self.n and 0 <= ac < self.n:
                        new[ar][ac] = True
                        ar,ac = ar+r,ac+c
                self.recurse(new,ind+1)
                
    def totalNQueens(self, n: int) -> int:
        self.n = n
        visited = [[False]*n for _ in range(n)]
        self.recurse(visited,0)
        return self.ans
        