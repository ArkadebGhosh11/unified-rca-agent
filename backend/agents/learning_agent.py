"""
learning_agent.py

Retrieves historical incidents and resolutions
to improve RCA generation.
"""

from backend.services.incident_memory import (
    IncidentMemory
)


class LearningAgent:

    def __init__(self):

        self.memory = IncidentMemory()

    def get_learning_context(
        self,
        query
    ):
        """
        Retrieve similar incidents from memory.
        """

        incidents = self.memory.search_similar_incidents(
            query
        )

        if not incidents:

            return {
                "similar_incidents": [],
                "historical_resolutions": []
            }

        resolutions = []

        for incident in incidents:

            if incident.get("resolution"):

                resolutions.append(
                    incident["resolution"]
                )

        return {
            "similar_incidents": incidents,
            "historical_resolutions": resolutions
        }