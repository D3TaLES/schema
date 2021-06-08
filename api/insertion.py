import jsonschema
import warlock
import json

class Insert2DB():
    def __init__(self,schema_path=None):
        with open(schema_path,"rb") as f:
            schema = json.load(f)
        self.schema = warlock.model_factory(schema)



