def find_distinct_representatives(sets):
    n = len(sets)
    representatives = [0] * n
    used = set()

    def backtrack(index):
        if index == n:
            return True

        for element in sets[index]:
            if element not in used:
                representatives[index] = element
                used.add(element)
                if backtrack(index + 1):
                    return True
                used.remove(element)

        return False

    if backtrack(0):
        return 'Y', representatives
    else:
        return 'N',

with open('in.txt', 'r') as file:
    sets_input = []
    n = int(file.readline().strip())
    for _ in range(n):
        line = list(map(int, file.readline().strip().split()))
        sets_input.append(line[:-1])  # Remove 0 at the end of each line

result = find_distinct_representatives(sets_input)

with open('out.txt', 'w') as file:
    if result[0] == 'Y':
        file.write('Y\n')
        file.write(' '.join(map(str, result[1])) + '\n')
    else:
        file.write('N\n')
