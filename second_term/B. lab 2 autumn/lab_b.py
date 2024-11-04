def find_distinct_representatives(sets: list) -> tuple:
    n = len(sets)
    representatives = [0] * n
    used = set()

    def backtrack(index: int) -> bool:
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


def read_input(file_path: str) -> list:
    with open(file_path, 'r') as file:
        inputs = []
        n = int(file.readline().strip())
        for _ in range(n):
            # We don't need to convert the elements to integers, because we don't use them as integers
            # using strings expands the program's capabilities
            line = list(file.readline().strip().split())
            # line = list(map(int, file.readline().strip().split()))
            inputs.append(line[:-1])  # Remove 0 at the end of each line
        return inputs


def write_output(file_path: str, result: tuple) -> None:
    with open(file_path, 'w') as file:
        if result[0] == 'Y':
            file.write('Y\n')
            file.write(' '.join(map(str, result[1])) + '\n')
        else:
            file.write('N\n')


def main():
    inputs = read_input('in.txt')
    result = find_distinct_representatives(inputs)
    write_output('out.txt', result)


if __name__ == '__main__':
    main()
