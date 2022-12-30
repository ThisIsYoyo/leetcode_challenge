from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._graph = None
        self._paths_to_final = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # init
        self._graph = graph

        self._find_path(path=[0])

        return self._paths_to_final

    def _find_path(self, path: List[int]) -> None:
        if path[-1] == len(self._graph) - 1:
            self._paths_to_final.append(path)
            return

        next_capable_nodes = self._graph[path[-1]]

        for c_node in next_capable_nodes:
            self._find_path(path=path + [c_node])


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        ([[4, 3, 1], [3, 2, 4], [3], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.allPathsSourceTarget(t_input)

        not_in_result = t_output.copy()
        for r in result:
            try:
                not_in_result.remove(r)
            except ValueError:
                continue
        print(f'Is all path expect ? `{not not_in_result}`')
