# Definition for a binary tree node.
from typing import List, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


LEFT = 'LEFT'
RIGHT = 'RIGHT'
def _prepare_node(val_list: List[int]) -> Union[TreeNode, None]:
    wait_for_target_queue = []  # (node, LEFT or RIGHT)

    head = None
    for val in val_list:
        node = None
        if val:
            node = TreeNode(val=val)

        if wait_for_target_queue:
            parent_node, direct = wait_for_target_queue.pop(0)

            if direct == LEFT:
                parent_node.left = node
            else:  # right
                parent_node.right = node

        if node:
            head = node if head is None else head
            wait_for_target_queue.append((node, LEFT))
            wait_for_target_queue.append((node, RIGHT))

    return head


TEST_CASES = [
    (
        (_prepare_node([1, 2, 3]), _prepare_node([1, 2, 3])),
        True,
    ),
    (
        (_prepare_node([1, 2]), _prepare_node([1, None, 2])),
        False,
    ),
    (
        (_prepare_node([1, 2, 1]), _prepare_node([1, 1, 2])),
        False,
    ),
]

