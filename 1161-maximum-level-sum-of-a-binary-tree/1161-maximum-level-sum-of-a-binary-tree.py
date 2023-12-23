# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic={}
    def search(self,tmp,t):
        if tmp!=None:
            value=tmp.val
            if t not in self.dic:
                self.dic[t]=value
            else:
                self.dic[t]+=value
            self.search(tmp.right,t+1)
            self.search(tmp.left,t+1)
            

        else:
            return
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        tmp=root
        self.search(tmp,1)
        enb=None
        k=None
        for i in self.dic.items():
            toplam=i[1]
            if enb==None:
                enb=toplam
                k=i[0]
            elif toplam>enb:
                enb=toplam
                k=i[0]
        return k