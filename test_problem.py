import sys
from typing import Tuple

import pytest


@pytest.mark.parametrize("file_str", [('p100')])
def test_param_problem(file_str):
    sys.path.append(f'problem/{file_str}')
    import solution
    import test_case

    for t_case in test_case.TEST_CASES:
        t_input, t_output = t_case

        sol = solution.Solution()
        first_func_str = [func for func in dir(sol) if callable(getattr(sol, func)) and not func.startswith('__')][0]
        sol_func = getattr(sol, first_func_str)

        if isinstance(t_input, Tuple):
            result = sol_func(*t_input)
        else:
            result = sol_func(t_input)

        assert result == t_output
