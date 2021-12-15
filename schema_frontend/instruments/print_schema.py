import os
import json
from sys import argv

if __name__ == "__main__":
    kwargs = []
    try:
        schema_json = argv[1]
    except IndexError:
        schema_json = os.path.join(os.getcwd(), "electrochemistry.schema.json")

    with open(schema_json, 'r') as f:
        schema_dict = json.load(f)

    properties = schema_dict.get('properties')
    for prop, info in properties.items():
        print("{}: \t{}".format(" ".join(prop.split('_')).capitalize(), info.get('description')))
