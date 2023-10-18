import json

parse_dict = {"username": "Will", "message": "test1"}
with open("storage/data.json", encoding="utf-8") as file:
    current_data = json.load(file)


parse_dict.update(current_data)
print(parse_dict)
