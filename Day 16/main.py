from math import prod

# TYPE_1 = sum
# TYPE_2 = prod
# TYPE_3 = min
# TYPE_4 = max
# # sub-packet count is always 2
# TYPE_5 =    # value == 1 if value(children_packets[0]) > value(children_packets[1]) else: value = 0
# TYPE_6 =    # value == 1 if value(children_packets[0]) < value(children_packets[1]) else: value = 0
# TYPE_7 =    # value == 1 if value(children_packets[0]) == value(children_packets[1]) else: value = 0

""" Todo: for each packet, collect values of all sub-packets. 
Value is the return value of sub-packets based on the type id.
"""


class Packet:
    version: int
    type: int
    literal_value: int or None
    length_type_id: int or None
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
        literal = 0
        stop_bit = 1
        index = 0
        while stop_bit == 1:
            stop_bit = int(packet[index])
            literal += int(packet[index + 1:index + 5], 2)
            index += 5
        self.literal_value = literal
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
        # print(f'level is {self.level}')
        # print(f'Packet is {self.bit_str}')
        indent = '  ' * self.level
        print(indent + f'Version -> {self.version}, Type - > {self.type}, Level -> {self.level}; Version Sum -> {version}')
        return version


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
    pass


def read_file():
    with open('input.txt') as f:
        file = f.read().split('\n\n')
    return file


if __name__ == "__main__":
    data = read_file()
    print(f'Part One: The solution is {part_one()}')
    print(f'Part Two: The solution is {part_two()}')
