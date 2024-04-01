import math
from typing import Dict, List, Tuple


def lower_distance_vertex(vertices_to_visit: List[str],
                          distance: Dict[str, int | float]) -> str | None:
    """Picks the closest vertex.

    Returns the vertex with the lower associated distance.

    :param vertices_to_visit: The list of vertices
    :param distance: The dict that associates to it's vertex his distance
    :return: The closest vertex
    """
    # Sets the minimal distance to infinity
    closest_vertex: str | None = None
    min_distance: int | float = math.inf
    for sommet in vertices_to_visit:  # For each vertex
        if distance[sommet] < min_distance:  # If the distance is lower than the actual distance
            closest_vertex = sommet  # Update the closest vertex field
            min_distance = distance[sommet]  # And the min distance field
    return closest_vertex  # Return the closest vertex


def dijkstra_opti(graph: Dict[str, Dict[str, int | float]],
                  start: str,
                  end: str) -> (Dict[str, int | float], Dict[str, str | None]):
    """Optimized dijkstra's algorithm.

    Optimized dijkstra's algorithm implementation, stops when the distance between the start and end vertices is found.

    :param graph: Graph's adjacence list
    :param start: The start vertex
    :param end: The wanted vertex
    :return: Tuple contaning: a dictionary that associates to each vertex it's distance with the start vertex; a
    dictionarty that associates to each vertex it's parent
    """
    # Creation of the dictionnaries
    distance: Dict[str, int | float] = {}
    parent: Dict[str, str | None] = {}

    # Initialisation of the distances as infinite
    for vertex in graph:
        distance[vertex] = math.inf

    # Mark the start vertex
    distance[start] = 0
    parent[start] = None

    vertices_to_visit = [vertex for vertex in graph]  # Create an array with the vertices that are not yet visited

    # Algorithm's main loop
    while len(vertices_to_visit) >= 1:
        closest_vertex = lower_distance_vertex(vertices_to_visit, distance)  # Get the vertex with the lower distance
        if closest_vertex == end:  # If the found vertex is the wanted one
            return distance, parent  # Return
        else:
            vertices_to_visit.remove(closest_vertex)  # Remove the chosen vertex from the array
            neighbors = [vertex for vertex in graph[closest_vertex]  # Get the vertex's neighbors
                         if vertex in vertices_to_visit]  # If they have not yet been visited
            for neighbor in neighbors:  # For each non visited neighbor
                # Process the total distance
                total_distance = distance[closest_vertex] + graph[closest_vertex][neighbor]
                if total_distance < distance[neighbor]:  # If the distance is lower than the actual one
                    # Update the dictionaries
                    parent[neighbor] = closest_vertex
                    distance[neighbor] = total_distance


def dijkstra(graph: Dict[str, Dict[str, int | float]],
             start: str) -> (Dict[str, int | float], Dict[str, str | None]):
    """Dijkstra's algorithm.

    Dijkstra's algorithm implementation.

    :param graph: Graph's adjacence list
    :param start: The start vertex
    :return: Tuple contaning: a dictionary that associates to each vertex it's distance with the start vertex; a
    dictionarty that associates to each vertex it's parent
    """
    # Creation of the dictionnaries
    distance: Dict[str, int | float] = {}
    parent: Dict[str, str | None] = {}

    # Initialisation of the distances as infinite
    for vertex in graph:
        distance[vertex] = math.inf

    # Mark the start vertex
    distance[start] = 0
    parent[start] = None

    vertices_to_visit = [sommet for sommet in graph]  # Create an array with the vertices that are not yet visited

    # Algorithm's main loop
    while len(vertices_to_visit) >= 1:
        closest_vertex = lower_distance_vertex(vertices_to_visit, distance)  # Get the vertex with the lower distance
        vertices_to_visit.remove(closest_vertex)  # Remove the chosen vertex from the array
        # création du tableau des voisins du sommet choisi
        neighbors = [sommet for sommet in graph[closest_vertex]  # Get the vertex's neighbors
                     if sommet in vertices_to_visit]  # If they have not yet been visited
        for neighbor in neighbors:  # For each non visited neighbor
            # Process the total distance
            total_distance = distance[closest_vertex] + graph[closest_vertex][neighbor]
            if total_distance < distance[neighbor]:  # If the distance is lower than the actual one
                # Update the dictionaries
                parent[neighbor] = closest_vertex
                distance[neighbor] = total_distance
    return distance, parent  # Return


def display_shortest_path(graph: Dict[str, Dict[str, int | float]],
                          start: str,
                          end: str) -> None:
    """Display the lower distance between two vertices

    Print the lower distance between two vertices in the console using dijkstra's algorithm

    :param graph: The adjacence list
    :param start: The start vertex
    :param end: The end vertex
    :return:
    """
    distance, parent = dijkstra_opti(graph, start, end)  # Dijkstra's algorithm
    print(f"La distance de {start} à {end} est de longueur {distance[end]}.")  # Print the distance
    # Print the path
    chemin = end
    sommet = end
    while sommet != start:
        chemin = parent[sommet] + ' --> ' + chemin
        sommet = parent[sommet]
    print(f"Le chemin de {start} à {end} : {chemin}.")


def display_shortest_path_usa(graph: Dict[str, Dict[str, int | float]],
                              start: str,
                              end: str,
                              data: List[List]) -> None:
    """Display the lower distance between two vertices

    Print the lower distance between two vertices in the console using dijkstra's algorithm

    :param graph: The adjacence list
    :param start: The start vertex
    :param end: The end vertex
    :param data: The list that contains states data (abbreviation, name, capital city, coordinates)
    :return:
    """

    def capital_city(state: str) -> str:
        """Get a state's capital city

        :param state: State's index
        :return: State's capital city
        """
        return data[int(state)][2]

    distance, parent = dijkstra_opti(graph, start, end)  # Dijkstra's algorithm
    # Print the distance
    print(f"La distance de {capital_city(start)} à {capital_city(end)} est de longueur {distance[end]}.")

    # Print the path
    chemin = capital_city(end)
    sommet = end
    while sommet != start:
        chemin = capital_city(parent[sommet]) + ' --> ' + chemin
        sommet = parent[sommet]
    print(f"Le chemin de {capital_city(start)} à {capital_city(end)} : {chemin}.")


def shortest_path_usa(graph: Dict[str, Dict[str, int | float]],
                      start: str,
                      end: str) -> Tuple[float, List[int]]:
    """Return the lower distance between two states and the shortest path

    Return the lower distance between two states and the shortest path using dijkstra's algorithm

    :param graph: The adjacence list
    :param start: The start vertex
    :param end: The end vertex
    :return (float, int[]): Tuple containing: the distance between the two states, the shortest path between them
    """
    distance, parent = dijkstra_opti(graph, start, end)  # Dijkstra's algorithm

    # Get the path
    path = [int(end)]
    vertex = end
    while vertex != start:
        path.append(int(parent[vertex]))
        vertex = parent[vertex]

    # Return
    return distance[end], path
