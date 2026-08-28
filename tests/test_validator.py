
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
