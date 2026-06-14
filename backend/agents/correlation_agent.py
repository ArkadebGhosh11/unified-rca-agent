"""
correlation_agent.py

Correlates incidents across towers and identifies
likely root causes.
"""


class CorrelationAgent:

    def correlate(self, incidents):

        towers = {
            incident["tower"]
            for incident in incidents
        }

        # Storage -> Application

        if (
            "storage" in towers
            and "application" in towers
        ):
            return {
                "root_cause": "storage-cluster-a",
                "confidence": 0.95,
                "reason":
                    "Storage degradation correlated "
                    "with application slowdown"
            }

        # Network -> Application

        if (
            "network" in towers
            and "application" in towers
        ):
            return {
                "root_cause": "core-network",
                "confidence": 0.90,
                "reason":
                    "Network latency correlated "
                    "with application degradation"
            }

        # Compute only

        if "compute" in towers:
            return {
                "root_cause": "worker-node-01",
                "confidence": 0.85,
                "reason":
                    "High CPU utilization detected"
            }

        return {
            "root_cause": "unknown",
            "confidence": 0.20,
            "reason": "Insufficient evidence"
        }