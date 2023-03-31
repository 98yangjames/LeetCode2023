# solution #1:
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # base case:
    if root is None:
        return []
    
    # recursion:
    return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]



# solution #2:
"""
def __init__(self):
    self.vals = []

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # base case:
    if root is None:
        return
    
    # recursion:
    self.postorderTraversal(root.left)
    self.postorderTraversal(root.right)
    self.vals.append(root.val)

    return self.vals
"""