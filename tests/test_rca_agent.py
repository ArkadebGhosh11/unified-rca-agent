from backend.agents.rca_agent import RCAAgent

agent = RCAAgent()

correlation_result = {
    "root_cause": "storage-cluster-a",
    "confidence": 0.95,
    "reason":
        "Storage degradation correlated "
        "with application slowdown"
}

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

response = agent.generate_rca(
    correlation_result,
    incidents
)

print(response)
