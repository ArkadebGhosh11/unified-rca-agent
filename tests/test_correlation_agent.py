from backend.agents.correlation_agent import (
    CorrelationAgent
)

agent = CorrelationAgent()

incidents = [
    {
        "tower": "storage",
        "severity": "critical"
    },
    {
        "tower": "application",
        "severity": "critical"
    }
]

result = agent.correlate(
    incidents
)

print(result)