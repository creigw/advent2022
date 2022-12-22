from enum import Enum
from pathlib import Path
from typing import List

from utils.file_handling import read_file_to_string_list


class ChoiceScore(Enum):
    X = 1
    Y = 2
    Z = 3


class RoundOutcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


WIN_REF = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

CHOICE_DECODE = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}


class Round():
    def __init__(self, opponent_choice, our_choice):
        self.opponent_choice = opponent_choice
        self.our_choice = our_choice

    def round_outcome(self):
        if CHOICE_DECODE[self.opponent_choice] == self.our_choice:
            return RoundOutcome.DRAW
        elif WIN_REF[self.opponent_choice] == self.our_choice:
            return RoundOutcome.WIN
        else:
            return RoundOutcome.LOSS

    def result_score(self):
        return ChoiceScore[self.our_choice].value + self.round_outcome().value


def get_round_list(data: List[str]) -> List[Round]:
    round_list = []

    for round in data:
        player_choices = round.split()
        round_list.append(Round(player_choices[0], player_choices[1]))

    return round_list


def get_rounds_total_score(round_list: List[Round]):
    total_score = 0
    for round in round_list:
        total_score += round.result_score()
    return total_score

######################


def main(data: List, debug):

    round_list = get_round_list(data)

    if debug:
        for r in round_list:
            print(r.round_outcome())
            print(r.result_score())

    # Part 1
    total_rounds_score = get_rounds_total_score(round_list)
    print(f'The total rounds score is: {total_rounds_score}')

    # Part 2


if __name__ == '__main__':
    # Config run
    DEBUG = True
    IS_TEST = 0

    DAY = 'd02'
    PART = 'a'
    REF = 'ref' if IS_TEST == 1 else 'input'

    DATA_FILE_NAME = f'{DAY}_{PART}_{REF}.txt'
    path = Path(__file__).parent.absolute() / 'data' / DATA_FILE_NAME

    data = read_file_to_string_list(path)

    main(data, DEBUG)
