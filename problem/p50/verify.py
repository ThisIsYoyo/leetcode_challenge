from typing import List


def verify(result: float, test_output: float) -> bool:
    round_5_result = round(result, 5)

    return round_5_result == test_output
