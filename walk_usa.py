import csv
from math import acos, sin, cos, radians
from typing import Dict, List

import dijkstra
import usa_data


def read_csv(file_name: str) -> List[List]:
    """Reads a CSV file, returns an array with the states data

    :param file_name: The CSV file's name
    :return: An array with the data from the csv
    """
    with open(file_name, newline="") as file:  # Open the file
        result = []  # Store the result
        reader = csv.reader(file, delimiter=';', quotechar='|')  # Read the file

        # Build the result
        for row in reader:
            result.append(row)

        return result  # Return


def distance_between_states(state1: int, state2: int, data: List[List]) -> float:
    """Calculate the disance between two states

    Calculate the orthodromic disance between two states

    :param state1: The first state
    :param state2: The second state
    :param data: The list that contains states data (abbreviation, name, capital city, coordinates)
    :return: The distance between the two states
    """
    earth_radius = 6370.7
    lat1 = radians(float(data[state1][3]))
    lon1 = radians(float(data[state1][4]))
    lat2 = radians(float(data[state2][3]))
    lon2 = radians(float(data[state2][4]))

    return earth_radius * acos(
        sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)
    )


def make_adjacence_list(adjacent_states: List[List[int]],
                        data: List[list]) -> Dict[str, Dict[str, float]]:
    """Build an adjacence list

    Build an adjacence list from the states data and the links between them

    :param adjacent_states: A list of states, each element is the list of adjacent states to it
    :param data: The list that contains states data (abbreviation, name, capital city, coordinates)
    :return:
    """
    result: Dict[str, Dict[str, float]] = {}  # Store the result
    for state in range(len(data)):  # For each state
        state_connections: Dict[str, float] = {}  # Store the connections
        for adjacent_state in adjacent_states[state]:  # For each adjacent state
            state_connections[str(adjacent_state)] = distance_between_states(state, adjacent_state, data)  # Add the distance
        result[str(state)] = state_connections
    return result  # Return the result


if __name__ == '__main__':
    # Test the program
    statesData: List[List] = read_csv('states.csv')
    adjacenceList: Dict[str, Dict[str, float]] = make_adjacence_list(usa_data.adjacent_states, statesData)
    dijkstra.display_shortest_path_usa(adjacenceList, "18", "30", statesData)
    print(dijkstra.shortest_path_usa(adjacenceList, "18", "30"))
