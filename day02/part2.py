from dataclasses import dataclass
from typing import List


@dataclass
class PasswordPolicy:
    """
    Each policy actually describes two positions in the password (starting with index = 1)

    Exactly one of these positions must contain the given letter.
    """
    letter: str
    lower_limit: int
    upper_limit: int

    def validate(self, password: str) -> bool:
        characters = [password[self.lower_limit - 1], password[self.upper_limit - 1]]
        return characters.count(self.letter) == 1


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


def solution(database: List[str]) -> int:
    return len([
        line for line in database
        if PasswordAttempt.from_database_line(line).validate()
    ])


def test_solution():
    from data import dataset_test

    # unit testing
    assert PasswordPolicy(letter="a", lower_limit=1, upper_limit=3).validate("abcde") is True
    assert PasswordPolicy(letter="b", lower_limit=1, upper_limit=3).validate("cdefg") is False
    assert PasswordPolicy(letter="c", lower_limit=2, upper_limit=9).validate("ccccccccc") is False

    assert solution(dataset_test) == 1


if __name__ == "__main__":
    from data import dataset

    print(solution(dataset))
