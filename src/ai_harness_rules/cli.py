
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
