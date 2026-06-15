"""
rca_agent.py

LLM-powered Root Cause Analysis Agent.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class RCAAgent:

    def __init__(self):

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "OPENAI_API_KEY not found "
                "in environment variables."
            )

        self.client = OpenAI(
            api_key=api_key
        )

    def generate_rca(
        self,
        correlation_result,
        incidents,
        learning_context=None
    ):
        """
        Generate RCA using:

        - Current incidents
        - Correlation results
        - Historical incidents
        - Historical resolutions
        """

        historical_context = ""

        if learning_context:

            similar_incidents = (
                learning_context.get(
                    "similar_incidents",
                    []
                )
            )

            historical_resolutions = (
                learning_context.get(
                    "historical_resolutions",
                    []
                )
            )

            historical_context = f"""

Historical Similar Incidents:
{similar_incidents}

Historical Resolutions:
{historical_resolutions}

"""
        prompt = f"""
You are an expert Site Reliability Engineer
and Observability Specialist.

Correlation Result:
{correlation_result}

Incidents:
{incidents}

{historical_context}

Generate a Root Cause Analysis report with
the following sections:

1. Executive Summary

2. Probable Root Cause

3. Impact Assessment

4. Recommended Actions

5. Confidence Assessment

Instructions:

- Use the correlation result to identify
  the most likely root cause.

- Use historical incidents and resolutions
  when available.

- If historical resolutions are relevant,
  reference them in your recommendations.

- Keep the report concise, professional,
  and actionable.

- Focus on operational remediation steps.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content":
                        "You are an expert "
                        "observability and "
                        "root cause analysis engineer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return (
            response
            .choices[0]
            .message
            .content
        )