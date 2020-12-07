import pandas as pd
import json


data = {}

coordinates = pd.read_csv("data/coordinates.csv")
waiting_times = pd.read_csv("data/waiting_times.csv")


for stop in coordinates["Paradas"]:
    stop_data = coordinates[(coordinates["Paradas"] == stop)]

    colors = stop_data["Color"].iloc[0].split()

    for color in colors:
        name = stop

        if len(colors) > 1:
            name += "(" + color + ")"

        data[name] = {
            "x": int(stop_data["x"].iloc[0]), 
            "y": int(stop_data["y"].iloc[0]),
            "color": color,
            "edges": []
        }


def get_stops(stop):
    if stop in data.keys():
        return [stop]

    return [name for name in data.keys() if stop + '(' in name]


for _, route in waiting_times.iterrows():
    stops1 = get_stops(route["Stop 1"])
    stops2 = get_stops(route["Stop 2"])

    for stop1 in stops1:
        for stop2 in stops2:
            data[stop1]["edges"].append([int(route["Duration"]), stop2])
            data[stop2]["edges"].append([int(route["Duration"]), stop1])


print(data)

with open("data/graph.json", 'w') as json_file:
    json.dump(data, json_file)
