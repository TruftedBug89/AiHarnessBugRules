
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
