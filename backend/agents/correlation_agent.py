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

        storage_incident = None
        network_incident = None
        compute_incident = None
        application_incident = None

        for incident in incidents:

            tower = incident.get(
                "tower"
            )

            if (
                tower == "storage"
                and
                incident.get(
                    "severity"
                ) == "critical"
            ):
                storage_incident = incident

            elif (
                tower == "network"
                and
                incident.get(
                    "severity"
                ) == "critical"
            ):
                network_incident = incident

            elif (
                tower == "compute"
                and
                incident.get(
                    "severity"
                ) == "critical"
            ):
                compute_incident = incident

            elif (
                tower == "application"
                and
                incident.get(
                    "severity"
                ) == "critical"
            ):
                application_incident = incident

        # Storage causing application slowdown

        if (
            storage_incident
            and
            application_incident
        ):

            return {
                "root_cause":
                    storage_incident.get(
                        "component",
                        "storage-cluster-a"
                    ),
                "confidence": 0.98,
                "reason":
                    "Storage degradation "
                    "caused application slowdown"
            }

        # Network causing service degradation

        if (
            network_incident
            and
            application_incident
        ):

            return {
                "root_cause":
                    network_incident.get(
                        "component",
                        "core-network"
                    ),
                "confidence": 0.95,
                "reason":
                    "Network degradation "
                    "caused application impact"
            }

        # Compute resource exhaustion

        if compute_incident:

            return {
                "root_cause":
                    compute_incident.get(
                        "component",
                        "worker-node-01"
                    ),
                "confidence": 0.90,
                "reason":
                    "Compute resource exhaustion "
                    "impacted services"
            }

        # Storage only

        if storage_incident:

            return {
                "root_cause":
                    storage_incident.get(
                        "component",
                        "storage-cluster-a"
                    ),
                "confidence": 0.95,
                "reason":
                    "Storage degradation detected"
            }

        # Network only

        if network_incident:

            return {
                "root_cause":
                    network_incident.get(
                        "component",
                        "core-network"
                    ),
                "confidence": 0.90,
                "reason":
                    "Network degradation detected"
            }

        return {
            "root_cause": "unknown",
            "confidence": 0.2,
            "reason": "Insufficient evidence"
        }