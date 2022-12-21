from functools import reduce

from pathlib import Path
from typing import List


from utils.file_handling import read_file_to_string_list


class Elf():
    def __init__(self, items: List[int]):
        self.items = items

    def __str__(self) -> str:
        return '[' + ','.join(map(lambda x: str(x), self.items)) + ']'

    @property
    def total_cals(self):
        return reduce(lambda x, y: x + y, self.items, 0)


def get_elves(data: List) -> List[Elf]:
    # Creates each elf with its own food items from the given list of data
    elves = []
    items = []
    for food in data:

        if food:
            items.append(int(food))

        elif not food:
            elves.append(Elf(items.copy()))
            items.clear()

    # this add the last elf in the list if there isn't a blank line at the end
    if items:
        elves.append(Elf(items.copy()))
        items.clear()

    return elves


def get_elf_with_most_cals(elves: List[Elf]):
    # finds and returns the elf carrying the most cals
    max_cals = 0
    max_cal_elf: Elf
    for elf in elves:
        if elf.total_cals > max_cals:
            max_cals = elf.total_cals
            max_cal_elf = elf

    return max_cal_elf


def sort_elves_by_cals(elf: Elf):
    return elf.total_cals


def get_total_for_top_three_elves(elves: List[Elf]):
    return elves[0].total_cals + elves[1].total_cals + elves[2].total_cals


######################


def main(data: List):
    elves = get_elves(data)

    # Part 1
    max_cal_elf = get_elf_with_most_cals(elves)
    # Answer part 1
    print(f'Elf carrying the most Calories: {max_cal_elf}, Total: {max_cal_elf.total_cals}')

    # Part 2
    elves.sort(reverse=True, key=sort_elves_by_cals)
    total_for_top_three = get_total_for_top_three_elves(elves)

    # Answer part 2
    print(f'Total for top three elves: {total_for_top_three}')


if __name__ == '__main__':
    # Config run
    IS_TEST = 0

    DAY = 'd01'
    PART = 'a'
    REF = 'ref' if IS_TEST == 1 else 'input'

    DATA_FILE_NAME = f'{DAY}_{PART}_{REF}.txt'
    path = Path(__file__).parent.absolute() / 'data' / DATA_FILE_NAME

    data = read_file_to_string_list(path)

    main(data)
