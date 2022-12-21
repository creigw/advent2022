from typing import Dict, List


def read_file_to_string_list(path) -> List[str]:
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    return data
