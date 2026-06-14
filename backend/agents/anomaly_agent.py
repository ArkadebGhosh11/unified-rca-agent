"""
anomaly_agent.py

Detects anomalies across telemetry towers.
"""

from datetime import datetime, UTC


class AnomalyAgent:

    def detect_storage_anomaly(self, metric):

        if metric["latency_ms"] > 200:

            return {
                "tower": "storage",
                "component": metric["component"],
                "severity": "critical",
                "anomaly_type": "high_latency",
                "message": "Storage latency exceeded threshold",
                "timestamp": datetime.now(UTC).isoformat()
            }

        return None

    def detect_application_anomaly(self, metric):

        if metric["response_time_ms"] > 2000:

            return {
                "tower": "application",
                "service": metric["service"],
                "severity": "critical",
                "anomaly_type": "slow_response",
                "message": "Application response time exceeded threshold",
                "timestamp": datetime.now(UTC).isoformat()
            }

        return None

    def detect_network_anomaly(self, metric):

        if metric["latency_ms"] > 100:

            return {
                "tower": "network",
                "component": metric["component"],
                "severity": "critical",
                "anomaly_type": "high_latency",
                "message": "Network latency exceeded threshold",
                "timestamp": datetime.now(UTC).isoformat()
            }

        return None

    def detect_compute_anomaly(self, metric):

        if metric["cpu_percent"] > 85:

            return {
                "tower": "compute",
                "component": metric["component"],
                "severity": "critical",
                "anomaly_type": "high_cpu",
                "message": "CPU utilization exceeded threshold",
                "timestamp": datetime.now(UTC).isoformat()
            }

        return None