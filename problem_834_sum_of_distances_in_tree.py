from typing import List, Tuple


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._neighbor_list_map = []  # [node_id]: neighbor
        self._cache = {}  # (node, parent_from): sum, total node num

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self._neighbor_list_map = [[] for _ in range(n)]

        for e in edges:
            e1, e2 = e
            self._neighbor_list_map[e1].append(e2)
            self._neighbor_list_map[e2].append(e1)

        result = []
        for node_id in range(n):
            node_sum, _ = self.sum_child(node_id, node_id)
            result.append(node_sum)

        return result

    def sum_child(self, node: int, parent_from: int) -> Tuple[int, int]:  # sum, total node num
        if (node, parent_from) in self._cache:
            return self._cache[(node, parent_from)]

        node_nei_list = self._neighbor_list_map[node]
        node_total_node_num = 1  # self
        node_sum = 0

        for nei in node_nei_list:
            if nei == parent_from:
                continue

            nei_sum, nei_total_node = self.sum_child(nei, parent_from=node)
            node_total_node_num += nei_total_node
            node_sum += nei_total_node + nei_sum

        self._cache[(node, parent_from)] = node_sum, node_total_node_num
        return node_sum, node_total_node_num


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ((6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]), [8, 12, 6, 10, 10, 10]),
        ((1, []), [0]),
        ((2, [[1, 0]]), [1, 1])
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()
        n, edges = t_input

        sol = Solution(built_in_func)
        result = sol.sumOfDistancesInTree(n, edges)

        print(f'Is sum expect ? `{result == t_output}`')
