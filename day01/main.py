from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from operator import mul
from typing import List


def part1_solution(report: List[int]) -> int:
    for a, b in combinations(report, 2):
        if a + b == 2020:
            return a * b


def part2_solution(report: List[int]) -> int:
    for items in combinations(report, 3):
        if sum(items) == 2020:
            return reduce(mul, items)


@dataclass
class GenericSolution:
    entries: int
    year: int

    def solve(self, report: List[int]) -> int:
        for items in combinations(report, self.entries):
            if sum(items) == self.year:
                return reduce(mul, items)


def test_solution():
    from data import dataset_test
    assert part1_solution(dataset_test) == 514579
    assert part2_solution(dataset_test) == 241861950

    part1 = GenericSolution(entries=2, year=2020)
    assert part1.solve(dataset_test) == 514579
    part2 = GenericSolution(entries=3, year=2020)
    assert part2.solve(dataset_test) == 241861950


if __name__ == "__main__":
    from data import dataset

    print(part1_solution(dataset))
    print(part2_solution(dataset))
