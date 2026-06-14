"""
test_incident.py

Unit test for Incident model.
"""

from backend.models.incident import Incident


incident = Incident.create(
    incident_id="INC-001",
    tower="storage",
    source="storage-cluster-a",
    severity="critical",
    anomaly_type="high_latency",
    message="Storage latency exceeded threshold"
)

print("\nIncident Object\n")
print(incident)

print("\nIncident Dictionary\n")
print(incident.to_dict())