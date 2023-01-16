import sys
from typing import Tuple

import pytest


SPECIFIC_PROBLEM_DIR_NAME = 'p57'

sys.path.append(f'problem/{SPECIFIC_PROBLEM_DIR_NAME}')
import solution
import test_case


@pytest.mark.parametrize("test_case", test_case.TEST_CASES)
def test_problem(test_case):
    t_input, t_output = test_case

    sol = solution.Solution()
    no_underscore_func_str = [func for func in dir(sol) if callable(getattr(sol, func)) and '_' not in func][0]
    sol_func = getattr(sol, no_underscore_func_str)

    if isinstance(t_input, Tuple):
        result = sol_func(*t_input)
    else:
        result = sol_func(t_input)

    assert result == t_output
