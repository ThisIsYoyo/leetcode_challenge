from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        zero_to_node_map = self.bfs_build_zero_to_node_map(edges)

        go_through_edge_set = set()
        for has_apple_idx, has_apple in enumerate(hasApple):
            if has_apple:
                go_through_edge_set.update(zero_to_node_map[has_apple_idx])
            else:
                pass

        return 2 * len(go_through_edge_set)

    def bfs_build_zero_to_node_map(self, edges: List[List[int]]):
        # assume i node must found connect in edges[0:j+1], where j is i first appear idx in edges
        rest_edges = edges.copy()
        zero_to_node_map = {0: []}

        while rest_edges:
            e1, e2 = rest_edges.pop(0)
            if e1 in zero_to_node_map:
                zero_to_node_map[e2] = zero_to_node_map[e1] + [(e1, e2)]
            elif e2 in zero_to_node_map:
                zero_to_node_map[e1] = zero_to_node_map[e2] + [(e2, e1)]
            else:
                print(f'Not connect edge ({e1}, {e2}) in exists map')

        return zero_to_node_map

