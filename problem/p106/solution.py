from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]
        root_node = TreeNode(root_val)

        left_inorder, right_inorder = self.group_inorder_by_root(inorder, root_val)

        left_inorder_len = len(left_inorder)
        left_postorder = postorder[:left_inorder_len]
        right_postorder = postorder[left_inorder_len:left_inorder_len + len(right_inorder)]

        root_node.left = self.buildTree(inorder=left_inorder, postorder=left_postorder)
        root_node.right = self.buildTree(inorder=right_inorder, postorder=right_postorder)

        return root_node

    @staticmethod
    def group_inorder_by_root(inorder: List, root: int) -> Tuple[List, List]:  # return left group, right group
        root_idx = inorder.index(root)

        return inorder[:root_idx], inorder[root_idx + 1:]

