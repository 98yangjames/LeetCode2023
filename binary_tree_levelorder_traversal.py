# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        q = deque()
        q.append(root)
        
        while q:
            levels_vals = []
            for i in range(len(q)):
                node = q.popleft()
                # If there is a value to pop. If not, don't append
                if node:
                    levels_vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels_vals:
                answer.append(levels_vals)
        return answer
                