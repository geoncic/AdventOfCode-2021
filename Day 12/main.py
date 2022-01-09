import collections

def bfs():
    while todo_bfs:
        path = todo_bfs.pop()
        if path[-1] == 'end':
            all_paths.add(path)
            continue

        for cand in edges[path[-1]]:
            if not cand.islower() or cand not in path:
                todo_bfs.append((*path, cand))
    return len(all_paths)

def dfs(path: list[list[str]], visited: set[str], cave: [str]):

    if cave == 'end':
        solutions_dfs.append(path)
    else:
        if cave.islower():
            visited.add(cave)
        for next_cave in edges[cave]:
            if next_cave not in visited:
                dfs(path + [next_cave], set(visited), next_cave)

def read_file():
    with open('input.txt') as f:
        data = f.read().split('\n')

    return data

if __name__ == "__main__":
    data = read_file()
    edges = collections.defaultdict(list)

    for line in data:
        src, dst = line.split("-")
        edges[src].append(dst)
        edges[dst].append(src)
    todo_bfs = [('start',)]
    todo_dfs = ['start']
    all_paths = set()
    solutions_dfs = []
    dfs(todo_dfs, set(), "start")

    print(f'Part One: BFS Path Count is {bfs()}')
    print(f'Part One: DFS Path Count is {len(solutions_dfs)}')