
class Packet:
    def __init__(self, packet: str) -> None:
        self.version = int(packet[:3], 2)
        self.type = int(packet[3:6], 2)
        self.literal_value = None
        self.length_type_id = None
        self.children = []
        self.extra_bits = ''
        self._parse_packet(packet[6:])

    def __repr__(self) -> str:
        if self.type == 4:
            return f"Packet: v{self.version} - Literal {self.literal_value}"
        else:
            num_children = len(self.children)
            return f"Packet: v{self.version} - T{self.length_type_id} - C{num_children}"

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
            stop_bit = packet[index]
            literal += int(packet[index + 1:index + 5], 2)
            index += 5
        self.literal_value = literal
        self.extra_bits = packet[index:]

    def _parse_total_children(self, packet: str) -> None:
        child_data_length = int(packet[:15], 2)
        child_bits = packet[15:15 + child_data_length]
        while any(child_bits):
            new_child = Packet(child_bits)
            self.children.append(new_child)
            child_bits = new_child.extra_bits
        self.extra_bits = packet[15 + child_data_length:]

    def _parse_number_children(self, packet: str) -> None:
        packet_count = int(packet[:11], 2)
        child_bits = packet[11:]
        for x in range(packet_count):
            new_child = Packet(child_bits)
            self.children.append(new_child)
            child_bits = new_child.extra_bits
        self.extra_bits = child_bits

    def total_version_number(self) -> int:
        version = self.version
        version += sum([c.total_version_number() for c in self.children])
        return version


def read_file():
    with open('test.txt') as f:
        file = f.read().split('\n\n')
    return file


def test():
    bin_packet_list = []
    for line in data:
        bin_str = ''
        for c in line:
            bin_str += f'{int(c, 16):04b}'
        bin_packet_list.append(bin_str)

    parse_input = Packet(bin_packet_list[3])
    solution = parse_input.total_version_number()
    print(bin_packet_list[0])
    print(solution)


def compute(packet: str):
    print(packet)
    vers = int(packet[0:3], 2)
    type_id = int(packet[4:6], 2)

    print(vers)
    print(type_id)


def part_one():
    pass


def part_two():
    pass


if __name__ == "__main__":
    data = read_file()
    vers_pos = (0, 2)
    type_id_pos = (3, 5)
    length_id_pos = (6, 6)
    length_id_opt = (15, 11)

    test()
