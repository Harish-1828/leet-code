# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(root1,root2):
            if root1 is not None and root2 is not None:
               return root1.val == root2.val and check(root1.left,root2.right) and check(root1.right,root2.left)

            elif root1 is not None and root2 is None:
                return False
            elif root2 is not None and root1 is None:
                return False
            else:
                return  True
        return check(root.left,root.right)