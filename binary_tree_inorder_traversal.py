class Solution:
    # solution #1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case:
        if root is None:
            return []
        
        # recursion:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



    # solution #2:
    """
    def __init__(self) -> None:
        self.vals = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case:
        if root is None:
            return
        
        # recursion:
        self.inorderTraversal(root.left)
        self.vals.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.vals
    """