from backend.services.incident_memory import (
    IncidentMemory
)

memory = IncidentMemory()

memory.add_incident(
    incident_id="INC-001",
    root_cause="storage-cluster-a",
    resolution="Increase storage IOPS",
    summary="Storage latency spike caused application slowdown"
)

results = memory.search_similar_incidents(
    "storage latency issue"
)

print(results)