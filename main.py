from typing import Dict

import dijkstra

if __name__ == '__main__':
    # Graphs for testing the algorithm
    test_graph: Dict[str, Dict[str, int | float]] = {
        "a": {"b": 3, "c": 1},
        "b": {"a": 3, "c": 2, "d": 2},
        "c": {"a": 1, "b": 2, "d": 3, "e": 5},
        "d": {"b": 2, "c": 3, "e": 1, "f": 3},
        "e": {"c": 5, "d": 1, "f": 1},
        "f": {"d": 3, "e": 1},
    }

    city_graph: Dict[str, Dict[str, int | float]] = {
        "berlin": {"budapest": 935, "kiev": 1346, "milan": 1036,
                   "paris": 1047},
        "budapest": {"berlin": 935, "kiev": 1121, "milan": 954},
        "kiev": {"berlin": 1346, "budapest": 1121},
        "madrid": {"milan": 1570, "paris": 1271},
        "milan": {"berlin": 1036, "budapest": 954, "madrid": 1570,
                  "paris": 849},
        "paris": {"berlin": 1047, "madrid": 1271, "milan": 849},
    }

    dijkstra.display_shortest_path(test_graph, "a", "f")
    print("------------------------------------------------")
    dijkstra.display_shortest_path(city_graph, "madrid", "kiev")
    print("------------------------------------------------")
    dijkstra.display_shortest_path(city_graph, "kiev", "paris")
