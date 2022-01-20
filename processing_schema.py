import os
import json
import warnings
from sys import argv


def schema2md_list(schema, outfile='schema_md.out'):
    out_text = "| Property | Description |  Data Type  |\n| :---------- | :------------- | :------------- |\n"
    props = schema.get("properties", {})
    for prop, prop_specifications in props.items():
        description = schema.get("description")
        data_type = schema.get("type")
        out_text += "| `{}` | {} | `{}` |\n".format(prop, description, data_type)
    with open(outfile, "a+") as fn:
        fn.write(out_text)


if __name__ == "__main__":
    kwargs = []
    try:
        schema_argv = argv[1]
        kwargs = argv[1:]
    except IndexError:
        schema_argv = None
        warnings.warn("Error. This script requires a json file argument.")
    schema_list = []
    if os.path.isfile(schema_argv):
        schema_list.append(schema_argv)
    elif os.path.isdir(schema_argv):
        for file in [os.path.join(schema_argv, f) for f in os.listdir(schema_argv) if os.path.isfile(os.path.join(schema_argv, f))]:
            schema_list.append(file)

    for schema_json in schema_list:
        with open(schema_json, 'r') as f:
            schema_dict = json.load(f)
        schema2md_list(schema_dict)
        print(schema_json, " converted.")
