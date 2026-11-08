# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return [str(root.val)]
        arr = []
        def dfs(root, s):
            nonlocal arr
            if root == None:
                return
            s += f"->{root.val}"
            if root.left == None and root.right == None:
                arr.append(s)
                return
            dfs(root.left, s)
            dfs(root.right, s)
            return
        dfs(root.left,f"{root.val}")
        dfs(root.right,f"{root.val}")
        return arr