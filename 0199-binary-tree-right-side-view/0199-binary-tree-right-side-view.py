# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def bfs(root):
            if root is None:
                return []
            queue=deque()
            queue.append(root)
            while queue:
                temp=[]
                size=len(queue)
                for i in range(size):
                    element=queue.popleft()
                    temp.append(element.val)
                    if element.left is not None:
                        queue.append(element.left)
                    if  element.right is not None:
                        queue.append(element.right)
                res.append(temp[-1])
        bfs(root)
        return res
