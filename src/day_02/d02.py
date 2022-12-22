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

LOSS_REF = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

CHOICE_DECODE = {
    'A': 'X',  # rock
    'B': 'Y',  # paper
    'C': 'Z'  # scissors
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


def get_round_list_p1(data: List[str]) -> List[Round]:
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


# Part 2
######################
OUTCOME_DECODE = {
    'X': RoundOutcome.LOSS,
    'Y': RoundOutcome.DRAW,
    'Z': RoundOutcome.WIN
}


def get_choices_given_outcome(coded_values):
    opponent_choice = coded_values[0]
    outcome = OUTCOME_DECODE[coded_values[1]]

    if outcome == RoundOutcome.DRAW:
        our_choice = CHOICE_DECODE[opponent_choice]
    elif outcome == RoundOutcome.LOSS:
        our_choice = LOSS_REF[opponent_choice]
    elif outcome == RoundOutcome.WIN:
        our_choice = WIN_REF[opponent_choice]
    return (opponent_choice, our_choice)


def get_round_list_p2(data: List[str]) -> List[Round]:
    round_list = []

    for round in data:
        coded_values = round.split()
        opponent_choice, our_choice = get_choices_given_outcome(coded_values)
        round_list.append(Round(opponent_choice, our_choice))

    return round_list

######################


def main(data: List):

    # Part 1
    round_list_p1 = get_round_list_p1(data)
    total_rounds_score = get_rounds_total_score(round_list_p1)
    print(f'The total rounds score for part 1 is: {total_rounds_score}')

    # Part 2
    round_list_p2 = get_round_list_p2(data)
    total_rounds_score = get_rounds_total_score(round_list_p2)
    print(f'The total rounds score for part 2 is: {total_rounds_score}')


if __name__ == '__main__':
    # Config run
    IS_TEST = 0

    DAY = 'd02'
    PART = 'a'
    REF = 'ref' if IS_TEST == 1 else 'input'

    DATA_FILE_NAME = f'{DAY}_{PART}_{REF}.txt'
    path = Path(__file__).parent.absolute() / 'data' / DATA_FILE_NAME

    data = read_file_to_string_list(path)

    main(data)
