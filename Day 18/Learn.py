import ast
import copy
from typing import List

class SFNumber:
    def __init__(self, snailfish_str: str) -> None:
        self.raw_number = copy.copy(snailfish_str)
        self._parse()

    def _parse(self):
        self.number = []
        current_digit = ""
        for char in self.raw_number:
            if char.isdigit():
                current_digit += char
            else:
                if current_digit != "":
                    self.number.append(int(current_digit))
                    current_digit = ""
                if char != ',':
                    self.number.append(char)

    def __repr__(self) -> str:
        return f"SFNumber({self.__str__()}"

def process_snail_list(numbers: List[str]) -> SFNumber:
    result_number = None
    for number in numbers:
        new_number = SFNumber(number)
        if result_number is None:
            result_number = new_number
        else:
            result_number.add(new_number)

    return result_number


def read_file():
    with open('input.txt') as f:
        file = f.read().split()
        output = []
        for i, line in enumerate(file):
            # output.append(ast.literal_eval(line))
            output.append(line)
    return output


if __name__ == "__main__":
    data = read_file()

    process_snail_list(data)

    # for line in data:
        # print(line)