import os
import json

folder_path = "data"
json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

data_array = []

for file_name in json_files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        eventType = data.get("eventType", None)
        if eventType is not None and eventType == "DOCUMENT_RESPONSES":
            data_array.append(data)