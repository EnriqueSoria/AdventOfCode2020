from dataclasses import dataclass
from typing import List


@dataclass
class PasswordPolicy:
    """
    The password policy indicates the lowest and highest number of times a given letter
    must appear for the password to be valid.

    For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
    """
    letter: str
    lower_limit: int
    upper_limit: int

    def validate(self, password: str) -> bool:
        return self.lower_limit <= password.count(self.letter) <= self.upper_limit


@dataclass
class PasswordAttempt:
    policy: PasswordPolicy
    password: str

    def validate(self) -> bool:
        return self.policy.validate(self.password)

    @staticmethod
    def from_database_line(line: str) -> "PasswordAttempt":
        limits, letter, password = line.split(" ")
        lower_limit, upper_limit = limits.split("-")

        return PasswordAttempt(
            policy=PasswordPolicy(
                letter=letter.rstrip(":"),
                lower_limit=int(lower_limit),
                upper_limit=int(upper_limit)
            ), password=password
        )


def part1_solution(database: List[str]) -> int:
    return len([
        line for line in database
        if PasswordAttempt.from_database_line(line).validate()
    ])


def test_solution():
    from data import dataset_test, result_test

    # unit testing
    assert PasswordPolicy(letter="a", lower_limit=1, upper_limit=3).validate("abcde") is True
    assert PasswordPolicy(letter="b", lower_limit=1, upper_limit=3).validate("cdefg") is False
    assert PasswordPolicy(letter="c", lower_limit=2, upper_limit=9).validate("ccccccccc") is True

    assert part1_solution(dataset_test) == result_test


if __name__ == "__main__":
    from data import dataset

    print(part1_solution(dataset))
