from backend.models.incident import Incident

incident = Incident.create(
    tower="storage",
    source="storage-cluster-a",
    severity="critical",
    anomaly_type="high_latency",
    message="Storage latency exceeded threshold"
)

print(incident.to_dict())