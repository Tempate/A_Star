import pandas as pd
import json


DATA_DIR = "data/"

GRAPH_FILENAME = "graph.json"
COORDINATES_FILENAME = "coordinates.csv"
CONNECTIONS_FILENAME = "connections.csv"


graph = {}


def main():
    parse_coordinates()
    parse_connections()

    with open(DATA_DIR + GRAPH_FILENAME, 'w') as json_file:
        json.dump(graph, json_file)


def parse_coordinates():
    coordinates = pd.read_csv(DATA_DIR + COORDINATES_FILENAME)

    for stop in coordinates["Stops"]:
        stop_row = coordinates[(coordinates["Stops"] == stop)]

        colors = stop_row["Color"].iloc[0].split()
        is_intersection = len(colors) > 1

        # We make a different node for every line that goes through a station
        # This simplifies dealing with transshipments
        for color in colors:
            name = stop

            if is_intersection:
                name += "(" + color + ")"

            graph[name] = {
                "x": int(stop_row["x"].iloc[0]), 
                "y": int(stop_row["y"].iloc[0]),
                "color": color,
                "edges": []
            }


def parse_connections():
    connections = pd.read_csv(DATA_DIR + CONNECTIONS_FILENAME)

    for _, route in connections.iterrows():
        # A station will have more than a name if it's an intersection
        stops1 = get_stop_names_for_station(route["Stop 1"])
        stops2 = get_stop_names_for_station(route["Stop 2"])

        for stop1 in stops1:
            for stop2 in stops2:
                # Connections need to be replicated in both directions
                graph[stop1]["edges"].append([int(route["Duration"]), stop2])
                graph[stop2]["edges"].append([int(route["Duration"]), stop1])


def get_stop_names_for_station(station):
    if station in graph.keys():
        return [station]

    return [name for name in graph.keys() if station in name]



if __name__ == "__main__":
    main()
