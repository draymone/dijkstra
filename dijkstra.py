import math
from typing import Dict, List


def sommet_distance_min(sommets_a_visiter: List[str],
                        distance: Dict[str, int | float]) -> str | None:
    """ Prend en entrée un tableau de sommets et un dictionnaire de distances
        Renvoie le sommet à distance minimale
    """
    # la distance affectée à chaque sommet est infinie
    sommet_min: str | None = None
    distance_min: int | float = math.inf
    # pour chaque sommet à visiter, si la distance est inférieure à la distance
    # minimale actuelle, on met à jour les données distance_min et sommet_min
    for sommet in sommets_a_visiter:
        if distance[sommet] < distance_min:
            sommet_min = sommet
            distance_min = distance[sommet]
    # on renvoie le sommet à distance minimale
    return sommet_min


def dijkstra_opti(graphe: Dict[str, Dict[str, int | float]],
                  depart: str,
                  arrivee: str) -> (Dict[str, int | float], Dict[str, str | None]):
    """ Version optimisée de l'algorithme de Djikstra, s'arrête dès que le chemin dmandé est trouvé. Prend en entrée une
    liste d'adjacence (graphe), un sommet de départ et un sommet d'arrivée.
    Renvoie deux dictionnaires :
        - distance : la distance de chaque sommet avec le sommet de départ
        - parent : le parent du sommet dans le chemin minimal à ce sommet
    """
    # création des dictionnaires distance et parent
    distance: Dict[str, int | float] = {}
    parent: Dict[str, str | None] = {}
    # initialisation des distances à l'infini
    for sommet in graphe:
        distance[sommet] = math.inf
    # on marque le départ dans les dictionnaires distance et parent
    distance[depart] = 0
    parent[depart] = None
    # on crée un tableau de sommets non sélectionnés, qui contient tous les
    # sommets du graphe au début
    sommets_a_visiter = [sommet for sommet in graphe]

    # boucle principale de l'algorithme
    while len(sommets_a_visiter) >= 1:
        # récupération du sommet non visité à distance minimale
        sommet_min = sommet_distance_min(sommets_a_visiter, distance)
        # test de sortie de l'algorithme : si le sommet choisi est l'arrivée,
        if sommet_min == arrivee:
            # on renvoie les deux dictionnaires construits.
            return distance, parent
        # dans le cas contraire
        else:
            # on supprime le sommet choisi du tableau des sommets à visiter
            sommets_a_visiter.remove(sommet_min)
            # création du tableau des voisins du sommet choisi
            voisins = [sommet for sommet in graphe[sommet_min] if sommet in sommets_a_visiter]
            # pour chaque sommet voisin non visité
            for voisin in voisins:
                # on calcule la distance totale au voisin
                distance_totale = distance[sommet_min] + graphe[sommet_min][voisin]
                # si la distance calculée est inférieure à la distance actuelle,
                # on met à jour les données distance et parent
                if distance_totale < distance[voisin]:
                    parent[voisin] = sommet_min
                    distance[voisin] = distance_totale


def dijkstra(graph: Dict[str, Dict[str, int | float]],
             start: str) -> (Dict[str, int | float], Dict[str, str | None]):
    """ Prend en entrée une liste d'adjacence (graphe) et un sommet de départ.
    Renvoie deux dictionnaires :
        - distance : la distance de chaque sommet avec le sommet de départ
        - parent : le parent du sommet dans le chemin minimal à ce sommet
    """
    # création des dictionnaires distance et parent
    distance: Dict[str, int | float] = {}
    parent: Dict[str, str | None] = {}
    # initialisation des distances à l'infini
    for sommet in graph:
        distance[sommet] = math.inf
    # on marque le départ dans les dictionnaires distance et parent
    distance[start] = 0
    parent[start] = None
    # on crée un tableau de sommets non sélectionnés, qui contient tous les
    # sommets du graphe au début
    sommets_a_visiter = [sommet for sommet in graph]

    # boucle principale de l'algorithme
    while len(sommets_a_visiter) >= 1:
        # récupération du sommet non visité à distance minimale
        sommet_min = sommet_distance_min(sommets_a_visiter, distance)
        # on supprime le sommet choisi du tableau des sommets à visiter
        sommets_a_visiter.remove(sommet_min)
        # création du tableau des voisins du sommet choisi
        voisins = [sommet for sommet in graph[sommet_min] if sommet in sommets_a_visiter]
        # pour chaque sommet voisin non visité
        for voisin in voisins:
            # on calcule la distance totale au voisin
            distance_totale = distance[sommet_min] + graph[sommet_min][voisin]
            # si la distance calculée est inférieure à la distance actuelle,
            # on met à jour les données distance et parent
            if distance_totale < distance[voisin]:
                parent[voisin] = sommet_min
                distance[voisin] = distance_totale
    return distance, parent


def display_shortest_path(graph: Dict[str, Dict[str, int | float]],
                          start: str,
                          end: str) -> None:
    """ Affiche la distance minimale entre les deux sommets, et le chemin minimal.
    """
    # application de l'algorithme de Dijkstra sur le graphe, entre les deux sommets
    distance, parent = dijkstra_opti(graph, start, end)
    print(f"La distance de {start} à {end} est de longueur {distance[end]}.")
    # affichage du chemin minimal entre les deux sommets
    chemin = end
    sommet = end
    while sommet != start:
        chemin = parent[sommet] + ' --> ' + chemin
        sommet = parent[sommet]
    print(f"Le chemin de {start} à {end} : {chemin}.")
