"""
correlation_agent.py

Correlates incidents across towers
to identify probable root causes.
"""


class CorrelationAgent:

    def correlate(
        self,
        incidents
    ):

        if not incidents:

            return {
                "root_cause": "unknown",
                "confidence": 0.0,
                "reason": "No incidents found"
            }

        for incident in incidents:

            if (
                incident["tower"] == "storage"
                and
                incident["severity"] == "critical"
            ):

                return {
                    "root_cause":
                        incident.get(
                            "component",
                            "unknown-component"
                        ),
                    "confidence": 0.95,
                    "reason":
                        "Storage degradation "
                        "correlated with service impact"
                }

        for incident in incidents:

            if (
                incident["tower"] == "network"
                and
                incident["severity"] == "critical"
            ):

                return {
                    "root_cause":
                        incident.get(
                            "component",
                            "unknown-component"
                        ),
                    "confidence": 0.90,
                    "reason":
                        "Network degradation "
                        "correlated with service impact"
                }

        for incident in incidents:

            if (
                incident["tower"] == "compute"
                and
                incident["severity"] == "critical"
            ):

                return {
                    "root_cause":
                        incident.get(
                            "component",
                            "unknown-component"
                        ),
                    "confidence": 0.88,
                    "reason":
                        "Compute resource exhaustion "
                        "correlated with service impact"
                }

        return {
            "root_cause": "unknown",
            "confidence": 0.2,
            "reason": "Insufficient evidence"
        }