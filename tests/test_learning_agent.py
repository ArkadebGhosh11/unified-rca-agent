from backend.agents.learning_agent import (
    LearningAgent
)

from backend.agents.rca_agent import (
    RCAAgent
)

learning_agent = LearningAgent()

learning_context = (
    learning_agent.get_learning_context(
        "storage latency issue"
    )
)

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

agent = RCAAgent()

report = agent.generate_rca(
    correlation_result,
    incidents,
    learning_context
)

print(report)