# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        table = set()
        ans = False
        def dfs(root):
            nonlocal table,k,ans
            if root == None:
                return
            if k - root.val in table:
                ans = True
                return
            table.add(root.val)
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return ans