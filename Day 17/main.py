class Bullet:
    x_v: int
    y_v: int

    def __init__(self, x_v: int, y_v: int) -> None:
        self.x_v = x_v
        self.y_v = y_v
        self.x = 0
        self.y = 0
        self.max_y = 0
        self.time = 0
        self.overshot = False


    def update(self):
        self.time += 1
        self.x += self.x_v
        self.y += self.y_v
        if self.y > self.max_y:
            self.max_y = self.y
        if self.x_v != 0:
            self.x_v -= abs(self.x_v) / self.x_v
        self.y_v -= 1
        # print(f'Step: {self.time}')
        # print(f'Position: ({self.x}, {self.y})')
        if self.check_bounds():
            return self.max_y
        if self.check_oob():
            # print(f'Overshot Big Time! ({self.x}, {self.y})')
            return self.overshot

    def check_bounds(self):
        # print(f'Checking {self.x} against {data[0][0]} <-> {data[1][0]}')
        # print(f'Checking {self.y} against {data[0][1]} <-> {data[1][1]}')
        if self.x in range(data[0][0], data[1][0]): # check x boundary
            if self.y in range(data[1][1], data[0][1]): # check y boundary
                print(f'Position ({self.x}, {self.y}) is In Bounds')
                return True

    def check_oob(self):
        if self.x > data[1][0]:
            # print(f'Overshot the Horizontal')
            self.overshot = True
        elif self.y < data[1][1]:
            # print(f'Overshot the Vertical')
            self.overshot = True
        return self.overshot


def part_one():
    bullet_1 = Bullet(6, 9)
    # while True:
        # result = bullet_1.update()
        # if result:
        #     break
    bullets = []
    bullet_height = []
    for i in range(500):
        for j in range(500):
            bullets.append(Bullet(i, j))
            while True:
                result = bullets[-1].update()
                if result:
                    # print(int(result))
                    bullet_height.append(int(result))
                    break
                # print(result)
    print(max(bullet_height))

def part_two():
    pass

def read_file():
    with open('input.txt') as f:
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
    part_one()