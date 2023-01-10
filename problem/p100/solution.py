from typing import Optional, Union

from problem.p100.test_case import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs_compare_node(p, q)

    @classmethod
    def dfs_compare_node(cls, node1: Union[TreeNode, None], node2: Union[TreeNode, None]) -> bool:
        if node1 is None or node2 is None:
            return node1 == node2

        if node1.val != node2.val:
            return False
        else:
            return cls.dfs_compare_node(node1.left, node2.left) and cls.dfs_compare_node(node1.right, node2.right)




