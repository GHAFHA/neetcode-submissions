"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_nodes = {}

        def dfs(n):
            if n in cloned_nodes:
                return cloned_nodes[n]

            clone = Node(n.val)
            cloned_nodes[n] = clone
            clone.neighbors = [dfs(neigh) for neigh in n.neighbors]

            return clone

        return dfs(node)