# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.liste1=[]
        self.liste2=[]
    def get_last_values(self,tree,number):
        if tree==None:
            return 
        if tree.left==None and tree.right==None:
            if number==1:
                self.liste1.append(tree.val)
            else:
                self.liste2.append(tree.val)
        else:
            self.get_last_values(tree.left,number)
            self.get_last_values(tree.right,number)
            
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tmp1=root1
        tmp2=root2
        self.get_last_values(tmp1,1)
        self.get_last_values(tmp2,2)
        if self.liste1==self.liste2:
            return True
        else:
            return False