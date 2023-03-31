class Solution:
    def __init__(self):
        self.num_good_nodes = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        # edge case:
        if root is None:
            return 0
        
        self.good_nodes_helper(root, root.val)
        
        return self.num_good_nodes
    
    def good_nodes_helper(self, root: TreeNode, max_val: int) -> None:
        # base case:
        if root is None:
            return
        
        # if root is a good node:
        if root.val >= max_val:
            # update max value of ancestors:
            max_val = root.val
            # increment number of good nodes:
            self.num_good_nodes += 1
        
        # DFS recursion:
        self.good_nodes_helper(root.left, max_val)
        self.good_nodes_helper(root.right, max_val)