"""
incident.py

Standard incident model used across the platform.
"""

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class Incident:

    tower: str
    source: str
    severity: str
    anomaly_type: str
    message: str
    timestamp: str

    @classmethod
    def create(
        cls,
        tower,
        source,
        severity,
        anomaly_type,
        message
    ):

        return cls(
            tower=tower,
            source=source,
            severity=severity,
            anomaly_type=anomaly_type,
            message=message,
            timestamp=datetime.now(
                UTC
            ).isoformat()
        )

    def to_dict(self):

        return {
            "tower": self.tower,
            "source": self.source,
            "severity": self.severity,
            "anomaly_type": self.anomaly_type,
            "message": self.message,
            "timestamp": self.timestamp
        }