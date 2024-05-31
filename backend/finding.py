from backend.utils import get_map_data
import heapq


def get_relations() -> dict[str, list[str]]:
    data = get_map_data()
    relations = {}
    for k, v in data['points'].items():
        relations[k] = v['path']
    return relations

def calc_distance(point1, point2, points):
    x1, y1 = points[point1]
    x2, y2 = points[point2]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def dijkstra(start, end, graph, points):
    queue = [(0, start, [])]
    seen = set()
    mins = {start: 0}

    while queue:
        (cost, v1, path) = heapq.heappop(queue)

        if v1 in seen:
            continue

        seen.add(v1)
        path = path + [v1]

        if v1 == end:
            return (path, cost)

        for v2 in graph.get(v1, []):
            if v2 in seen:
                continue

            prev = mins.get(v2, None)
            next = cost + calc_distance(v1, v2, points)
            if prev is None or next < prev:
                mins[v2] = next
                heapq.heappush(queue, (next, v2, path))

    return float("inf")

# path = get_relations()
# points = get_points()
# start = 'a1'
# end = 'a261'

# shortest_path, distance = dijkstra(start, end, path, points)
# print(shortest_path,distance)
