class Solution:
    def __init__(self):
        self.LCA = None
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base case:
        if root is None:
            return
        
        # recursion:
        # found LCA:
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            self.LCA = root
            return self.LCA
        else:
            # left subtree:
            if root.val > min(p.val, q.val):
                self.lowestCommonAncestor(root.left, p, q)
            # right subtree:
            elif root.val < max(p.val, q.val):
                self.lowestCommonAncestor(root.right, p, q)
        
        return self.LCA