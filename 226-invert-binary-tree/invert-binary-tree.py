# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root == None:
            return None
        def dfs(root):
            if root == None:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            dfs(root.left)
            dfs(root.right)
            return

        dfs(root)
        return root