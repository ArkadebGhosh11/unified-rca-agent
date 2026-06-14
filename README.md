# Unified RCA Agent

Unified Observability & Root-Cause Analysis (RCA) Agent — telemetry generators, anomaly detectors, and a simple correlation agent for end-to-end RCA experiments.

## Project status
- Telemetry generators implemented: storage, network, compute, application.
- Fault injection and shared fault state manager implemented.
- Anomaly detection (AnomalyAgent) and correlation logic (CorrelationAgent) implemented.
- Incident dataclass model and example scripts/tests included.
- Frontend (Streamlit) and API scaffolds present (some files intentionally minimal).

## Components
- telemetry/: Synthetic telemetry generators and fault_injector.
- backend/agents/: AnomalyAgent and CorrelationAgent implementations.
- backend/models/: Incident dataclass model.
- data/: Topology, sample incidents and fault state JSON files.
- tests/: Basic unit tests demonstrating usage.

## Quickstart
1. Create a Python 3.10+ virtualenv and activate it.
2. Install requirements:

   pip install -r requirements.txt

3. Run a telemetry generator (in separate shells):

   python -m telemetry.storage_generator
   python -m telemetry.network_generator
   python -m telemetry.compute_generator
   python -m telemetry.application_generator

4. Run simple examples from tests or interact with agents:

   python tests/test_incident.py
   python tests/test_anomaly_agent.py
   python tests/test_correlation_agent.py

## Notes about LLM inference (vLLM)
This project intends to run LLM-based inference using vLLM. Install `vllm` and provide a model binary or model path per vLLM documentation. vLLM may require GPU/CUDA and additional dependencies; follow vLLM docs for environment setup.

## Running tests

   pytest -q
