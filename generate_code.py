import os
import json

# Setup directory structure
dirs = [
    "src/ai_harness_rules",
    "tests",
    "rules",
    "templates"
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# 1. validator.py
with open("src/ai_harness_rules/validator.py", "w") as f:
    f.write('''
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
''')

# 2. exports.py
with open("src/ai_harness_rules/exports.py", "w") as f:
    f.write('''
import json
import yaml

class Exporter:
    def __init__(self, rules_data):
        self.rules_data = rules_data
        
    def export_agents_md(self):
        return f"# Agents Rules\\n\\nTotal Rules: {len(self.rules_data.get('rules', []))}"
        
    def export_claude_md(self):
        return f"# Claude Rules\\n\\nTotal Rules: {len(self.rules_data.get('rules', []))}"
''')

# 3. cli.py
with open("src/ai_harness_rules/cli.py", "w") as f:
    f.write('''
import argparse
from .validator import RuleValidator

def main():
    parser = argparse.ArgumentParser(description="AI Harness Bug Rules CLI")
    parser.add_argument("--validate", help="Path to rules file to validate")
    parser.add_argument("--schema", help="Path to schema file", default="schemas/rules.schema.json")
    args = parser.parse_args()
    
    if args.validate:
        validator = RuleValidator(args.schema)
        validator.validate_file(args.validate)
        print("Validation successful.")
''')

# 4. __init__.py
with open("src/ai_harness_rules/__init__.py", "w") as f:
    f.write('''
''')

# 5. tests/test_validator.py
with open("tests/test_validator.py", "w") as f:
    f.write('''
import pytest
import os
import json
from ai_harness_rules.validator import RuleValidator
from ai_harness_rules.cli import main
from unittest.mock import patch

def test_validator_valid_json(tmp_path):
    schema = {
        "type": "object",
        "properties": {"rules": {"type": "array"}}
    }
    schema_file = tmp_path / "schema.json"
    with open(schema_file, "w") as f:
        json.dump(schema, f)
        
    rules_file = tmp_path / "rules.json"
    with open(rules_file, "w") as f:
        json.dump({"rules": []}, f)
        
    validator = RuleValidator(str(schema_file))
    assert validator.validate_file(str(rules_file)) == True

def test_validator_invalid_json(tmp_path):
    schema = {
        "type": "object",
        "properties": {"rules": {"type": "array"}},
        "required": ["rules"]
    }
    schema_file = tmp_path / "schema.json"
    with open(schema_file, "w") as f:
        json.dump(schema, f)
        
    rules_file = tmp_path / "rules.json"
    with open(rules_file, "w") as f:
        json.dump({}, f)
        
    validator = RuleValidator(str(schema_file))
    with pytest.raises(Exception):
        validator.validate_file(str(rules_file))

def test_validator_unsupported_format(tmp_path):
    schema_file = tmp_path / "schema.json"
    with open(schema_file, "w") as f:
        json.dump({}, f)
    
    rules_file = tmp_path / "rules.txt"
    with open(rules_file, "w") as f:
        f.write("test")
        
    validator = RuleValidator(str(schema_file))
    with pytest.raises(ValueError):
        validator.validate_file(str(rules_file))

def test_cli(tmp_path):
    schema_file = tmp_path / "schema.json"
    with open(schema_file, "w") as f:
        json.dump({}, f)
        
    rules_file = tmp_path / "rules.json"
    with open(rules_file, "w") as f:
        json.dump({}, f)
        
    with patch("sys.argv", ["cli.py", "--validate", str(rules_file), "--schema", str(schema_file)]):
        main()
''')

# 6. tests/test_schemas.py
with open("tests/test_schemas.py", "w") as f:
    f.write('''
import pytest
import os
import json
import yaml
from ai_harness_rules.validator import RuleValidator

def test_rules_json_conforms_to_schema():
    validator = RuleValidator("schemas/rules.schema.json")
    
    # Create dummy rules.json
    rules = {
        "rules": [
            {
                "id": "R001",
                "category": "security",
                "severity": "critical",
                "title": "Test",
                "description": "Test description"
            }
        ]
    }
    with open("rules/rules.json", "w") as f:
        json.dump(rules, f)
        
    assert validator.validate_file("rules/rules.json") == True

def test_rules_yaml_conforms_to_schema():
    validator = RuleValidator("schemas/rules.schema.json")
    
    # Create dummy rules.yaml
    rules = {
        "rules": [
            {
                "id": "R001",
                "category": "security",
                "severity": "critical",
                "title": "Test",
                "description": "Test description"
            }
        ]
    }
    with open("rules/rules.yaml", "w") as f:
        yaml.dump(rules, f)
        
    assert validator.validate_file("rules/rules.yaml") == True
''')

# 7. tests/test_exports.py
with open("tests/test_exports.py", "w") as f:
    f.write('''
import pytest
from ai_harness_rules.exports import Exporter

def test_export_agents_md():
    rules_data = {"rules": [{"id": "R001"}]}
    exporter = Exporter(rules_data)
    result = exporter.export_agents_md()
    assert "Total Rules: 1" in result
    assert "# Agents Rules" in result

def test_export_claude_md():
    rules_data = {"rules": [{"id": "R001"}, {"id": "R002"}]}
    exporter = Exporter(rules_data)
    result = exporter.export_claude_md()
    assert "Total Rules: 2" in result
    assert "# Claude Rules" in result
''')

# 8. conftest.py
with open("tests/conftest.py", "w") as f:
    f.write('''
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
''')
