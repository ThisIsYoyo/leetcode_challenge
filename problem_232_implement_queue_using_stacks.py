from typing import List


class BuildInFunc:
    pass


class MyQueue:

    def __init__(self):
        self._push_stack = []
        self._pop_stack = []

    def push(self, x: int) -> None:
        self._push_stack.append(x)

    def pop(self) -> int:
        if self._pop_stack:
            pass
        else:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())

        return self._pop_stack.pop()

    def peek(self) -> int:
        if self._pop_stack:
            pass
        else:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())

        peek_result = self._pop_stack.pop()
        self._pop_stack.append(peek_result)

        return peek_result

    def empty(self) -> bool:
        return not self._push_stack and not self._pop_stack


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def exe_fifo(self, cmds: List, params: List) -> List:
        queue = None
        exe_result = []

        for cmd, param in zip(cmds, params):
            if cmd == 'MyQueue':
                queue = MyQueue()
                exe_result.append(None)
            elif cmd == 'push':
                queue.push(param[0])
                exe_result.append(None)
            elif cmd == 'pop':
                exe_result.append(queue.pop())
            elif cmd == 'peek':
                exe_result.append(queue.peek())
            elif cmd == 'empty':
                exe_result.append(queue.empty())

        return exe_result


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (
            (["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]),
            [None, None, None, 1, 1, False],
        ),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()
        cmds, params = t_input

        sol = Solution(built_in_func)
        result = sol.exe_fifo(cmds, params)

        print(f'Is execute expect ? `{result == t_output}`')
