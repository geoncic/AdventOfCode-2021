import functools
import collections
import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
QUANTUM_ROLLS = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
# REALITY_COMPLETE = [False, False, False, False, False, False, False]
die = 0


def day_twentyone(data: list):
    players, turns = part_one(data)
    for player in players:
        if not player.win:
            score = player.points

    part_one_sol = score * turns * 3
    print(f'Part One: {part_one_sol}')
    print(f'Part Two: {part_two(data)}')

class Player:
    pid: int
    position: int
    points: int
    win: bool
    realities = dict


    def __init__(self, pid: int, position: int) -> None:
        self.pid = pid
        self.position = position
        self.points = 0
        self.win = False
        # [position, score, counts]
        self.realities = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 5: [0, 0, 0], 6: [0, 0, 0]}

    def move(self, r: int) -> ...:
        self.position += r
        while self.position > 10:
            self.position -= 10
        self.points += self.position
        return self.points



def turn(d1: int, d2: int, d3: int) -> int:
    return d1 + d2 + d3

def find_pos(p: int) -> int:
    while p > 10:
        p -= 10
    return p

def roll(d: int, size: int) -> int:
    global die
    if d == size:
        die = 1
        return 1
    else:
        die += 1
        return die

def play_dirac(players, score: int):
    count = 0

    p1_pos = players[0].position
    p2_pos = players[1].position

    @functools.lru_cache(maxsize=None)
    def win_count(
            p1_pos: int,
            p1_score: int,
            p2_pos: int,
            p2_score: int,
    ) -> tuple[int, int]:
        p1_wins = p2_wins = 0
        for dis, ct in QUANTUM_ROLLS:
            new_p1_pos = find_pos(p1_pos + dis)
            new_p1_score = p1_score + new_p1_pos
            if new_p1_score >= 21:
                p1_wins += ct
            else:
                tmp_p2_wins, tmp_p1_wins = win_count(
                    p2_pos,
                    p2_score,
                    new_p1_pos,
                    new_p1_score,
                )
                p1_wins += tmp_p1_wins * ct
                p2_wins += tmp_p2_wins * ct

        return p1_wins, p2_wins

    p1_win, p2_win = win_count(p1_pos, 0, p2_pos, 0)

    print(f'P1 Wins: {p1_win}; P2 Wins: {p2_win}')
    return p1_win, p2_win

def part_one(data: list):
    global die
    turns = 0
    players = []
    for pid, player in enumerate(data):
        players.append(Player(pid + 1, player))

    while True:
        for player in players:
            d1 = roll(die, 100)
            d2 = roll(die, 100)
            d3 = roll(die, 100)
            distance = turn(d1, d2, d3)
            player.move(distance)
            turns += 1
            if player.points >= 1000:
                player.win = True
            if player.win:
                return players, turns


def part_two(data: list):
    players = []
    for pid, player in enumerate(data):
        players.append(Player(pid + 1, player))
    p1_wins, p2_wins = play_dirac(players, 21)

    return max(p1_wins, p2_wins)



def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        data = f.read().splitlines()
        player_start = []
        for line in data:
            start = line.split(' ')[-1]
            player_start.append(int(start))

    return player_start


def main():
    data = read_file()
    day_twentyone(data)


if __name__ == "__main__":
    raise SystemExit(main())
