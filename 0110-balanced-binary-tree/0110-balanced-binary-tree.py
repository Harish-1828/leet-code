# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None :
                return 0
            else:
                left_h=height(root.left)
                if left_h==-1:
                    return -1
                right_h=height(root.right)
                if right_h==-1:
                    return -1
                if abs(left_h-right_h)>1:
                    return -1
                return 1+max(left_h,right_h)
        val=height(root)
        if val < 0:
            return False
        return True


        