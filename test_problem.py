#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="test_problem",
        description="test leetcode problem",
    )
    parser.add_argument("problem_number", type=int, help="problem number")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # import problem package
    problem_folder = Path(__file__).parent / "problem" / f"p{args.problem_number}"
    sys.path.insert(0, str(problem_folder.resolve()))

    # import solution, test_case, verify
    from solution import Solution
    from test_case import TEST_CASES
    try:
        from verify import verify
    except ModuleNotFoundError:
        def verify(actual, expected) -> bool:
            return actual == expected

    sol = Solution()
    process_function = getattr(sol, sol.process_function_str)

    for input_, expected in TEST_CASES:
        if isinstance(input_, tuple):
            actual = process_function(*input_)
        else:
            actual = process_function(input_)
        assert verify(actual, expected), (actual, expected)

if __name__ == "__main__":
    raise SystemExit(main())
