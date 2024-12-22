def kuhn_algorithm(n: int, sets: list) -> list[str]:

    graph = {}
    for i in range(n):
        graph[i] = sets[i]

    match = {}
    used = set()

    def try_kuhn(v):
        if v in used:
            return False
        used.add(v)
        for to in graph[v]:
            if to not in match or try_kuhn(match[to]):
                match[to] = v
                return True
        return False

    for v in range(n):
        used.clear()
        try_kuhn(v)

    if len(match) == n:
        result = ['Y']
        representatives = [0] * n
        for key, value in match.items():
            representatives[value] = key
        result.append(' '.join(map(str, representatives)))
        return result
    else:
        return ['N']


def main():
    with open('in.txt', 'r') as file:
        sets_input = []
        n = int(file.readline().strip())
        for _ in range(n):
            line = list(map(int, file.readline().strip().split()))
            sets_input.append(line[:-1])  # Remove 0 at the end of each line

    result = kuhn_algorithm(n, sets_input)

    with open('out.txt', 'w') as file:
        file.write(result[0] + '\n')
        if result[0] == 'Y':
            file.write(result[1] + '\n')


if __name__ == "__main__":
    main()
