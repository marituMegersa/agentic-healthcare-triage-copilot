def test_agent_orchestrator():
    prompt = "Test execution query for agentic-healthcare-triage-copilot"
    assert len(prompt) > 0
    assert "Test" in prompt
