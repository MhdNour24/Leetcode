from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.liste=[]
    def get_depth(self,tree):
        if tree==None:
            return 
        else:
            value=tree.val
            self.liste.append(value)
            right=tree.right
            left=tree.left
            self.get_depth(right)
            self.get_depth(left)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        tmp=root
        self.get_depth(tmp)
        count_dic=Counter(self.liste)
        count_dic=dict(sorted(count_dic.items(), key=lambda item: item[1],reverse=True))
        liste=[]
        if count_dic:
            val=None
            for key,value in count_dic.items():
                if val==None:
                    val=value
                    liste.append(key)
                
                elif val==value:
                    liste.append(key)

                elif value!=val:
                    break
            return liste

