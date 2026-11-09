# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        total = 0
        def dfs(root):
            nonlocal total
            if root.left != None:
                if root.left.left == None and root.left.right == None:
                    total += root.left.val
                else:
                    dfs(root.left)
            if root.right != None:
                dfs(root.right)
            return
        dfs(root)
        return total