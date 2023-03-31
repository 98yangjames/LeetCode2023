class Solution:
    # solution #1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case:
        if root is None:
            return []
        
        # recursion:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    


    # solution #2:
    """
    def __init__(self) -> None:
        self.vals = []
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case:
        if root is None:
            return
        
        # recursion:
        self.vals.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.vals
    """