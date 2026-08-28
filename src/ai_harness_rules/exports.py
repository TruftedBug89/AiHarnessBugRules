
import json
import yaml

class Exporter:
    def __init__(self, rules_data):
        self.rules_data = rules_data
        
    def export_agents_md(self):
        return f"# Agents Rules\n\nTotal Rules: {len(self.rules_data.get('rules', []))}"
        
    def export_claude_md(self):
        return f"# Claude Rules\n\nTotal Rules: {len(self.rules_data.get('rules', []))}"
