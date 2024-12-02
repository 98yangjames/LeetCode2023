# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root, currentSum, targetSum):
    if root is None:
        return False
    currentSum += root.val

    if not root.left and not root.right:
        if currentSum == targetSum:
            return True
        else:
            return False
    return inorderTraversal(root.left, currentSum, targetSum) or inorderTraversal(root.right, currentSum, targetSum)
    

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        val = inorderTraversal(root, 0, targetSum)
        return val

    