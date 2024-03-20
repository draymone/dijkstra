import csv
import dijkstra
from math import acos, sin, cos, radians
from typing import Dict, List

import usa_data


def make_list_donnes_etats(file_name: str) -> List[List]:
    """Takes in input a CSV, returns a list with the data of each state"""
    with open(file_name, newline="") as file:
        result = []
        reader = csv.reader(file, delimiter=';', quotechar='|')
        for row in reader:
            result.append(row)
        return result


def distance_etats(state1: int, state2: int, data: List[List]) -> float:
    earth_radius = 6370.7
    lat1 = radians(float(data[state1][3]))
    lon1 = radians(float(data[state1][4]))
    lat2 = radians(float(data[state2][3]))
    lon2 = radians(float(data[state2][4]))

    return earth_radius * acos(
        sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon2-lon1)
    )


def make_list_adja(adjacent_states: List[List[int]],
                   data: List[list]) -> Dict[str, Dict[str, float]]:
    """

    :param adjacent_states: A list of states, each element is the list of adjacent states to it
    :param data: A list of states, each element contains (in the order) the state's: abbreviation, name, capital city,
    latitude, longitude
    :return:
    """
    result: Dict[str, Dict[str, float]] = {}  # Store the result
    for state in range(len(data)):  # For each state
        state_connections: Dict[str, float] = {}  # Store the connections
        for adjacent_state in adjacent_states[state]:  # For each adjacent state
            state_connections[str(adjacent_state)] = distance_etats(state, adjacent_state, data)  # Add the distance
        result[str(state)] = state_connections
    return result  # Return the result


if __name__ == '__main__':
    statesData: List[List] = make_list_donnes_etats('states.csv')
    adjacenceList: Dict[str, Dict[str, float]] = make_list_adja(usa_data.etats_adjacents, statesData)
    dijkstra.display_shortest_path_usa(adjacenceList, "18", "30", statesData)
