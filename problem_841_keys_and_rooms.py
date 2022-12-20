from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._rooms = []  # [room_id]: key in room

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # init
        self._rooms = rooms

        return self.bfs(capable_set={0}, visited_room_set=set())

    def bfs(self, capable_set: set, visited_room_set: set) -> bool:
        cur_visited_room_set = visited_room_set.copy()
        cur_capable_set = capable_set.copy()
        for not_visit_room in capable_set - visited_room_set:
            cur_visited_room_set |= {not_visit_room}
            cur_capable_set |= set(self._rooms[not_visit_room])

        if len(capable_set) == len(self._rooms):
            return True

        if capable_set == visited_room_set:
            return False

        return self.bfs(capable_set=cur_capable_set, visited_room_set=cur_visited_room_set)


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
        ([
             [13], [15, 29, 22], [5, 18, 9], [7], [27], [27], [6, 28], [26], [34], [1, 44, 11], [8, 36], [17, 35],
             [11, 45, 46, 10, 49], [19, 38, 47, 39], [20, 30], [34], [32, 31], [25, 19, 21, 29], [36], [], [38],
             [2, 13, 17, 47], [12], [49, 46], [], [40], [], [39, 16, 24], [24, 41], [14, 3, 40], [14, 43], [],
             [3, 20, 23], [37, 48], [6, 10], [26, 1, 4], [], [41, 45], [23, 33], [], [22, 18, 37], [4, 33, 43],
             [28, 31, 42], [30, 48], [16, 35], [5, 8, 44], [2, 25], [9, 21, 42], [7, 12, 32], []
         ], True)
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.canVisitAllRooms(t_input)

        print(f'Is can visit expect ? `{result == t_output}`')
