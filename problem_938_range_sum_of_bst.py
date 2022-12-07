from typing import List, Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._low = 0
        self._high = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # init
        self._low = low
        self._high = high

        return self.sum_node(root)

    def sum_node(self, node: Union[TreeNode, None]):
        if node is None:
            return 0

        if self._high >= node.val >= self._low:
            return node.val + self.sum_node(node.left) + self.sum_node(node.right)
        else:
            return self.sum_node(node.left) + self.sum_node(node.right)


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (([10, 5, 15, 3, 7, None, 18], 7, 15), 32),
        (([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10), 23),
    ]


NODE_LIST = []
def make_tree_node(val_list: List) -> TreeNode:
    for val in val_list:
        if val:
            NODE_LIST.append(TreeNode(val=val))
        else:
            NODE_LIST.append(None)

    node_list_len = len(NODE_LIST)
    for idx_1, node in enumerate(NODE_LIST, 1):
        if node is None:
            continue

        left_idx = 2 * idx_1 - 1
        right_idx = 2 * idx_1

        if left_idx < node_list_len:
            node.left = NODE_LIST[left_idx]
        if right_idx < node_list_len:
            node.right = NODE_LIST[right_idx]

    return NODE_LIST[0]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        val_list, low, high = t_input
        root = make_tree_node(val_list=val_list)
        result = sol.rangeSumBST(root, low=low, high=high)
        NODE_LIST = []

        print(f'Is sum expect ? `{result == t_output}`')
