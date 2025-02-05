from shapely.geometry import Polygon

def find_adjacent_polygons(polygons):
    adjacency_dict = {}
    polygon_objects = {key: Polygon(coords) for key, coords in polygons.items()}
    
    for poly_name, poly_geom in polygon_objects.items():
        adjacency_dict[poly_name] = []
        for other_name, other_geom in polygon_objects.items():
            if poly_name != other_name and poly_geom.touches(other_geom):
                adjacency_dict[poly_name].append(other_name)
    
    return adjacency_dict

# Sample Input
polygons = {
    "Polygon_1": [(0,0), (2,0), (2,2), (0,2)],
    "Polygon_2": [(2,0), (4,0), (4,2), (2,2)],
    "Polygon_3": [(2,2), (4,2), (4,4), (2,4)],
    "Polygon_4": [(0,2), (2,2), (2,4), (0,4)]
}

# Compute adjacency
adjacency = find_adjacent_polygons(polygons)
print(adjacency)
