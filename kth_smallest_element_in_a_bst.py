class Solution:
    def __init__(self):
        self.inorder_vals = []
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # run inorder traversal:
        self.inorder_traversal(root)
        
        # edge cases:
        if len(self.inorder_vals) == 0:
            return -1
        if (k-1) >= len(self.inorder_vals):
            return -1
        
        # return kth smallest value (1-indexed):
        return self.inorder_vals[k-1]
    
    def inorder_traversal(self, root: TreeNode) -> None:
        # base case:
        if root is None:
            return
        
        # recursion:
        self.inorder_traversal(root.left)
        self.inorder_vals.append(root.val)
        self.inorder_traversal(root.right)