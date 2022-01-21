import binascii

def read_file():
    with open('test.txt') as f:
        file = f.read().split('\n\n')
    return file

def test():
    for line in data:
        bin_str = ''
        binary = bin(int(line, 16))[2:]
        for c in line:
            bin_str += f'{int(c, 16):04b}'
        print(f'Character at a time: {bin_str}')
        print(f'Line at a time:      {binary:#040b}')



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