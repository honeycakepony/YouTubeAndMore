# started 27-04-2024
# https://youtu.be/A80YzvNwqXA?si=QyzntaCJTeO0d4PS
# Understanding: low
from typing import List


def is_valid_state(state, n) -> bool:
    """Checks if the state is valid, i.e. all n queens have been placed"""
    return len(state) == n


def get_candidates(state, n):
    if not state:
        return range(n)

    position = len(state)
    candidates = set(range(n))

    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates


def state_to_string(state, n):
    ret = []
    for i in state:
        string = '.' * i + 'Q' + '.' * (n - i - 1)
        ret.append(string)
    return ret


class Solution:
    def solve_n_queens(self, n: int) -> List[List[str]]:
        """input: n = 1 -> output: ["Q"]"""
        solutions = list()
        state = list()
        self.search(state, solutions, n)
        return solutions

    def search(self, state, solutions, n):
        if is_valid_state(state, n):
            state_string = state_to_string(state, n)
            solutions.append(state_string)
            return

        for candidate in get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
            return
