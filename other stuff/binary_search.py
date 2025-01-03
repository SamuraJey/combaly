# Задача - дана матрица, в кайждой строке расположенны целые числа по возрастанию, в каждой следующей строке первое число строго больше последнего в предыдущей строке.
# Необходимо найти запрашиваемый элемент или сказать, что его нет
# Пример матрицы
# a = [
#         [1,2,3],
#         [10,20,30],
#         [100,200,300],
#     ]


import heapq
import random
from time import time


def matrix_print(a: list[list[int]]) -> None:
    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]

    print('\n'.join(table))


def sort_matrix(mat: list[list[int]]) -> list[list[int]]:
    # Step 1: Create a min-heap and insert all elements of the matrix into it.
    heap = []
    for row in mat:
        for num in row:
            heapq.heappush(heap, num)

    # Step 2: Extract the minimum element from the heap repeatedly to create a sorted list.
    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))

    # Step 3: Reshape the sorted list back into a matrix.
    n_rows = len(mat)
    n_cols = len(mat[0])
    sorted_mat = [sorted_list[i:i+n_cols] for i in range(0, len(sorted_list), n_cols)]

    return sorted_mat


def prepare_data(n: int, m: int) -> list[list[int]]:
    a = []

    counter = 1
    low_end = 0
    high_end = 10
    for i in range(m):
        # a.append([0]*(n))
        unique_row = set()
        kek = random.randint(low_end, high_end)
        while len(unique_row) < n:
            unique_row.add(kek)
            kek += 1

        counter += 1
        a.append(list(unique_row))

        low_end = max(a[i]) + 1
        high_end = low_end * 2

    return sort_matrix(a)


def get_1d_index(x: int, y: int, w: int) -> int:
    i = y * w + x
    return i


def get_2d_index(i: int, m) -> tuple[int, int]:
    x = i // m
    y = i % m
    return x, y


def binary_search(a: list, value: int) -> tuple[int, int] | bool:
    n = len(a)
    m = len(a[0])

    matrix_low = 0
    matrix_high = n * m - 1
    while matrix_low <= matrix_high:
        matrix_mid = (matrix_high + matrix_low) // 2
        # x = matrix_mid // m
        # y = matrix_mid % m
        x, y = get_2d_index(matrix_mid, m)

        if a[x][y] == value:
            return x, y
        if a[x][y] < value:
            matrix_low = matrix_mid + 1
        else:
            matrix_high = matrix_mid - 1

    return False


def get_correct_answer(a: list[list[int]], value: int) -> tuple[int, int] | bool:
    x, y = None, None
    for arr in a:
        try:
            y = arr.index(value, 0, len(a[0]))
            x = a.index(arr, 0, len(a))
        except ValueError:
            continue
    if x is not None and y is not None:
        return x, y
    else:
        return False


def main() -> tuple[float, float]:
    n = random.randint(100, 100)
    m = random.randint(100, 100)
    a = prepare_data(n, m)

    value_to_find = a[random.randint(0, m-1)][random.randint(0, n-1)]
    binary_start = time()
    result = binary_search(a, value_to_find)
    binary_time = time() - binary_start
    # print(f'binary search time: {binary_time}')

    pythonic_start = time()
    expected_result = get_correct_answer(a, value_to_find)
    pythonic_time = time() - pythonic_start
    # print(f'pythonic search time: {pythonic_time}')

    # print(result)
    # print(expected_result)

    assert result == expected_result

    return binary_time, pythonic_time

    # b = []
    # for lol in a:
    #     for kek in lol:
    #         b.append(kek)


# def test_speed():


if __name__ == '__main__':
    total_time_start = time()
    binary_time_arr = []
    pythonic_time_arr = []
    for i in range(100):
        binary_time, pythonic_time = main()

        binary_time_arr.append(binary_time)
        pythonic_time_arr.append(pythonic_time)

    binary_mean = sum(binary_time_arr) / len(binary_time_arr)
    pythonic_mean = sum(pythonic_time_arr) / len(pythonic_time_arr)
    total_time_end = time()
    print(f'total time to run everything: {total_time_end - total_time_start:.4f}')
    print(f'{binary_mean=:.16f}')
    print(f'{pythonic_mean=:.16f}')
    if binary_mean > pythonic_mean:
        print(f'pythonic way is {binary_mean/pythonic_mean:.2f}x faster')
    elif binary_mean < pythonic_mean:
        print(f'binary way is {pythonic_mean/binary_mean:.2f}x faster')
