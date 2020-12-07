import pandas as pd
import json


data = {}

coordinates = pd.read_csv("data/coordinates.csv")
waiting_times = pd.read_csv("data/waiting_times.csv")


for stop in coordinates["Paradas"]:
    stop_data = coordinates[(coordinates["Paradas"] == stop)]

    data[stop] = {
        "x": int(stop_data["x"].iloc[0]), 
        "y": int(stop_data["y"].iloc[0]),
        "color": stop_data["Color"].iloc[0],
        "edges": []
    }


for _, route in waiting_times.iterrows():
    data[route["Stop 1"]]["edges"].append([int(route["Duration"]), route["Stop 2"]])
    data[route["Stop 2"]]["edges"].append([int(route["Duration"]), route["Stop 1"]])


with open("data/graph.json", 'w') as json_file:
    json.dump(data, json_file)
