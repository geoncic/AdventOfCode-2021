from collections import defaultdict

def dayTen():
    data = readFile()
    print(f'Part One: Total syntax errors score is {partOne(data)}')
    print(f'Part One: Middle score is {partTwo(data)}')

def partOne(data):
    points = 0
    set_dict = {')':'(',']':'[','}':'{','>':'<'}
    forward = {v: k for k, v in set_dict.items()}
    set_points = {')':3,']':57,'}':1197,'>':25137}
    for line in data:
        stack = []
        for c in line:
            if c in forward:
                stack.append(c)
            elif c in set_dict:
                if set_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    points += set_points[c]
                    break
    return points

def partTwo(data):
    stack_scores = []
    set_dict = {')': '(', ']': '[', '}': '{', '>': '<'}
    forward = {v: k for k, v in set_dict.items()}
    set_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for l, line in enumerate(data):
        stack = []
        for i, c in enumerate(line):
            if c in forward:
                stack.append(c)
                if (i+1) == len(line):
                    stack = stack[::-1]
                    stack_scores.append(scoreStack(stack))
            elif c in set_dict:
                if set_dict[c] == stack[-1]:
                    stack.pop()
                    if (i + 1) == len(line):
                        stack = stack[::-1]
                        stack_scores.append(scoreStack(stack))
                else:
                    # points += set_points[c]
                    break

    stack_scores = sorted(stack_scores)
    return stack_scores[int(len(stack_scores)/2)]


    # This finally makes sense... this code does not work below, because it
    # tries to close a chunk while others are still open
    # for example: [][(())]<> is valid
    # but [][(]) is not valid...

    # for l, line in enumerate(data):
    #     chunk = defaultdict(lambda: 0)
    #     for x, character in enumerate(line):
    #         if character in open_chunk:
    #             chunk[character] += 1
    #         else:
    #             chunk[set_dict[character]] -= 1
    #             if chunk[set_dict[character]] < 0:
    #                 print(f'Line: {l} is corrupt at position {x}, with character {character}')
    #                 break

def scoreStack(stack):
    score = 0
    set_points = {'(': 1, '[': 2, '{': 3, '<': 4}

    for i in stack:
        score = score*5 + set_points[i]
    return score



def readFile():
    with open('input.txt') as f:
        data = f.read().split('\n')
        data = [list(i) for i in data]
    return data


if __name__ == "__main__":
    dayTen()