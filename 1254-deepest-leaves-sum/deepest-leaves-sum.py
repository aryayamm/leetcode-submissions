# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        tot = 0
        k = 0
        def dfs(root, n):
            nonlocal tot, k
            if root.left == None and root.right == None:
                if n == k:
                    tot += root.val
                if n > k:
                    k = n
                    tot = root.val
                return
            if root.left == None:
                dfs(root.right, n+1)
                return
            if root.right == None:
                dfs(root.left, n+1)
                return
            dfs(root.left,n +1)
            dfs(root.right, n+1)
            return
        dfs(root, 0)
        return tot
                