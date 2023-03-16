from typing import List, Union

from problem.p106.solution import TreeNode


def verify(result: TreeNode, test_output: List[Union[int, None]]) -> bool:
    # list all val in tree
    node_val_list = []
    iter_level = [result]
    while iter_level:
        next_iter_level = []
        empty_node_buffer = []

        for node in iter_level:
            node_val_list.append(node.val)

            if node.right:
                next_iter_level.extend(empty_node_buffer)
                empty_node_buffer.clear()

                next_iter_level.extend([
                    node.left or TreeNode(None),
                    node.right,
                ])
            else:
                for child in [node.left, node.right]:
                    if child:
                        next_iter_level.extend(empty_node_buffer)
                        empty_node_buffer.clear()

                        next_iter_level.append(child)
                    else:
                        empty_node_buffer.append(TreeNode(None))

        if any([node.val for node in next_iter_level]):
            iter_level = next_iter_level
            continue

        iter_level = []

    return node_val_list == test_output
