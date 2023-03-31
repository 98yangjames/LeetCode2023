class Solution:
    # solution #1:
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case:
        if root is None:
            return 0
        
        # recursion:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    """


    # solution #2:
    def __init__(self):
        self.max_depth = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth_helper(root, 0)
        
        return self.max_depth
    
    def max_depth_helper(self, root: Optional[TreeNode], depth: int) -> None:
        # base case:
        if root is None:
            return
        
        # increment depth:
        depth += 1
        if depth > self.max_depth:
            self.max_depth = depth
        
        # recursion:
        self.max_depth_helper(root.left, depth)
        self.max_depth_helper(root.right, depth)