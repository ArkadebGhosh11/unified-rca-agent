"""
anomaly_agent.py

Detects anomalies across telemetry towers.
"""

from datetime import datetime, UTC


class AnomalyAgent:

    def detect_anomaly(
        self,
        metric
    ):

        tower = metric.get(
            "tower"
        )

        if tower == "storage":

            return self.detect_storage_anomaly(
                metric
            )

        elif tower == "application":

            return self.detect_application_anomaly(
                metric
            )

        elif tower == "network":

            return self.detect_network_anomaly(
                metric
            )

        elif tower == "compute":

            return self.detect_compute_anomaly(
                metric
            )

        return None

    def detect_storage_anomaly(
        self,
        metric
    ):

        if metric.get(
            "latency_ms",
            0
        ) > 200:

            return {
                "tower": "storage",
                "component":
                    metric.get(
                        "component",
                        "storage-cluster-a"
                    ),
                "severity": "critical",
                "anomaly_type": "high_latency",
                "message":
                    "Storage latency exceeded threshold",
                "timestamp":
                    datetime.now(
                        UTC
                    ).isoformat()
            }

        return None

    def detect_application_anomaly(
        self,
        metric
    ):

        if metric.get(
            "response_time_ms",
            0
        ) > 2000:

            return {
                "tower": "application",
                "service":
                    metric.get(
                        "service",
                        "unknown-service"
                    ),
                "component":
                    metric.get(
                        "service",
                        "unknown-service"
                    ),
                "severity": "critical",
                "anomaly_type": "slow_response",
                "message":
                    "Application response time exceeded threshold",
                "timestamp":
                    datetime.now(
                        UTC
                    ).isoformat()
            }

        return None

    def detect_network_anomaly(
        self,
        metric
    ):

        if metric.get(
            "latency_ms",
            0
        ) > 100:

            return {
                "tower": "network",
                "component":
                    metric.get(
                        "component",
                        "core-network"
                    ),
                "severity": "critical",
                "anomaly_type": "high_latency",
                "message":
                    "Network latency exceeded threshold",
                "timestamp":
                    datetime.now(
                        UTC
                    ).isoformat()
            }

        return None

    def detect_compute_anomaly(
        self,
        metric
    ):

        if metric.get(
            "cpu_percent",
            0
        ) > 85:

            return {
                "tower": "compute",
                "component":
                    metric.get(
                        "component",
                        "worker-node-01"
                    ),
                "severity": "critical",
                "anomaly_type": "high_cpu",
                "message":
                    "CPU utilization exceeded threshold",
                "timestamp":
                    datetime.now(
                        UTC
                    ).isoformat()
            }

        return None