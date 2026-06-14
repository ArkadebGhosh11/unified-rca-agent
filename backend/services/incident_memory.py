import json
from pathlib import Path


class IncidentMemory:

    def __init__(self):

        self.memory_file = Path(
            "memory/incidents.json"
        )

        if not self.memory_file.exists():

            self.memory_file.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            self.memory_file.write_text("[]")

    def add_incident(
        self,
        incident_id,
        root_cause,
        resolution,
        summary
    ):

        incidents = self.get_all_incidents()

        # Prevent duplicates
        for incident in incidents:

            if incident["incident_id"] == incident_id:

                print(
                    f"Incident {incident_id} already exists."
                )

                return

        incidents.append(
            {
                "incident_id": incident_id,
                "root_cause": root_cause,
                "resolution": resolution,
                "summary": summary
            }
        )

        with open(
            self.memory_file,
            "w"
        ) as f:

            json.dump(
                incidents,
                f,
                indent=4
            )
        print(
            f"Incident {incident_id} stored successfully."
        )

    def get_all_incidents(self):

        with open(
            self.memory_file,
            "r"
        ) as f:

            return json.load(f)

 
    def search_similar_incidents(
    self,
    query
    ):

        incidents = self.get_all_incidents()

        query_words = set(
            query.lower().split()
        )

        matches = []

        for incident in incidents:

            summary_words = set(
                incident["summary"].lower().split()
            )

            score = len(
                query_words.intersection(
                    summary_words
                )
            )

            if score > 0:

                matches.append(
                (
                    score,
                    incident
                )
            )

        matches.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            item[1]
            for item in matches
        ]