import heapq
from collections import namedtuple
from typing import NamedTuple


class Data(NamedTuple):
    n: int
    m: int
    start_room: int
    initial_chips: int
    rooms: list[list[int]]
    costs: list[int]


def read() -> Data:
    with open("in.txt", "r") as f:
        n, m, start_room, initial_chips = map(int, f.readline().split())
        rooms = []
        for _ in range(n):
            rooms.append(list(map(int, f.readline().split()))[1:])
        costs = []
        for _ in range(m):
            for i in f.readline().split():
                costs.append(int(i))
    return Data(n, m, start_room, initial_chips, rooms, costs)


def solve(data: Data) -> tuple[dict[int, float], dict[int, list[int]]] | None:
    adj = [[] for _ in range(data.n + 1)]
    for i in range(1, data.n + 1):
        for door in data.rooms[i - 1]:
            for j in range(1, data.n + 1):
                if i != j and door in data.rooms[j - 1]:
                    adj[i].append((j, door))
            if len([room for room in data.rooms if door in room]) == 1:
                adj[i].append((0, door))  # 0 это наружа

    def dijkstra(start: int, chips: int) -> tuple[dict[int, float], dict[int, list[int]]]:
        dist = {i: float('inf') for i in range(data.n + 1)}
        # path = {i: [] for i in range(data.n + 1)}
        dist[start] = 0
        pq = [(0, start, [start])]
        parent = {i: -1 for i in range(data.n + 1)}
        while pq:
            d, u, p = heapq.heappop(pq)

            for v, door in adj[u]:
                cost = data.costs[door - 1]
                if chips >= cost:
                    if dist[v] > dist[u] + cost:
                        dist[v] = dist[u] + cost
                        parent[v] = u
                        heapq.heappush(pq, (dist[v], v, p + [v]))

        cur = 0
        kek_path = []
        while cur != -1:
            cur = parent[cur]
            if cur == -1:
                continue
            kek_path.append(cur)
        kek_path.reverse()
        return dist, kek_path
    try:
        dist, path = dijkstra(data.start_room, data.initial_chips)
    except TypeError as e:
        print(e)
        return None
    return namedtuple("Result", ["dist", "path"])(dist, path)


def write(result: tuple, flag=True) -> None:
    with open("out.txt", "w") as outfile:
        if flag:
            outfile.write("Y\n")
            outfile.write(str(result.dist[0]) + "\n")
            outfile.write(" ".join(map(str, result.path)) + "\n")
            # print("Y")
            # print(result.dist[0])
            # print(*result.path)
        else:
            outfile.write("N\n")
            # print("N")


def main():
    data = read()
    result = solve(data)
    if isinstance(result, tuple) and result.dist[0] <= data.initial_chips and result.dist[0] != float('inf'):
        write(result)
    else:
        write(result=result, flag=False)


if __name__ == "__main__":
    main()
