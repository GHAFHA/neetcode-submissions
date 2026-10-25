# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # breaking the problem down to make it easier to solve
    def visit(self, node, depth, levels):
        if node is None:
            return

        if depth == len(levels):
            levels.append([])
        
        levels[depth].append(node.val)

        self.visit(node.left, depth + 1, levels)
        self.visit(node.right, depth + 1, levels)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.visit(root, 0, levels)
        return levels