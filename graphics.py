import walk_usa
from dijkstra import shortest_path_usa
from tkinter import Tk, Canvas, PhotoImage, Label
from typing import List, Dict, Tuple
import usa_data


# List with each state's coordinates on the map
coordinates: List[Tuple[int, int]] = [
    (668, 443),
    (189, 564),
    (188, 398),
    (554, 396),
    (51, 245),
    (332, 275),
    (871, 190),
    (843, 264),
    (709, 481),
    (705, 400),
    (35, 410),   # Hawai
    (164, 159),
    (596, 275),  # Illinois
    (656, 271),
    (527, 238),  # Iowa
    (491, 297),  # Kansas
    (684, 307),
    (583, 489),  # Louisana
    (896, 120),
    (817, 261),  # Maryland
    (887, 167),
    (672, 198),  # Michigan
    (529, 159),
    (597, 447),  # Mississipi
    (556, 304),
    (235, 108),  # Montana
    (473, 258),
    (94, 250),   # Nevada
    (881, 148),
    (849, 227),  # New Jersey
    (303, 362),
    (846, 174),  # New York
    (800, 342),
    (419, 123),  # North Dakota
    (709, 260),
    (457, 376),  # Oklahoma
    (67, 109),
    (810, 233),  # Pennsylvania
    (890, 186),
    (765, 384),  # South Carolina
    (419, 173),
    (548, 358),  # Tenessee
    (455, 494),  # Texas
    (217, 236),
    (853, 130),  # Vermont
    (813, 298),
    (95, 70),    # Washington
    (737, 296),
    (595, 203),  # Wisconsin
    (336, 242),  # Wycoming
]


def display_path(distance: float,
                 path: List[int]) -> None:
    """Display the shortest path between two states

    Display the shortest path between two states graphically using Tkinter

    :param distance: the distance
    :param path: the path
    :return:
    """
    window: Tk = Tk()  # Create the window
    window.geometry("1000x700")  # Set the size

    # Canvas
    canvas: Canvas = Canvas(window, width=1000, height=633)
    canvas.pack()

    # Draw background
    img = PhotoImage(file="assets/usa_map.png")
    canvas.create_image(0, 0, anchor="nw", image=img)

    # Draw path
    for i in range(len(path)-1):
        # Get states ids
        state1: int = path[i]
        state2: int = path[i+1]

        # Get states coordinates
        x1, y1 = coordinates[state1]
        x2, y2 = coordinates[state2]

        canvas.create_line(x1, y1, x2, y2, fill="#ff0000", width=3)  # Draw the line

    # Display distance
    distance_display = Label(window, text=f"Distance: {distance}km")
    distance_display.pack()

    window.mainloop()  # Main loop to display the window


def main():
    # Get the data
    states_data: List[List] = walk_usa.read_csv('states.csv')
    adjacence_list: Dict[str, Dict[str, float]] = walk_usa.make_adjacence_list(usa_data.adjacent_states, states_data)

    state1 = input("In which state are you in ? (alphabetical index starting at 0) ")
    state2 = input("Where do you want to go ? ")

    distance, path = shortest_path_usa(adjacence_list, state1, state2)
    display_path(distance, path)


if __name__ == '__main__':
    main()
