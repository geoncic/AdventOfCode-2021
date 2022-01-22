class Bullet:
    x_v: int
    y_v: int

    def __init__(self, x_v: int, y_v: int) -> None:
        self.x_in = x_v
        self.y_in = y_v
        self.x_v = x_v
        self.y_v = y_v
        self.x = 0
        self.y = 0
        self.max_y = 0
        self.time = 0
        self.overshot = False


    def update(self):
        self.time += 1
        self.x += int(self.x_v)
        self.y += int(self.y_v)
        if self.y > self.max_y:
            self.max_y = self.y
        if self.x_v != 0:
            self.x_v -= abs(self.x_v) / self.x_v
        self.y_v -= 1
        if self.check_bounds():
            return self.max_y
        if self.check_oob():
            return self.overshot

    def check_bounds(self):
        global count

        print(f'Checking {self.x}, {self.y}')
        print(data[0][0], data[1][0])
        if self.x in range(data[0][0], data[1][0]): # check x boundary
            if self.y in range(data[1][1], data[0][1]): # check y boundary
                print(f'Vel: {self.x_in}, {self.y_in}')
                print(f'Pos: {self.x}, {self.y}')
                count += 1
                return True

    def check_oob(self):
        if self.x > data[1][0]:
            self.overshot = True
            print(f'Out Vel: {self.x_in}, {self.y_in}')
            print(f'Out Pos: {self.x}, {self.y}')
        elif self.y < data[1][1]:
            self.overshot = True
            print(f'Out Vel: {self.x_in}, {self.y_in}')
            print(f'Out Pos: {self.x}, {self.y}')
        return self.overshot


def part_one():
    bullets = []
    bullet_height = []
    for i in range(data[1][0]+1):
        for j in range(data[1][1]-1, abs(data[1][1])+1):
            bullets.append(Bullet(i, j))
            while True:
                result = bullets[-1].update()
                if result:
                    bullet_height.append(int(result))
                    break
    print(max(bullet_height))

def part_two():
    pass

def read_file():
    with open('test.txt') as f:
        file = f.read()
        x_start = file.index('=')
        x_end = file.index(',', x_start + 1)
        y_start = file.index('=',x_start + 1)
        x_min, x_max = file[x_start + 1:x_end].split('..')
        y_min, y_max = file[y_start + 1:].split('..')
        top_left = (int(x_min), int(y_max))
        bottom_right = (int(x_max), int(y_min))
    return top_left, bottom_right


if __name__ == "__main__":
    data = read_file()
    count = 0

    print(f'Part One: Max Y is {part_one()}')
    print(f'Part Two: Successful hits is: {count}')
    print(5 in range(5,10))
