"""
incident.py

Standard incident model used across the platform.
"""

from dataclasses import dataclass
from datetime import datetime, UTC
from typing import Optional


@dataclass
class Incident:

    tower: str
    source: str
    severity: str
    anomaly_type: str
    message: str
    timestamp: str

    incident_id: Optional[str] = None
    root_cause: Optional[str] = None
    confidence: Optional[float] = None
    resolution: Optional[str] = None

    @classmethod
    def create(
        cls,
        tower,
        source,
        severity,
        anomaly_type,
        message,
        incident_id=None
    ):
        return cls(
            tower=tower,
            source=source,
            severity=severity,
            anomaly_type=anomaly_type,
            message=message,
            timestamp=datetime.now(UTC).isoformat(),
            incident_id=incident_id
        )

    def to_dict(self):
        return {
            "incident_id": self.incident_id,
            "tower": self.tower,
            "source": self.source,
            "severity": self.severity,
            "anomaly_type": self.anomaly_type,
            "message": self.message,
            "timestamp": self.timestamp,
            "root_cause": self.root_cause,
            "confidence": self.confidence,
            "resolution": self.resolution
        }