from typing import List


def verify(result: List[List[int]], test_output: List[List[int]]) -> bool:
    for r in result:
        if r in test_output:
            test_output.remove(r)
        else:
            assert False

    assert test_output == []
