from .utils import get_map_data, get_points


def find_paths(start, end, graph, points):
    def dfs(current, path, length):
        if current == end:
            paths.append((path, length))
            return
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                neighbor_length = length + calc_distance(current, neighbor)
                dfs(neighbor, path + [neighbor], neighbor_length)
        visited.remove(current)

    def calc_distance(point1, point2):
        x1, y1 = map(int, points[point1])
        x2, y2 = map(int, points[point2])
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    paths = []
    visited = set()
    dfs(start, [start], 0)
    return paths


def get_relations() -> dict[str, list[str]]:
    """读取关系文件，并返回一个字典，键为起点，值为一个列表，包含所有终点
    
    例如：{'a1': ['a2', 'a3'], 'a2': ['a1', 'a3'], 'a3': ['a1', 'a2']}
    """    
    data = get_map_data()
    # print()
    relations = {}
    for k,v in data['points'].items():
        # print(k,v['path'])
        relations.update({k:v['path']})
    # print(relations)
    return relations
path: dict[str, list[str]] = get_relations()
# path = {'a1': ['a2', 'a3','a4'], 'a2': ['a1', 'a3'], 'a3': ['a1', 'a2'], 'a4': ['a1', 'a2']}
# points = {'a1': ['100', '100'], 'a2': ['200', '100'], 'a3': ['3 00', '100'], 'a4': ['400', '60']}
points = get_points()
start = 'a1'
end = 'a3'

def get_shortest_path(start:str, 
                      end:str, 
                      path:dict[list[str]], 
                      points:dict[list[str]]
                      
                      )                       -> tuple[list[str], int]:
    """找到从起点到终点的最短路径
    
    返回一个元组，包含路径和路径长度"""
    
    
    paths = find_paths(start, end, path, points)
    shortest_path = min(paths, key=lambda x: x[1])
    return shortest_path


# result = get_shortest_path(start, end, path, points)
# print(result)
# result = find_paths(start, end, paths, points)
# print(result)
# print("Paths from {} to {}:".format(start, end))
# for path, length in result:
#     print("Path:", "->".join(path), "Length:", length)
