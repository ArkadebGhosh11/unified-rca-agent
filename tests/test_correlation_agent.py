from backend.agents.correlation_agent import (
    CorrelationAgent
)

agent = CorrelationAgent()

incidents = [
    {
        "tower": "storage",
        "component":
            "storage-cluster-a",
        "severity":
            "critical"
    },
    {
        "tower": "application",
        "service":
            "checkout-api",
        "severity":
            "critical"
    }
]

result = agent.correlate(
    incidents
)

print(result)