
import json
import yaml
import jsonschema

class RuleValidator:
    def __init__(self, schema_path):
        with open(schema_path, "r") as f:
            self.schema = json.load(f)
            
    def validate_file(self, file_path):
        with open(file_path, "r") as f:
            if file_path.endswith(".json"):
                data = json.load(f)
            elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
                data = yaml.safe_load(f)
            else:
                raise ValueError("Unsupported file format")
        
        jsonschema.validate(instance=data, schema=self.schema)
        return True
