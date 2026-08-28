
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
