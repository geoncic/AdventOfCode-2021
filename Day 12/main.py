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

def dfs_2(path: list[list[str]], visited: set[str], cave: [str], twice: set[str]):
    if cave == 'end':
        solutions_dfs.append(path)
    else:
        if cave.islower():
            if cave in visited and cave not in ['start', 'end']:
                twice.add(cave)
            visited.add(cave)
        for next_cave in edges[cave]:
            if next_cave not in visited:
                dfs_2(path + [next_cave], set(visited), next_cave, set(twice))
            elif next_cave not in ['start', 'end'] and len(twice) == 0:
                dfs_2(path + [next_cave], set(visited), next_cave, set(twice))

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
    revisited = set()
    solutions_dfs = []
    solutions_dfs_2 = []
    dfs_2(todo_dfs, set(), "start", set())

    print(f'Part One: BFS Path Count is {bfs()}')
    print(f'Part Two: DFS Path Count is {len(solutions_dfs)}')
