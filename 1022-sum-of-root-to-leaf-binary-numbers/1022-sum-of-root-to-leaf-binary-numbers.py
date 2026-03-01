# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sums=0
        res=[]
        def dfs(root,path):
            nonlocal sums
            if root is None:
                return
            path.append(root.val)
            if root.left is None and root.right is None:
                s = "".join(map(str, path))
                n=int(s,2)
                sums=sums+n
            else:
                dfs(root.left,path)
                dfs(root.right,path)
            path.pop()

        dfs(root,[])
        return sums

