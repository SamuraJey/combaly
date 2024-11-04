class BoruvkaKraskal:
    used = {}
    result = {}
    sum = 0
    count = 1

    @staticmethod
    def compute_tree_weight(vertex, matrix):
        '''
        Compute the weight of the tree using Boruvka-Kraskal algorithm
        '''
        BoruvkaKraskal.result = {i: f"" for i in range(1, vertex + 1)}
        # for i in range(1, vertex + 1):
        #     BoruvkaKraskal.result[i] = ""
        while True:
            if not BoruvkaKraskal.process(vertex, matrix):
                break
        BoruvkaKraskal.sort_vertex_mapping()

    @staticmethod
    def process(vertex, matrix):
        min_edge = float('inf')
        x, y = -1, -1
        for i in range(1, vertex + 1):
            for j in range(i + 1, vertex + 1):
                if matrix[i][j] != -1 and matrix[i][j] < min_edge:
                    min_edge = matrix[i][j]
                    x, y = i, j
        if min_edge == float('inf'):
            return False
        BoruvkaKraskal.arrangement_vertex(min_edge, x, y, matrix)
        return True

    @staticmethod
    def arrangement_vertex(edge_weight, x, y, matrix):
        if BoruvkaKraskal.check_used_vertex_update(x, y):
            BoruvkaKraskal.sum += edge_weight
            BoruvkaKraskal.result[x] += f"{y} "
            BoruvkaKraskal.result[y] += f"{x} "
        matrix[x][y] = -1

    @staticmethod
    def check_used_vertex_update(x, y):
        one = BoruvkaKraskal.set_update(x)
        two = BoruvkaKraskal.set_update(y)

        if one == two and one != -1:
            return False
        if one == two and one == -1:
            BoruvkaKraskal.used[BoruvkaKraskal.count] = [x, y]
            BoruvkaKraskal.count += 1
            return True
        if one != -1 and two != -1:
            BoruvkaKraskal.used[one].extend(BoruvkaKraskal.used[two])
            del BoruvkaKraskal.used[two]
            return True
        if one == -1:
            BoruvkaKraskal.used[two].append(x)
            return True
        if two == -1:
            BoruvkaKraskal.used[one].append(y)
            return True
        return False

    @staticmethod
    def set_update(value):
        for key, vertices in BoruvkaKraskal.used.items():
            if value in vertices:
                return key
        return -1

    @staticmethod
    def sort_vertex_mapping():
        for key, proc in BoruvkaKraskal.result.items():
            sorted_vertices = sorted(map(int, proc.split()))
            BoruvkaKraskal.result[key] = " ".join(map(str, sorted_vertices)) + " 0"


def reader(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    amount_of_elements = int(lines[0].strip())
    all_values = []
    for line in lines[1:]:
        all_values.extend(map(int, line.split()))
    return amount_of_elements, all_values


def make_list(all_values):
    graph = {}
    for i in range(len(all_values)):
        el = all_values[i]
        if el == len(all_values):
            break
        el2 = all_values[i + 1]
        adjacency_list = []
        for j in range(0, el2 - el, 2):
            adjacent = {all_values[el - 1 + j]: all_values[el + j]}
            adjacency_list.append(adjacent)
        graph[i + 1] = adjacency_list
    return graph


def make_matrix(graph, vertex):
    matrix = [[-1] * (vertex + 1) for _ in range(vertex + 1)]
    for x, edges in graph.items():
        for edge in edges:
            for y, weight in edge.items():
                matrix[x][y] = weight
    return matrix


def write_result(file_path):
    with open(file_path, 'w') as file:
        for key, value in BoruvkaKraskal.result.items():
            file.write(f"{value}\n")
        file.write(str(BoruvkaKraskal.sum))


def main():
    amount_of_elements, all_values = reader('in.txt')
    graph = make_list(all_values)
    vertex = len(graph)
    matrix = make_matrix(graph, vertex)
    BoruvkaKraskal.compute_tree_weight(vertex, matrix)
    write_result('out.txt')


if __name__ == "__main__":
    main()