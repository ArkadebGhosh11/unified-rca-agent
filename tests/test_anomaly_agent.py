from backend.agents.anomaly_agent import AnomalyAgent

agent = AnomalyAgent()

storage_metric = {
    "component": "storage-cluster-a",
    "latency_ms": 280
}

result = agent.detect_storage_anomaly(
    storage_metric
)

print(result)