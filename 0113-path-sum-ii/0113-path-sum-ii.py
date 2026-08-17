# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res=[]
        def back(root,sum,path):
            if sum==target and ( root.left is None and root.right is None):
                path.append(root.val)
                res.append(path[:])
                return
            elif root is None:
                return
            else:
                if root.left is not None:
                    back(root.left,sum+root.left.val,path+[root.val])
                if root.right is not None:
                    back(root.right,sum+root.right.val,path+[root.val])
        if root is None:
            return []
        back(root,root.val,[])
        if res:
            return res
        return []        

