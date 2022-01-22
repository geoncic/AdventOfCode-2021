from math import prod


class Packet:
    version: int
    type: int
    literal_value: int or None
    length_type_id: int or None
    value: int
    children: list
    extra_bits: str
    level: int
    versions_sum: int

    def __init__(self, packet: str, level: int) -> None:
        self.bit_str = packet
        self.version = int(packet[:3], 2)
        self.type = int(packet[3:6], 2)
        self.literal_value = None
        self.length_type_id = None
        self.value = 0
        self.children = []
        self.extra_bits = ''
        self.level = level
        self.versions_sum = 0
        self._parse_packet(packet[6:])

    def _parse_packet(self, packet: str) -> None:

        if self.type == 4:
            self._parse_literal(packet)
        else:
            self.length_type_id = int(packet[0])
            if self.length_type_id == 0:
                self._parse_total_children(packet[1:])
            elif self.length_type_id == 1:
                self._parse_number_children(packet[1:])

    def _parse_literal(self, packet: str) -> None:
        packet_value = ''
        stop_bit = 1
        index = 0
        while stop_bit == 1:
            stop_bit = int(packet[index])
            packet_value += packet[index + 1:index + 5]
            index += 5
        self.literal_value = int(packet_value, 2)
        self.extra_bits = packet[index:]

    def _parse_total_children(self, packet: str) -> None:
        child_data_length = int(packet[:15], 2)
        child_bits = packet[15:15 + child_data_length]
        while any(child_bits):
            new_child = Packet(packet=child_bits, level=self.level+1)
            self.children.append(new_child)
            child_bits = new_child.extra_bits
        self.extra_bits = packet[15 + child_data_length:]

    def _parse_number_children(self, packet: str) -> None:
        packet_count = int(packet[:11], 2)
        child_bits = packet[11:]
        for x in range(packet_count):
            new_child = Packet(packet=child_bits, level=self.level+1)
            self.children.append(new_child)
            child_bits = new_child.extra_bits
        self.extra_bits = child_bits

    def total_version_number(self) -> int:
        version = self.version
        version += sum([c.total_version_number() for c in self.children])
        children_version_sum = version - self.version
        indent = '  ' * self.level
        print(indent + f'Type - > {self.type}, Level -> {self.level}; Children Version Sum -> '
                       f'{children_version_sum}; Version Sum -> {version}')
        return version

    # def total_value(self) -> int:
    #     if self.type == 4:
    #         self.value = self.literal_value
    #     elif self.type == 0:
    #         self.value += sum([c.total_value() for c in self.children])
    #
    #
    #     elif self.type == 1:
    #         self.value += prod([c.total_value() for c in self.children])
    #
    #     elif self.type == 2:
    #         self.value += min([c.total_value() for c in self.children])
    #
    #     elif self.type == 3:
    #         self.value += max([c.total_value() for c in self.children])
    #
    #     elif self.type == 5:
    #         if self.children[0].total_value() > self.children[1].total_value():
    #             self.value += 1
    #
    #     elif self.type == 6:
    #         if self.children[0].total_value() < self.children[1].total_value():
    #             self.value += 1
    #
    #     elif self.type == 7:
    #         if self.children[0].total_value() == self.children[1].total_value():
    #             self.value += 1
    #
    #
    #     indent = '  ' * self.level
    #     # if self.level == 1:
    #     print(indent + f'Type - > {self.type}, Level -> {self.level}; Value -> {self.value}')
    #     return self.value

    def total_value(self) -> int:
        child_values = [c.total_value() for c in self.children]

        if self.type == 4:
            return self.literal_value
        elif self.type == 0:
            return sum(child_values)
        elif self.type == 1:
            return prod(child_values)
        elif self.type == 2:
            return min(child_values)
        elif self.type == 3:
            return max(child_values)
        elif self.type == 5:
            return int(child_values[0] > child_values[1])
        elif self.type == 6:
            return int(child_values[0] < child_values[1])
        elif self.type == 7:
            return int(child_values[0] == child_values[1])


def part_one() -> int:
    parse_input: Packet
    solution: int
    bin_packet_list: list[str]

    bin_packet_list = []
    for line in data:
        bin_str = ''
        for c in line:
            bin_str += f'{int(c, 16):04b}'
        bin_packet_list.append(bin_str)

    parse_input = Packet(packet=bin_packet_list[0], level=0)
    solution = parse_input.total_version_number()
    return solution


def part_two():
    parse_input: Packet
    solution: int
    bin_packet_list: list[str]

    bin_packet_list = []
    for line in data:
        bin_str = ''
        for c in line:
            bin_str += f'{int(c, 16):04b}'
        bin_packet_list.append(bin_str)

    parse_input = Packet(packet=bin_packet_list[0], level=0)
    solution = parse_input.total_value()

    return solution


def read_file():
    with open('input.txt') as f:
        file = f.read().split('\n\n')
    return file


if __name__ == "__main__":
    data = read_file()
    print(f'Part One: The solution is {part_one()}')
    print(f'Part Two: The solution is {part_two()}')
