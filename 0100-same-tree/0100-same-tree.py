# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
    def dfs(self,tree,a):
        if tree != None:
            self.arr.append(tree.val)
            self.dfs(tree.left,False)
            self.dfs(tree.right,True)
        else:
            if a:
                self.arr.append("None")
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.dfs(p,True)
        tree1=self.arr
        self.arr=[]
        self.dfs(q,True)
        tree2=self.arr
        if tree1==tree2:
            return True
        else:
            return False