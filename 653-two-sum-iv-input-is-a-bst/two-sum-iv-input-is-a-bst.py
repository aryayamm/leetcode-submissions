# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def dfs(root):
            nonlocal arr
            if root is None:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
            return
        dfs(root)
        l = 0
        r = len(arr)-1
        while l < r:
            cur = arr[l] + arr[r]
            if cur == k:
                return True
            if cur < k:
                l +=1
            else:
                r -= 1
        return False