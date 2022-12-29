from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # init
        time = 1
        not_ava_tasks_by_queue_time = [
            (task_info[0], task_info[1], task_idx)  # queue time, process time, idx
            for task_idx, task_info in enumerate(tasks)
        ]
        not_ava_tasks_by_queue_time.sort()
        wait_to_process_tasks = []  # process time, idx
        result_orders = []

        while not_ava_tasks_by_queue_time:
            if not wait_to_process_tasks and not_ava_tasks_by_queue_time[0][0] > time:
                time = not_ava_tasks_by_queue_time[0][0]

            while not_ava_tasks_by_queue_time and not_ava_tasks_by_queue_time[0][0] <= time:
                q_t, p_t, idx = not_ava_tasks_by_queue_time.pop(0)
                wait_to_process_tasks.append((p_t, idx))

            wait_to_process_tasks.sort()
            process_time, task_idx = wait_to_process_tasks.pop(0)

            result_orders.append(task_idx)
            time += process_time

        if wait_to_process_tasks:
            result_orders.extend([task_idx for _, task_idx in wait_to_process_tasks])

        return result_orders


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
        ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.getOrder(t_input)

        print(f'Is order expect ? `{result == t_output}`')
