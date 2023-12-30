# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = 0

    def average(self, node):
        if node is None:
            return (0, 0)
        left_sum, left_count = self.average(node.left)
        right_sum, right_count = self.average(node.right)
        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1
        if total_sum // total_count == node.val:
            self.counter += 1
        return total_sum, total_count

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.average(root)
        return self.counter


