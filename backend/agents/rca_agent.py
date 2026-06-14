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

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_rca(
        self,
        correlation_result,
        incidents
    ):

        prompt = f"""
You are an expert Site Reliability Engineer.

Correlation Result:
{correlation_result}

Incidents:
{incidents}

Generate a Root Cause Analysis report with:

1. Executive Summary
2. Probable Root Cause
3. Impact Assessment
4. Recommended Actions
5. Confidence Assessment

Keep the response concise and professional.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content":
                        "You are an expert observability "
                        "and root cause analysis engineer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content