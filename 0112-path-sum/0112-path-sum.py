# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        left=[]

        def back(root,t):
            if root is None:
                return 0
            left.append(root.val)
            if root.left is None and root.right is None:
                if sum(left)==t:
                    left.pop()
                    return -1
            s1=back(root.left,t)
            if s1==-1:
                left.pop()
                return -1
            s2=back(root.right,t)
            if s2==-1:
                left.pop()
                return -1
            left.pop()
            return 0

        return back(root,targetSum)==-1