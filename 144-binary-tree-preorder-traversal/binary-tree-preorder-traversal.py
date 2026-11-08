# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        pre = []
        post = []
        mid = []
        def dfs(root):
            nonlocal pre, post, mid
            if root == None:
                return
            pre.append(root.val)
            dfs(root.left)
            mid.append(root.val)
            dfs(root.right)
            post.append(root.val)
            return
        dfs(root)
        print(pre)
        print(post)
        print(mid)
        return pre