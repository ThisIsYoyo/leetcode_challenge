import sys
import time
from typing import Tuple

import pytest


SPECIFIC_PROBLEM_DIR_NAME = 'p29'

sys.path.append(f'problem/{SPECIFIC_PROBLEM_DIR_NAME}')
import solution
import test_case
try:
    import verify
except ModuleNotFoundError:
    class verify:
        @staticmethod
        def verify(result, test_output):
            assert result == test_output


@pytest.mark.parametrize("test_case", test_case.TEST_CASES)
def test_problem(test_case):
    t_input, t_output = test_case

    sol = solution.Solution()
    no_underscore_func_str = [func for func in dir(sol) if callable(getattr(sol, func)) and '_' not in func][0]
    sol_func = getattr(sol, no_underscore_func_str)

    spend_t = 0
    if isinstance(t_input, Tuple):
        _t = time.time()
        result = sol_func(*t_input)
        spend_t = time.time() - _t
    else:
        _t = time.time()
        result = sol_func(t_input)
        spend_t = time.time() - _t

    verify.verify(result, t_output)
    print(f"\ntestcase spend time: {spend_t} secs")
