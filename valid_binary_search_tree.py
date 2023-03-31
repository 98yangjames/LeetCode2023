class Solution:
    def __init__(self) -> None:
        self.inorder_vals = []
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # run inorder traversal:
        self.inorderTraversal(root)
        
        # edge cases:
        if len(self.inorder_vals) == 0:
            return True
        if len(self.inorder_vals) == 1:
            return True
        
        # check if inorder traversal is sorted:
        for i in range(0, len(self.inorder_vals)-1):
            if self.inorder_vals[i] >= self.inorder_vals[i+1]:
                return False
        # inorder traversal is sorted:
        return True
    
    def inorderTraversal(self, root: Optional[TreeNode]):
        # base case:
        if root is None:
            return
        
        # recursion:
        self.inorderTraversal(root.left)
        self.inorder_vals.append(root.val)
        self.inorderTraversal(root.right)