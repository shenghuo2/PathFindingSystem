
import json
# from re import M


def get_map_data() ->dict[dict[str:dict[dict]]] :
    """
    从map_data.json获取地图数据
    
    :return json(dict): 
    """
    data = open('map_data.json', 'r', encoding='utf-8')
    map_data = data.read()
    map_data = json.loads(map_data)
    data.close()
    return map_data


def process_points() -> dict[int, list[str]]:
    data = get_map_data()
    paths = {}
    path_id = 1


    for point, info in data['points'].items():
        for connected_point in info['path']:
            path = sorted([point, connected_point])
            path_str = ','.join(path)

            if path_str not in paths.values():
                paths[path_id] = path
                path_id += 1


    unique_paths = {}
    for path_id, path in paths.items():
        unique_paths[tuple(path)] = path_id

    return {index+1: list(value[0]) for index, value in enumerate(unique_paths.items())}

def generate_path(points_data:dict[int, list[str]], map_data:dict[dict]) -> dict[int:list[list[str,str],list[str,str]]]:
    paths = {}
    map_data = map_data['points'] 
    # print(map_data)
    for key, value in points_data.items():

        paths.update({
            key:
                [   
                    [
                        map_data[value[0]]['pos']['x'],
                        map_data[value[0]]['pos']['y']
                    ],
                    [
                        map_data[value[1]]['pos']['x'],
                        map_data[value[1]]['pos']['y']
                    ]
                    
                ]
                })
    # print(paths)
    return paths
def get_points() -> dict[str:list[str,str]]:
    map_data = get_map_data()
    points = {}
    for name, value in map_data['points'].items():
        points.update(
            {
            name:
                [
                    value['pos']['x'],
                    value['pos']['y']
                ]
            }
                   )
    # print(tmp)
    return points


# print(get_points())
# print(generate_path(process_points(), get_map_data()))